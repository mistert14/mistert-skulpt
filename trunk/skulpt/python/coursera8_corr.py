# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
NUM_ROCKS = 9
score = 0
lives = 3
time = 0.5

class ImageInfo:
    def __init__(self, name, image, center, size, radius = 0, lifespan = None, animated = False):
        self.name = name
        self.center = center
        self.size = size
        self.radius = radius
        self.image = simplegui.load_image(image)
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_name(self):
        return self.name    
    def get_image(self):
        return self.image      
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
debris_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png"
debris_info = ImageInfo("debris",debris_image,[320, 240], [640, 480])

# nebula images - nebula_brown.png, nebula_blue.png
nebula_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png"
nebula_info = ImageInfo("nebuleuse",nebula_image,[400, 300], [800, 600])

# splash image
splash_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png"
splash_info = ImageInfo("splash",splash_image,[200, 150], [400, 300])

# ship image
ship_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png"
ship_info = ImageInfo("ship",ship_image,[45, 45], [90, 90], 35)
ship_thrust = ImageInfo("thrust",ship_image,[135, 45], [90, 90], 35)

# missile image - shot1.png, shot2.png, shot3.png
missile_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png"
missile_info = ImageInfo("missile",missile_image,[5,5], [10, 10], 3, 50)

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png"
asteroid_info = ImageInfo("asteroid",asteroid_image,[45, 45], [90, 90], 40)

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_image = "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png"
explosion_info = ImageInfo("explosion",explosion_image,[64, 64], [128, 128], 17, 24, True)

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

def process_sprite_group(canvas,group):
    
    for elem in set(group):
        
        elem.draw(canvas)
    for elem in set(group):
        test = elem.update()
        if test:
            group.remove(elem)
    
def group_collide(group,other):
    
    global explosion_image, explosion_info, explosion_sound
    count=0
     
    for elt in set(group):
        if elt.collide(other):
                
                if elt.info.get_name() == 'missile':
                    #def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
                    explo = Sprite(elt.pos, (0,0),0,0,explosion_image, explosion_info, explosion_sound)
                    explosion_group.add(explo)
                    
                    explosion_sound.rewind()
                    explosion_sound.play()
                group.remove(elt)
                count+=1
    return count
           

def group_group_collide(group1,group2):
    global explosion_group
    count= 0
    for elt in set(group1):
        elt_count=group_collide(group2,elt)
        if elt_count>0:
            count+=elt_count
            group1.remove(elt)
            
                
    return count

# Ship class
class Ship:
    
    def __init__(self, pos, vel, angle, image, info):
        angle = 0
        self.accel = 0
        self.pos = pos
        self.vel = vel
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.info = info
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.friction = 0.005
    
    def get_radius(self):
        return self.radius
    def get_position(self):
        return [self.pos[0],self.pos[1]]
    
    def shoot(self, missiles):
        global missile_info
              
        v = angle_to_vector(self.angle)
        pos = (self.pos[0],self.pos[1])
        vit = (self.vel[0] + 10*v[0] , self.vel[1]+10*v[1])
        a_missile = Sprite(pos, vit, self.angle, 0, missile_image, missile_info, missile_sound)
        missiles.add(a_missile)
        missile_sound.play()
        
    def draw(self,canvas):
        if self.thrust:
            center = (self.image_center[0]+self.image_size[0],self.image_center[1] ) 
        else:
            center = self.image_center
        canvas.draw_image(self.info.get_image(), center , self.image_size, self.pos, self.image_size, self.angle )

    def update(self):
        
        self.angle += self.angle_vel
                   
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
        
        self.vel[0] *= (1 - self.friction)
        self.vel[1] *= (1 - self.friction)
        
        if self.thrust:
            #angle = (self.angle / 360.0) * 2.0 * math.pi
            vector = angle_to_vector(self.angle)
            self.vel[0] = 5*vector[0]
            self.vel[1] = 5*vector[1]
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
    
    def get_radius(self):
        return self.radius
    def get_position(self):
        return self.pos        
            
    def set_pos(self,x,y):
        self.pos = [x,y]
    def set_vit(self,x,y):
        self.vel = [x,y]    
    def set_angle(self,a):
        self.angle = a
    def collide(self,other):
        
        pos1 = self.get_position()
        pos2 = other.get_position()
                
        if dist(pos1,pos2) <= self.radius + other.get_radius():
            return True
        else:
            return False
        
        
    def draw(self, canvas):
        if self.animated:
            center = list([self.image_center[0] + (self.age % 30)*self.image_size[0] ,self.image_center[1]])
            canvas.draw_image(self.info.get_image(), center , self.image_size, self.pos, self.image_size, self.angle )
        else:
            
            canvas.draw_image(self.info.get_image(), self.image_center , self.image_size, self.pos, self.image_size, self.angle )

    def update(self):
        global explosion_group
                
        self.age += 1    
        self.angle += self.angle_vel 
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        if self.info.get_name() == 'asteroid':
                       
            self.pos[0] = self.pos[0] % WIDTH
            self.pos[1] = self.pos[1] % HEIGHT
        if self.info.get_name() == 'explosion':
            if self.age > self.lifespan:
                explosion_group.remove(self)
                
            
            
        if self.info.get_name() == 'missile':
                        
            if self.age <= self.lifespan:
                return False
            else:
                return True
        return False
               
