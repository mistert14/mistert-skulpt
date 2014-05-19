#binaire_et_corr
#binaire_et
import canvas
canvas.clear_timers()
#canvas.clear()

bits = {'A': 0, 'B': 0, 'C': 0 }

def process(val):
  #ceci est le compilateur binaire
  global bits
  for i in range(3):
    val = val.replace('A', str(int(bits['A'])))
    val = val.replace('B', str(int(bits['B'])))
    val = val.replace('C', str(int(bits['C'])))
    val = val.replace('((0))', '0')
    val = val.replace('((1))', '1')
    val = val.replace('(0)', '0')
    val = val.replace('(1)', '1')
    val = val.replace('/0', '1')
    val = val.replace('/1', '0')
    val = val.replace('0.0', '0')
    val = val.replace('0.1', '0')
    val = val.replace('1.0', '0')
    val = val.replace('1.1', '1')
    val = val.replace('(0.0)', '0')
    val = val.replace('(0.1)', '0')
    val = val.replace('(1.0)', '0')
    val = val.replace('(1.1)', '1')
    val = val.replace('0+0', '0')
    val = val.replace('0+1', '1')
    val = val.replace('1+0', '1')
    val = val.replace('1+1', '1')
    val = val.replace('(0+0)', '0')
    val = val.replace('(0+1)', '1')
    val = val.replace('(1+0)', '1')
    val = val.replace('(1+1)', '1')
  
  
  return val

def checkA(value):
  global bits
  if value:
    bits['A'] = 1
  else:
    bits['A'] = 0
  
def checkB(value):
  global bits
  if value:
    bits['B'] = 1
  else:
    bits['B'] = 0
    
def checkC(value):
  global bits
  if value:
    bits['C'] = 1
  else:
    bits['C'] = 0 
    
def check(val):
  process(val)

canvas.add_checkbox("chkA","A",checkA,20)
canvas.add_checkbox("chkB","B",checkB,20)
canvas.add_checkbox("chkC","C",checkC,20)
inp = canvas.add_input("equ:",check,200)
inp.set_text("A.(/B+/C)")

def color(value):
  if value == '1':
    return 'Yellow'
  else:
    return 'White'

def draw(mycanvas):
  #ceci est la fonction qui gere l'ecran
  global bits
  left = 80
  top = 30
  canvas.draw_line((0,30+top),(500,30+top),4,'Blue')  
  cl2 = 'Yellow'
  
  canvas.draw_text("ENTREES",(left-30,25+top),24,cl2)
  canvas.draw_text("SORTIES",(left+250,25+top),24,cl2)
  canvas.draw_circle((left, 50+top), 10, 2, 'Blue', color(str(bits['A'])))
  canvas.draw_circle((left, 73+top), 10, 2, 'Blue', color(str(bits['B'])))
  canvas.draw_circle((left, 96+top), 10, 2, 'Blue', color(str(bits['C'])))

  equ = process(inp.get_text())
  canvas.draw_circle((left+250, 50+top), 10, 2, 'Blue', color(equ))
  
  canvas.draw_text("A: "+str(bits['A']),(left+15,58+top),24,cl2)
  canvas.draw_text("B: "+str(bits['B']),(left+15,80+top),24,cl2)
  canvas.draw_text("C: "+str(bits['C']),(left+15,102+top),24,cl2)
  canvas.draw_text(inp.get_text(),(left+265,58+top),24,cl2)
  
  """
  A FAIRE:
  
  Dessiner avec draw_circle et draw_line les interrupteurs
  et les faire basculer et eteindre quand les entrees changent
  
  """
  #dessin des fils
  
  canvas.draw_line((0,290+top),(100,290+top),3,'Blue')
  canvas.draw_line((150,290+top),(200,290+top),3,'Blue')
  canvas.draw_line((200,230+top),(200,350+top),3,'Blue')
  canvas.draw_line((200,230+top),(250,230+top),3,'Blue')
  canvas.draw_line((200,350+top),(250,350+top),3,'Blue')
  canvas.draw_line((300,230+top),(350,230+top),3,'Red')
  canvas.draw_line((300,350+top),(350,350+top),3,'Red')
  canvas.draw_line((350,230+top),(350,350+top),3,'Red')
  canvas.draw_line((500,290+top),(350,290+top),3,'Red') 
  canvas.draw_circle((420, 290+top), 30, 2, 'Blue', color(equ))
  
  canvas.draw_text("A",(115,270+top),24,cl2)
  canvas.draw_text("B",(267,210+top),24,cl2)
  canvas.draw_text("C",(267,330+top),24,cl2)
  #dessin des interrupteurs
  
  if bits['A'] == 0:
    canvas.draw_line((100,290+top),(150,270+top),3,'Orange')
  else:
    canvas.draw_line((100,290+top),(150,290+top),3,'Orange')
    
  if bits['B'] == 0:
    canvas.draw_line((250,230+top),(300,230+top),3,'Orange')
  else:
    canvas.draw_line((250,230+top),(300,210+top),3,'Orange')
    
  if bits['C'] == 0:
    canvas.draw_line((250,350+top),(300,350+top),3,'Orange')
  else:
    canvas.draw_line((250,350+top),(300,330+top),3,'Orange')
    
    
  
canvas.start("Purple")
canvas.set_draw_handler(draw)