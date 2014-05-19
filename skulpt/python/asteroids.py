#asteroids
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5

class ImageInfo:
    def __init__(self, name, center, size, radius = 0, lifespan = None, animated = False):
        self.name = name
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_name(self):
        return self.name    
        
    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo("debris",[320, 240], [640, 480])
debris_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo("nebuleuse",[400, 300], [800, 600])
nebula_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo("splash",[200, 150], [400, 300])
splash_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/splash.png")

# ship image
ship_info = ImageInfo("ship",[45, 45], [90, 90], 35)
ship_thrust = ImageInfo([135, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo("missile",[5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo("asteroid",[45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo("explosion",[64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://mrt2.no-ip.org/skulpt/assets/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    global a_missile
    def __init__(self, pos, vel, angle, image, info):
        self.accel = 0
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.friction = 0.005
        
    def shoot(self, missile):
        v = angle_to_vector(self.angle)
        missile.set_pos(self.pos[0],self.pos[1])
        missile.set_angle(self.angle)
        missile.set_vit(self.vel[0] + 10*v[0] , self.vel[1]+10*v[1])
        missile_sound.play()
        
    def draw(self,canvas):
        if self.thrust:
            center = (self.image_center[0]+self.image_size[0],self.image_center[1] ) 
        else:
            center = self.image_center
        canvas.draw_image(self.image, center , self.image_size, self.pos, self.image_size, self.angle )

    def update(self):
        self.angle += self.angle_vel
        vector = angle_to_vector(self.angle)
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
        
        self.vel[0] *= (1 - self.friction)
        self.vel[1] *= (1 - self.friction)
        
        if self.thrust:
            self.vel[0] = vector[0]
            self.vel[1] = vector[1]
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.info = info
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
    def set_pos(self,x,y):
        self.pos = [x,y]
    def set_vit(self,x,y):
        self.vel = [x,y]    
    def set_angle(self,a):
        self.angle = a
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center , self.image_size, self.pos, self.image_size, self.angle )

    def update(self):
        
        self.angle += self.angle_vel 
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        if self.info.get_name() == 'asteroid':
                       
            self.pos[0] = self.pos[0] % WIDTH
            self.pos[1] = self.pos[1] % HEIGHT
        
    
           
def draw(canvas):
    global time, lives, score 
    
    # animiate background
    soundtrack.play()
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    canvas.draw_text("lives: "+str(lives)+" score: "+str(score), (600, 30), 30,'White')
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    x = random.randrange(0, 2)
   
    x = x * WIDTH
    if x == 0:
        vx = 1
    else:
        vx = -1
    y = random.randrange(30, HEIGHT)
    vx *= random.randrange(2, 50)
    vy = random.randrange(2, 50)
    a_rock = Sprite([x,y], [vx/10,vy/10], 0, 0.1, asteroid_image, asteroid_info)
    
def key_up(code):
    global my_ship
    my_ship.angle_vel = 0
    my_ship.accel = 0
    my_ship.thrust = False
    ship_thrust_sound.pause()
    ship_thrust_sound.rewind()
    
def key_down(code):
    
    global my_ship, a_missile
    if (code == 38):
        my_ship.thrust = True
    if (code == 37):
        my_ship.angle_vel -= 0.1
    if (code == 39):
        my_ship.angle_vel += 0.1
    if (code == 32):
        my_ship.shoot(a_missile)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([0,HEIGHT/2], [8,8], 0, 0.1, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
timer = simplegui.create_timer(3000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
