import canvas, math, math2
canvas.clear_timers()

W = 500
H = 500
NB_POINTS = 64.0

x_min = -1.15
y_min = -1.1
x_max = 3.15
y_max = 1.1
x = []
y = None


#fonction de calcul de la sortie
def process(val):
  global varss, x, y, x_min, y_min, x_max, y_max
  #elaboration de x
  x = []
  y = None
  for i in range(int(NB_POINTS)+1):
    ech = 1.0*x_min +1.0*i*((1.0*x_max-1.0*x_min)/(1.0*NB_POINTS))
    x.append([ech])
  #print x
  #variables generales
  varss = {'x': 0 }
  parser = math2.RpnMathParser(val, varss); 
  out = parser.get_result()
  y = parser.update(['x'], x ); 
  #print y

#
#creation de l'interface
inp = canvas.add_input("equ:",process,200)
inp.set_text("sin(x)")
process(inp.get_text())


#ceci est la fonction qui dessine l'ecran toutes les 17 millisecondes
def draw(cnvs):
  
  global x_min,y_min,x_max,y_max, x, y
  #print len(y)
  #canvas.fill_rect(0,0,W,H)
  last = (0,H/2)
  axex = 0
  if y == None:
    return 
  for i in range(len(y)):
    ab = x[i][0]
    #print ab
    ordon = float(y[i])
    x1 = ((ab - x_min) / (x_max - x_min))* W
    y1 = H - ((ordon - y_min) / (y_max - y_min))* H
    axex = (( - x_min) / (x_max - x_min))*W 
    axey = H - ((- y_min) / (y_max - y_min))* H
    canvas.draw_line((0,axey), (W,axey), 1, 'White')
    canvas.draw_line((axex,0), (axex,H), 3, 'White')
    #y1 = -5*x1
    #canvas.draw_circle((x1,y1), 2, 2, 'Blue', 'Yellow')
    #canvas.draw_text(str(ab)+" "+str(ordon),(x1,y1),12,'Red')
    if i>0:
      canvas.draw_line((x1,y1), last, 2, 'Yellow')
    
    last = (x1,y1) 
    #print ab,ordon
  
#appel de la temporisation de dessin de l'ecran  
  
canvas.start("Purple")
canvas.set_draw_handler(draw)



