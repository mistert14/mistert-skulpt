
import document
import canvas
import urllib2

URL = "http://mrt2.no-ip.org/skulpt/donne_mot.php"

class Pendu:
  
  def new_game(self):
  
    #global mot, to_find, letters, to_find, msg, errors, end_game, t
  
    canvas.clear_timers()
  
    f = urllib2.urlopen(URL)
    mots =  f.readlines()
    mots.pop(-1)
    self.mot = ''.join(str(x) for x in mots) 

    self.to_find = []
    self.letters = []

    for c in self.mot:
      if not(c in self.to_find):
        self.to_find.append(c)
   
    self.msg = None
    self.errors = 1
    self.end_game = False

    self.t.stop()
    self.t.start()
  

  def get_mouse(self):
    ms = document.getElementById("mouse").innerHTML
    ms2 = document.getElementById("mouse")
    if ms == "mouse ...":
      return None
    if int(ms.split(':')[1]) <= 18:
    
      ms2.innerHTML = "mouse ..."
      html = ms
      code =  int(html.split(':')[0]) // 18
      return (chr(65+code))
    else:
      ms2.innerHTML = "mouse ..."
      return None

  def mouse_handler(self,ch):
  
  #global letters, to_find, errors, end_game, msg, mot
  
    if (ch == "[") and (self.end_game):
      self.new_game()
    if ch in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-']:
      if not(ch in self.letters):
        self.letters.append(ch)
      if (ch in self.mot) and (ch in self.to_find):
        self.to_find.remove(ch)
      if len(self.to_find) == 0:
        self.end_game = True
        self.msg = "YOU WIN!"
      else:
        if (ch in self.mot):
          return
        else:
          self.errors += 1
          if self.errors >=12:
            self.end_game = True
            self.msg = "YOU LOOSE! "+str(self.mot)
 
  def render(self):
  
    #global errors, mot, to_find, msg , end_game
  
    canvas.clear()
  
    if self.msg <> None:
      canvas.draw_text(200,250,self.msg)
  
    if self.end_game:
      canvas.add_button(26*18,0,18,18,"@")
    
    c = self.get_mouse()
    if c <> None:
      #une lettre est cliquee mouse_handler
      #canvas.draw_text(200,250,c)
      self.mouse_handler(c)
    
  
    w = 18
    for i in range(26):
      canvas.add_button(i*w,0,18,18,chr(65+i))
  
  
    n = len(self.mot)
    p = (500 * 2) / ( 3*n + 1 )
    e = p / 2
    
    for i in range(len(self.mot)):
      if self.mot[i] in self.to_find:
        canvas.draw_line((i+1)*e+(i)*p,80,(i+1)*(e+p),80)
      else:
        a = (i+1)*e+(i)*p
        b = (i+1)*(e+p)
        canvas.draw_text((a+b)/2 - e/2 , 70, self.mot[i])
  
  
    if (self.errors > 1):
      canvas.draw_line(100,400,200,400)
    if (self.errors >= 2):
      canvas.draw_line(100,400,200,400)  
    if (self.errors >= 3):
      canvas.draw_line(150,400,150,150)
    if (self.errors >= 4):
      canvas.draw_line(150,150,300,150)
    if (self.errors >= 5):
      canvas.draw_line(225,150,150,230)
    if (self.errors >= 6):
      canvas.draw_line(300,150,300,180)
    if (self.errors >= 7):
      canvas.draw_circle(300,200,20)
    if (self.errors >= 8):
      canvas.draw_line(300,220,300,300)
    if (self.errors >= 9):
      canvas.draw_line(300,300,330,360)
    if (self.errors >= 10):
      canvas.draw_line(300,300,270,360)
    if (self.errors >= 11):
      canvas.draw_line(300,240,330,300)
    if (self.errors >= 12):
      canvas.draw_line(300,240,270,300)


  def __init__(self):
    self.t = canvas.create_timer(200, self.render)
    self.new_game()

pendu = Pendu()
