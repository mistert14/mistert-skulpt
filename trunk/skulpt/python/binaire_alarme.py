import canvas, math2
canvas.clear_timers()
#canvas.clear()
out = '0'
bits = {'A': 0, 'B': 0, 'C': 0 }

def process(val):
  #ceci est le compilateur binaire
  global bits, out
  
  parser = math2.RpnMathParser(val, bits); 
  out = parser.get_result()
  if str(out) == '0.0':
    out = '0'
  else:
    out = '1'
  return out

def check(id,value):
  global bits
  if value:
    bits[id] = 1
  else:
    bits[id] = 0
  
  
canvas.add_checkbox("chkA","A",check,20)
canvas.add_checkbox("chkB","B",check,20)
canvas.add_checkbox("chkC","C",check,20)
inp = canvas.add_input("equ:",process,200)
inp.set_text("A & (not(B) | not(C))")

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
  
  
canvas.start("Purple")
canvas.set_draw_handler(draw)
