
import document
import canvas
import urllib2
import math
import random

DIR = "http://mrt2.no-ip.org/skulpt/assets/"
WIDTH = 500
HEIGHT = 500


images = {}

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)



class Media:
  
  def __init__(self, name, image, radius,center, size, size2 = None):
    self.radius = radius
    self.name = name
    self.image = canvas.load_image(image) 
    self.center = center
    self.size = size
    if size2 == None:
      self.size2 = self.size     
    else:
      self.size2 = size2
  def get_center(self):
    return self.center
  def get_name(self):
    return self.name
  def get_image(self):
    return self.image
  def get_size(self):
    return self.size
  def get_radius(self):
    return self.radius
      
class Sprite:
    def __init__(self , pos, vel, info, ang=0, ang_vel=0, music = 'None'):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.info = info
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = info.get_image()
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.exploded = False
        
    def set_pos(self,x,y):
        self.pos = [x,y]
    def set_vit(self,x,y):
        self.vel = [x,y]    
    def set_angle(self,a):
        self.angle = a
    def explode(self):
      self.exploded = True
    

    def update(self):
        
        self.angle += self.angle_vel 
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        if self.info.get_name() == 'asteroid':
                       
            self.pos[0] = self.pos[0] % WIDTH
            self.pos[1] = self.pos[1] % HEIGHT

class Ship:
 
  def __init__(self, pos, vel, info, angle = 0, vel_angle = 0):
    
    self.pos = pos
    self.vel = vel
    self.info = info
    self.angle = angle
    self.vel_angle = vel_angle
    self.friction = 0.1
    self.thrust = False
    self.radius = self.info.radius
  def destroy(self):
    global lives, end_game
    if lives>0:
      lives -= 1
    else:
      end_game = True
  def shoot(self, m):
    m.set_pos(self.pos[0],self.pos[1]) 
    m.set_angle(self.angle)
    angle = ((1.0*self.angle)/360.0)*2.0*math.pi
    v = [1.0*math.cos(angle), 1.0*math.sin(angle)]
    m.set_vit(self.vel[0] + 10*v[0] , self.vel[1]+10*v[1])
       
  
  def inc_angle(self):
    self.vel_angle = 5
  def dec_angle(self):
    self.vel_angle = -5
  def stop_angle(self):
    self.vel_angle = 0  
  
  
  def set_vel(self, value):
    self.vel = value
  def set_thrust(self, value):
    self.thrust = value
  def set_angle(self, value):
    self.angle = value
  def get_angle(self):
    return self.angle
    
  def update(self):
    
    
    self.set_angle(self.get_angle() + self.vel_angle)
    
    if self.thrust:
      self.info.center = (135,45)
      angle = ((1.0*self.angle)/360.0)*2.0*math.pi
      acc = [1.0*math.cos(angle), 1.0*math.sin(angle)]
         
      self.vel[0] = 5 * acc[0]
      self.vel[1] = 5 * acc[1]
      
    else:
      self.info.center = (45,45)
      
    self.vel[0] *= 1-self.friction 
    self.vel[1] *= 1-self.friction
    
    self.pos[0] = self.pos[0]+self.vel[0]
    self.pos[1] = self.pos[1]+self.vel[1]
    
    self.pos[0] =  self.pos[0] % WIDTH
    self.pos[1] =  self.pos[1] % HEIGHT 
    
    
      
