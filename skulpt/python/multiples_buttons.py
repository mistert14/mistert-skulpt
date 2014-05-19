import toto
toto.clear_timers()

boutons = {}

def click(txt):
  code = ord(txt[0])
  #if code == :
  # do this
  
for i in range(26):
  bouton = toto.add_button(chr(65+i),click)
  boutons[bouton.get_text()] = bouton
  
  #boutons.append(bouton.get_text())

def draw(mycanvas):
  pass

 
toto.start("Purple")
toto.set_draw_handler(draw)