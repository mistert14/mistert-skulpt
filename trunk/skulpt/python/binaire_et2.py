import canvas
canvas.clear_timers()

bits = {'A': 0 , 'B':0 }

def check(id,value):
  global bits
  if value:
    bits[id] = 1
  else:
    bits[id] = 0
    
canvas.add_checkbox("chkA","A",check,20)
canvas.add_checkbox("chkB","B",check,20)

def color(value):
  if value == '1':
    return 'Yellow'
  else:
    return 'White'

def draw():
  #ceci est la fonction qui gere l'ecran
  global bits
  canvas.clear()
  canvas.fill_rect(0,0,500,500)
  
  left = 80
  top = 30
  canvas.draw_line((0,30+top),(500,30+top),4,'Blue')  
  cl2 = 'Yellow'
  
  canvas.draw_text("ENTREES",(left-30,25+top),24,cl2)
  canvas.draw_text("SORTIES",(left+250,25+top),24,cl2)
  equ = bits['A']*bits['B']
  canvas.draw_circle((left, 50+top), 10, 2, 'Blue', color(str(bits['A'])))
  canvas.draw_circle((left, 80+top), 10, 2, 'Blue', color(str(bits['B'])))
 
  canvas.draw_circle((left+250, 50+top), 10, 2, 'Blue', color(str(equ)))
  
  canvas.draw_text("A: "+str(bits['A']),(left+15,58+top),24,cl2)
  canvas.draw_text("B: "+str(bits['B']),(left+15,88+top),24,cl2)
  canvas.draw_text("L: "+str(equ),(left+265,58+top),24,cl2)
 
  canvas.draw_line((0,290+top),(100,290+top),3,'Red')
  canvas.draw_line((200,290+top),(150,290+top),3,'Blue')
  canvas.draw_line((500,290+top),(250,290+top),3,'Blue') 
  
  canvas.draw_circle((420, 290+top), 30, 2, 'Blue', color(str(equ)))
  
  canvas.draw_text("A",(115,270+top),24,cl2)
  canvas.draw_text("B",(215,270+top),24,cl2)
  canvas.draw_text("L",(410,240+top),24,cl2)
  
  if bits['A'] == 0:
    canvas.draw_line((100,290+top),(150,270+top),3,'Orange')
  else:
    canvas.draw_line((100,290+top),(150,290+top),3,'Orange')
    
  if bits['B'] == 0:
    canvas.draw_line((200,290+top),(250,270+top),3,'Orange')
  else:
    canvas.draw_line((200,290+top),(250,290+top),3,'Orange')
  
  """
  A FAIRE:
  
  Modifier ce programme pour transformer l'interrupteur B en
  le placant en derivation sous l'interrupteur A et en
  dessinant le circuit en consequence
  """
  
  

t = canvas.create_timer(17,draw)
t.start()

