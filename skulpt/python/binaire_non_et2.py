import canvas
canvas.clear_timers()


bits = {'A': 1 , 'B':1 }

def checkA(value):
  global bits
  if value:
    bits['A'] = 0
  else:
    bits['A'] = 1
    
def checkB(value):
  global bits
  if value:
    bits['B'] = 0
  else:
    bits['B'] = 1
    
canvas.add_checkbox("chkA","A",checkA,20)
canvas.add_checkbox("chkB","B",checkB,20)

def color(value):
  if value == '1':
    return 'Yellow'
  else:
    return 'White'

def draw():
  #ceci est la fonction qui gere l'ecran
  global bits
  canvas.fill_rect(0,0,500,500)
  left = 80
  top = 30
  canvas.draw_line((0,30+top),(500,30+top),4,'Blue')  
  cl2 = 'Yellow'
  
  canvas.draw_text("ENTREES",(left-30,25+top),24,cl2)
  canvas.draw_text("SORTIES",(left+250,25+top),24,cl2)
  if (bits['A']+bits['B'] >= 1):
    equ = 1
  else:
    equ = 0
  canvas.draw_circle((left, 50+top), 10, 2, 'Blue', color(str(bits['A'])))
  canvas.draw_circle((left, 80+top), 10, 2, 'Blue', color(str(bits['B'])))
 
  canvas.draw_circle((left+250, 50+top), 10, 2, 'Blue', color(str(equ)))
  
  canvas.draw_text("A: "+str(bits['A']),(left+15,58+top),24,cl2)
  canvas.draw_text("B: "+str(bits['B']),(left+15,88+top),24,cl2)
  canvas.draw_text("L: "+str(equ),(left+265,58+top),24,cl2)
 
  canvas.draw_line((0,290+top),(100,290+top),3,'Red')
  canvas.draw_line((150,350+top),(200,350+top),3,'Blue')
  canvas.draw_line((50,350+top),(100,350+top),3,'Red')
  canvas.draw_line((50,350+top),(50,290+top),3,'Red')
  canvas.draw_line((200,350+top),(200,290+top),3,'Blue')
  canvas.draw_line((500,290+top),(150,290+top),3,'Blue') 
  
  canvas.draw_circle((420, 290+top), 30, 2, 'Blue', color(str(equ)))
  
  canvas.draw_text("A",(115,270+top),24,cl2)
  canvas.draw_text("B",(115,320+top),24,cl2)
  canvas.draw_text("L",(410,240+top),24,cl2)
  
  if bits['A'] == 0:
    canvas.draw_line((100,290+top),(150,270+top),3,'Orange')
  else:
    canvas.draw_line((100,290+top),(150,290+top),3,'Orange')
    
  if bits['B'] == 0:
    canvas.draw_line((100,350+top),(150,330+top),3,'Orange')
  else:
    canvas.draw_line((100,350+top),(150,350+top),3,'Orange')
  
  """
  A FAIRE:
  
  Modifier ce programme pour transformer l'interrupteur B en
  le placant en serie apres l'interrupteur A et en
  dessinant le circuit en consequence pour former une fonction

  L = /(A+B)


  A B L
  0 0 1 
  0 1 0
  1 0 0
  1 1 0


  """
  
  
#canvas.start("Purple")
#canvas.set_draw_handler(draw)
t = canvas.create_timer(16,draw)
t.start()



