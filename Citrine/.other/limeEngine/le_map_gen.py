from random import randint

from le_colors import colored

'''
    Note:
        It should be working faster.
                Optimisation decreased the speed, which is strange and dumb.
        But at least it looks better.
        :)
'''

class world():
    def __init__(self, size = 32):
        '''
            Creates the map of the world.
        '''
        self.size_x = size + 4      # longitude
        self.size_y = size*2 + 4    # latitude
        self.map = [[0 for y in range(self.size_y)] for x in range(self.size_x)]
        self.tempMap = self.map
        self.fillMap()
        #self.DEBUG_printMap()
        self.smoothMap()
        self.prepMap()
        self.printMap()

    def fillMap(self, window = 32):
        '''
            Randomly fills the map plane with numbers from [-window; window].
        '''
        for x in range(2, self.size_x - 2):
            for y in range(2, self.size_y - 2):
                self.map[x][y] = randint(-window, window)

    def regionSum(self, x, y, radius):
        '''
            Finds the sum at [x,y] of the surrounding tiles in sertain radius.
        '''
        _sum = 0
        for _x in range(x - radius, x + radius + 1):
            for _y in range(y - radius, y + radius + 1):
                _sum += self.map[_x][_y]
        return _sum

    def smooth(self, radius, level):
        '''
            Smooth the map using given smooth radius and level.
        '''
        while level != 0:
            for x in range(2, self.size_x - 2):
                for y in range(2, self.size_y - 2):
                    self.tempMap[x][y] = self.regionSum(x, y, radius) // ((radius + 1 + radius) ** 2)
            level -= 1
            self.map = self.tempMap

    def smoothMap(self):
        '''
            Sequence of smoothing the map.
            radius  1 - 9   square
                    2 - 25
                    3 - 49
        '''
        self.smooth(2, 1)
        #self.DEBUG_printMap()
        self.smooth(1, 2)
        #self.DEBUG_printMap()

    def prepMap(self, lim = 2):
        '''
            Prepares the map before printing.
        '''
        for x in range(2, self.size_x - 2):
            for y in range(2, self.size_y - 2):
                if self.map[x][y] < -lim:
                    self.map[x][y] = -1
                elif self.map[x][y] > lim:
                    self.map[x][y] = 1
                elif self.map[x][y] >= -lim and self.map[x][y] <= lim:
                    self.map[x][y] = 0
                else:
                    self.map[x][y] = 'N'

    def DEBUG_printMap(self, lim = 2):
        '''
            Prints the map.
        '''
        for x in range(self.size_x):
            for y in range(self.size_y):
                if x==0 or x==1 or y==0 or y==1 or x==self.size_x-1 or x==self.size_x-2 or y==self.size_y-1 or y==self.size_y-2:
                    print(' ', end = '')
                elif self.map[x][y] < -lim:   # sea
                    print(colored('_', 'blue'), end = '')
                elif self.map[x][y] >= -lim and self.map[x][y] <= lim:    # flat
                    print(colored('"', 'green'), end = '')
                elif self.map[x][y] > lim:    # mountains
                    print(colored('^', 'yellow'), end = '')
                else:
                    print(colored(self.map[x][y], 'red'), end = '')
            print()

    def printMap(self):
        '''
            Prints the map.
        '''
        for x in range(self.size_x):
            for y in range(self.size_y):
                if x==0 or x==1 or y==0 or y==1 or x==self.size_x-1 or x==self.size_x-2 or y==self.size_y-1 or y==self.size_y-2:
                    print(' ', end = '')
                elif self.map[x][y] == -1:   # sea
                    print(colored('_', 'blue'), end = '')
                elif self.map[x][y] == 0:    # flat
                    print(colored('"', 'green'), end = '')
                elif self.map[x][y] == 1:    # mountains
                    print(colored('^', 'yellow'), end = '')
                else:
                    print(colored(self.map[x][y], 'red'), end = '')
            print()

    def update(self):
        self.printMap()

world()
