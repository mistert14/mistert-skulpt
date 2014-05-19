import canvas, math, math2
canvas.clear_timers()
#variables generales
bits = {'A': 0, 'B': 0, 'C': 0 }
out = '0'
#fonction de calcul de la sortie
def process(val):
  global bits, out
  
  parser = math2.RpnMathParser(val, bits); 
  out = parser.get_result()
  if str(out) == '0.0':
    out = '0'
  else:
    out = '1'
#gestion des cases a cocher    
def chk(id,value):
  global bits
  if value:
    bits[id] = 1
  else:
    bits[id] = 0
  process(inp.get_text())
#gestion de l'equation
def check(val):
  process(val)
#creation de l'interface
canvas.add_checkbox("chkA","A",chk,20)
canvas.add_checkbox("chkB","B",chk,20)
canvas.add_checkbox("chkC","C",chk,20)
inp = canvas.add_input("equ:",check,200)
inp.set_text("A & (not(B) | not(C))")
process(inp.get_text())

def color(value):
  if value == '1':
    return 'Yellow'
  else:
    return 'White'
#ceci est la fonction qui dessine l'ecran toutes les 17 millisecondes
def draw():
  
  global bits, out
  canvas.fill_rect(0,0,500,500)
  left = 80
  top = 30
  canvas.draw_line((0,30+top),(500,30+top),4,'Blue')  
  cl2 = 'Yellow'
  
  canvas.draw_text("ENTREES",(left-30,25+top),24,cl2)
  canvas.draw_text("SORTIES",(left+250,25+top),24,cl2)
  canvas.draw_circle((left, 50+top), 10, 2, 'Blue', color(str(bits['A'])))
  canvas.draw_circle((left, 73+top), 10, 2, 'Blue', color(str(bits['B'])))
  canvas.draw_circle((left, 96+top), 10, 2, 'Blue', color(str(bits['C'])))

  canvas.draw_circle((left+170, 50+top), 10, 2, 'Blue', color(out))
  
  canvas.draw_text("A: "+str(bits['A']),(left+15,58+top),24,cl2)
  canvas.draw_text("B: "+str(bits['B']),(left+15,80+top),24,cl2)
  canvas.draw_text("C: "+str(bits['C']),(left+15,102+top),24,cl2)
  canvas.draw_text(inp.get_text(),(left+185,58+top),24,cl2)
  
  """
  A FAIRE:
  
  Dessiner avec draw_circle et draw_line les interrupteurs
  et les faire basculer et eteindre quand les entrees changent
  
  """
#appel de la temporisation de dessin de l'ecran  
t = canvas.create_timer(17,draw)  
t.start()



