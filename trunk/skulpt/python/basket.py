#basket
#basket
#basket
import document
import canvas
import urllib2
import math

DIR = "http://mrt2.no-ip.org/skulpt/assets/"
WIDTH = 500
HEIGHT = 500

images = {}

class Media:
  global images
  def __init__(self, name, image, center, size, size2 = None):
    
    self.name = name
    self.image = image
    images[name] = canvas.load_image(self.image)
    self.center = center
    self.size = size
    if size2 == None:
      self.size2 = self.size
    else:
      self.size2 = size2

class Ball:
  def __init__(self, pos, vel, info, angle = 0, vel_angle = 0):
    self.pos = pos
    self.vel = vel
    self.info = info
    self.angle = angle
    self.vel_angle = vel_angle
    self.friction = 0.0051
    self.acc = [0,0]
    self.shooting = False
    self.score = 0
  
  def get_score(self):
    return int(self.score)
  
  def shoot(self):
    self.acc = [7,-17]
  
  def check(self):
    x1 = 400
    x2 = 500
    y = 146
    radius = self.info.size2[0]/2
    
    if (self.pos[0]-radius >= x1 and self.pos[0]+radius <= x2 
        and self.pos[1] <= y and self.pos[1] > 131):
      self.score +=1
      
     
    
  def update(self):
        
    self.angle += self.vel_angle
    
    
    self.pos[0] += self.vel[0] 
    self.pos[1] += self.vel[1] 
    
    self.vel[1]+=0.5
    
    self.vel[0] *= (1 - self.friction)
    self.vel[1] *= (1 - self.friction)
    
    if self.pos[0] >= 500:
      self.pos[0] = 55
      self.pos[1] = 350.5
    
    if self.pos[1] > 500-25:
      self.pos[1] = 500-25
      self.vel_angle = 0
    
      
      
    
    if self.shooting:
      self.vel_angle = 1
      self.vel[0] = self.acc[0] 
      self.vel[1] = self.acc[1]
    self.check()

class Game: 
  def new_game(self):
    canvas.clear_timers()
    self.t.stop()
    self.t.start()

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

  def render(self):
    self.time += 1
    canvas.clear()
    canvas.draw_image(images[self.fond.name],self.fond.center,self.fond.size,(470,150),self.fond.size2,0)
    canvas.draw_image(images[self.ball.info.name],self.ball.info.center,self.ball.info.size,self.ball.pos,self.ball.info.size2,self.ball.angle)  
    canvas.draw_line((500,146),(400,146),3,'Red')
    canvas.draw_text("Score: "+str(self.ball.get_score()),(370,46),30,'Orange')
    c = self.get_kb()
    if c == '38':
      self.ball.shooting = True
      self.ball.shoot()
    if c == None:
      self.ball.shooting = False
      
    self.ball.update()
    
  def __init__(self):
    self.time = 0
    self.t = canvas.create_timer(25, self.render)
    self.new_game()
    self.fond = Media("fond",DIR+"basket-hoop.png",(200,135),(400,370),(150,150))
    info = Media("ball",DIR+"basketball.png",(128,128),(256,256),(70,70))
    self.ball = Ball([55,350.5],[0,0.981], info,0,1)
    
game = Game()

