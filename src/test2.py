import random
import pygame
from math import sqrt, sin, cos, atan2, ceil
 
WIDTH, HEIGHT = 402, 402
r = 99
origin = (WIDTH/2, HEIGHT/2)
 
 
class radar:
    def __init__(self, screen, sweep, numtargets, headinglength, font16, font8, circles):
        #basic input
        self.screen = screen
        self.sweep = sweep
        self.nt = numtargets
        self.a = headinglength
        self.c = circles
        #colors
        self.green = (0, 255, 0)
        self.color = (0, 0, 0)
        self.visualcolor = (25, 50, 25)
        #heading render components
        self.headingpos = []
        self.degreepos = []
        self.ax0, self.ay0, self.ax1, self.ay1 = 0, 0, 0, 0
        self.font16 = font16
        self.font8 = font8
        #sweep render components
        self.sweeppos = []
        #target render components
        self.targets = []
        self.dtargets = []
        self.dx, self.dy = 0, 0
        self.degreeinc = 0
        self.origin = (round(WIDTH/2), round(HEIGHT/2))
        self.detectbool = False
        self.timer = 0
        self.r = 100
        self.visual()
 
 
    def visual(self):
        #create heading position coordinates before rendering starts
        for i in range(ceil(self.r / self.a)):
            b = i * 3
            self.ax0, self.ay0, self.ax1, self.ay1 = (b * cos(-1.570)) + 200, (b * sin(-1.570)) + 200, (i * cos(-1.570)) + 200, (i * sin(-1.570)) + 200
            list = [self.ax0, self.ay0, self.ax1, self.ay1]
            self.headingpos.append(list)
 
        #create coordinates before rendering starts
        for i in range(18):
            d = -1.570 + (i * 0.349)
            r = self.r + 20
            x, y = (r * cos(d)) + 187, (r * sin(d)) + 192
            list = [x, y]
            self.degreepos.append(list)
 
    #create a sweep that visualizes the radar sweep
    def calc_sweep(self, degrees):
        for i in range(self.sweep):
            endposx = ((r) * cos(degrees - (i / r))) + 200
            endposy = ((r) * sin(degrees - (i / r))) + 200
            ci = i / 2
            pygame.draw.rect(self.screen, (100 - ci, 180 - ci, 100 - ci), (endposx, endposy, 1, 1))
 
    # "detects" targets on screen
    def detected(self):
        a = 0
        b = 255
        if self.detectbool:
            a += 1
            b -= a
            self.color = (0, b, 0)
            #render targets that cross with the radar line
            if self.dtargets[len(self.dtargets) - 1][2] - self.dtargets[0][2] >= self.sweep * 19:
                self.dtargets.pop(0)
            for i in range(len(self.dtargets)):
                pygame.draw.rect(self.screen, self.color,(self.origin[0] + self.dtargets[i][0], self.origin[1] +
                                        self.dtargets[i][1], 1 + random.randint(0, 2), 1 + random.randint(0, 2)))
 
    #render engine
    def render(self, degrees):
        x = (r * cos(degrees)) + 200
        y = (r * sin(degrees)) + 200
        b, c = 0, 0
        time = pygame.time.get_ticks()
        #rotate line from positive to negative
        if self.degreeinc >= 3.1415:
            self.degreeinc = 0
        self.degreeinc += 0.001
        if degrees >= 3.1415:
            degrees = -3.1415 + self.degreeinc
        #render target if hit by radar line
        for i in range(len(self.targets) - 1):
            #find x and y values, used for rendering dots
            h = atan2(self.targets[i][1], self.targets[i][0])
            if round(h, 3) == round(degrees, 3):
                print("detected", round(h, 3))
                self.detectbool = True
                self.dx, self.dy = self.targets[i][0], self.targets[i][1]
                list = [self.dx, self.dy, time]
                self.dtargets.append(list)
        self.detected()
        self.calc_sweep(degrees)
        pygame.draw.aaline(self.screen, self.green, (self.origin[0], self.origin[1]), (x, y))
        #render heading
        for i in range(round(self.r / self.a)):
            b = i*3
            for j in range(self.a):
                if j * b < self.r:
                    pygame.draw.rect(self.screen, self.green, ((r * cos(-1.570)) + 200, ((j * b) * sin(-1.570)) + 200, 1, 1) )
        #render degree offset text
        for i in range(len(self.degreepos)):
            b = i * 20
            degree = self.font16.render(str(b), True, (0, 255, 0))
            self.screen.blit(degree, (self.degreepos[i][0], self.degreepos[i][1]))
        #degree offset lines
        for i in range(18):
            d = -1.570 + (i * 0.349)
            x, y = round(r * cos(d) + 200), round(r * sin(d) + 200)
            pygame.draw.aaline(self.screen, self.visualcolor, (self.origin), (x, y))
        #circle mile indicators
        for i in range(self.c):
            i = i + 1
            radius = self.r / (self.c / i)
            x, y = round(radius * cos(-1.4) + 200), round(radius * sin(-1.4) + 200)
            if radius >= self.r:
                continue
            else:
                pygame.draw.circle(self.screen, self.visualcolor, self.origin, radius, 1)
            degree = self.font8.render(str(radius), True, (0, 255, 0))
            self.screen.blit(degree, (x, y))
 
 
    def gen_targets(self):
        #generate random points on grid within circle radius
        for i in range(self.nt):
            degree = random.randint(0, 360)
            x = (r * cos(degree)) + random.randint(5, r - 1)
            y = (r * sin(degree)) + random.randint(5, r - 1)
            d = sqrt(x*x + y*y)
            if d > 100:
                continue
            else:
                z = random.randint(0, 75)
                if z <= 25:
                    x = -x
                elif z > 25 and z <= 50:
                    y = -y
                elif z > 50 and z <= 75:
                    x = -x
                    y = -y
                gen_t = [x, y]
                self.targets.append(gen_t)
 
def main():
    TICKRATE = 720
    running = True
    pygame.init()
    font16 = pygame.font.SysFont('couriernew', 16)
    font8 = pygame.font.SysFont('couriernew', 8)
    clock = pygame.time.Clock
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.init()
    #main setup
    degrees = 0
    #create radar and generate imaginary targets
    render_radar = radar(screen, 200, 100, 3, font16, font8, 4)
    render_radar.gen_targets()
    while running:
        clock().tick(TICKRATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        #rotate the radar line
        degrees += 0.001
        if degrees >= 3.1415*2:
            degrees = 0
        #background
        pygame.draw.circle(screen, (10, 20, 10), origin, 100)
        #self explanatory
        render_radar.render(degrees)
        pygame.display.update()
 
 
if __name__ == '__main__':
    main()