class Game: 
  global end_game
  def timer(self):
    pass
  
  def new_game(self):
  
    canvas.clear_timers()
    self.t.stop()
    self.t.start()
    self.t2.stop()
    self.t2.start()
   


  def debug(self, vl):
    console = document.getElementById("output")
    console.innerHTML =""
    console.innerHTML = str(vl)
  
  def get_kb(self):
    ms = document.getElementById("editor").value
    if len(ms) == 0:
      return None
    else:
      return ms
        
  def check_collision(self):
    global score
    #test collision betwenn missile and rocks
    p = self.a_rock
    q = self.a_missile
    if dist(p.pos,q.pos) < p.info.radius+ q.info.radius:
      score += 1
      self.a_missile.set_pos(-1,-1)
      self.a_missile.set_vit(0,0)
      self.a_rock.explode()
    p = self.a_rock
    q = self.ship
    if dist(p.pos,q.pos) < (p.info.radius+ q.radius)-10:
      self.ship.destroy()
      self.a_rock.set_pos(250,250)
    
      
  def render(self):
    global a_missile, lives, score
    
          
    if lives == 0:
      canvas.draw_text("YOU LOOSE :(",(200,230),30,"Red")
      return
    
    self.time += 1
    wtime = (self.time / 4) % WIDTH
    
    canvas.clear()
    canvas.draw_image(self.fond.get_image(),self.fond.center,self.fond.size,(250,250),self.fond.size2,0)
    canvas.draw_image(self.debris.get_image(), self.debris.get_center(), self.debris.get_size(), (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT),0)
    canvas.draw_image(self.debris.get_image(), self.debris.get_center(), self.debris.get_size(), (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT),0)

    canvas.draw_image(self.ship.info.image,self.ship.info.center,self.ship.info.size,self.ship.pos,self.ship.info.size2,self.ship.angle)
    #canvas.draw_circle(self.ship.pos[0],self.ship.pos[1],self.ship.radius)
    canvas.draw_image(self.a_missile.info.image,self.a_missile.info.center,self.a_missile.info.size,self.a_missile.pos,self.a_missile.info.size2,self.a_missile.angle)  
   
    
    if self.a_rock.exploded:
      if (wtime) % 24 == 0:
        self.a_rock.exploded = False
        x = random.randrange(0,2)
        y = random.randrange(0,HEIGHT)
        x = x * WIDTH
        self.a_rock.set_pos(x,y)
        if x == 0:
          vx = 1
        else:
          vx = -1
        vy = 1
        self.a_rock.set_vit(vx,vy)
      #self.a_rock.exploded = False
      canvas.draw_image(self.a_rock_exploded.info.image,
                        (self.a_rock_exploded.info.center[0]
                         +((wtime) % 24)*self.a_rock_exploded.info.size[0],
                         self.a_rock_exploded.info.center[1]),
                        self.a_rock_exploded.info.size,
                        self.a_rock.pos,
                        self.a_rock_exploded.info.size,
                        0)  

    else:
      canvas.draw_image(self.a_rock.info.image,self.a_rock.info.center,self.a_rock.info.size,self.a_rock.pos,self.a_rock.info.size2,self.a_rock.angle)  
    canvas.draw_text("lives: "+str(lives)+" score: "+str(score),(320,30),24,'Orange')
    
    #canvas.draw_circle(self.a_rock.pos[0],self.a_rock.pos[1],self.a_rock.radius)
    
    c = self.get_kb()
    if c == '32':
      self.ship.shoot(self.a_missile)
    if c == '37':
      self.ship.dec_angle()
    if c == '39':
      self.ship.inc_angle()
    if c == '38' and (self.time % 10 == 0):
      self.ship.set_thrust(True)
    if c == None:
      self.ship.stop_angle()
      self.ship.set_thrust(False)
      
    self.ship.update()
    self.a_missile.update()
    self.a_rock.update()
    self.check_collision()
    
    
  def __init__(self):
    self.time = 0
    self.t = canvas.create_timer(25, self.render)
    self.t2 = canvas.create_timer(1000, self.timer)
    self.new_game()
    
    self.fond = Media("fond",DIR+"nebula_blue.s2014.png",0,(400,300),(800,600),(500,500))
    self.debris = Media("debris",DIR+"debris2_blue.png",0,(320, 240), (640, 480),(500,500))

    info = Media("ship",DIR+"double_ship.png",45,(45,45),(90,90),(75,75))
    self.ship = Ship([235.5,235,5],[1,0], info)
    info = Media("missile",DIR+"shot2.png",5,(5,5),(10,10))
    self.a_missile = Sprite([0,0],[0,0],info)
    info = Media("asteroid",DIR+"asteroid_blue.png",30,(45,45),(90,90),(60,60))
    self.a_rock = Sprite([0,HEIGHT/2],[1,1],info,1,1)
    info = Media("explosion",DIR+"explosion_alpha.png",64,(64, 64), (128, 128),(128, 128))
    self.a_rock_exploded = Sprite([0,0],[0,0],info) 
    
end_game = False
game = Game()
lives = 3
score = 0