def draw(canvas):
    global time, lives, score, started, timer, rock_group, missile_group, explosion_group,my_ship
    
    # animiate background
    soundtrack.play()
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    
    canvas.draw_image(nebula_info.get_image(), nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_info.get_image(), center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_info.get_image(), center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

   
    # draw ship and sprites
    my_ship.draw(canvas)
    my_ship.update()
    
    process_sprite_group(canvas,rock_group)
    process_sprite_group(canvas,missile_group)
    process_sprite_group(canvas,explosion_group)
    
   
    
    
   
    if (started == False):
        canvas.draw_image(splash_info.get_image(), splash_info.get_center(),   
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],   
                          splash_info.get_size())  
          
    else:
        #detecting collisons asteroids and ship
        collisions = group_collide(rock_group, my_ship)
        if collisions>0:
            lives -= 1
            if lives == 0:
                started = False
                rock_group = set([])
                timer.stop()
        
        destructions = group_group_collide(rock_group,missile_group)
        score += destructions
     
    canvas.draw_text("lives: "+str(lives)+" score: "+str(score), (600, 30), 30,'White')

    
    # timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    copy = set(rock_group)
    if len(copy) < NUM_ROCKS:
        x = random.randrange(0, 2)
        x = x * WIDTH
        if x == 0:
            vx = 1
        else:
            vx = -1
        y = random.randrange(30, HEIGHT)
        vx *= random.randrange(2, 50)
        vy = random.randrange(2, 50)
        rock = Sprite([x,y], [vx/10,vy/10], 0, 0.1, asteroid_image, asteroid_info)
        copy.add(rock)
    rock_group = copy
        
def key_up(code):
    global my_ship
    my_ship.angle_vel = 0
    my_ship.accel = 0
    my_ship.thrust = False
    ship_thrust_sound.pause()
    ship_thrust_sound.rewind()
    
def key_down(code):
    
    global my_ship, missile_group
    if code == simplegui.KEY_MAP['up']:
         my_ship.thrust = True
    if code == simplegui.KEY_MAP['left']:
        my_ship.angle_vel -= 0.1
    if code == simplegui.KEY_MAP['right']:
        my_ship.angle_vel += 0.1
    if code == simplegui.KEY_MAP['space']:
        my_ship.shoot(missile_group)
    
def click(pos):
    global started,lives,score, timer
    started = True
    score = 0
    lives = 3
    timer.start()
    soundtrack.rewind()
    soundtrack.play()
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])
started = False

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(2000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

