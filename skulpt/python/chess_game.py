#chess_game
#chess_game
import chess
import canvas

ML = 60
MT = ML
W = 500

partie = [
"e4","b6","d4","Bb7","Bd3","f5","exf5","Bxg2",
"Qh5+", "g6","fxg6","Nf6","gxh7+","Nxh5","Bg6#"
]


pieces = { 
'K':(0,0),'Q':(0,1),'R':(0,2),'B':(0,3),'N':(0,4),'P':(0,5),
'k':(1,0),'q':(1,1),'r':(1,2),'b':(1,3),'n':(1,4),'p':(1,5),
}

echiquier = canvas.load_image("http://mrt2.no-ip.org/skulpt/assets/echiquier.gif")
echiquier_size = (200,200)

pions = canvas.load_image("http://mrt2.no-ip.org/skulpt/assets/pions_echecs.gif")
pions_size = (60,58.5)
pions_center = (30,29.25)
pions_size2 = pions_size



jeu = chess.Game(None,None)

def render():
  global jeu, count, partie, timer
  canvas.clear()
  
  canvas.draw_image(echiquier, (175,171),(350,342),(250,250),(500,500),0)
 
  board = str(jeu.board).split()
 
  j = 0
  for ligne in board:
    i = 0
    for c in ligne:
      i += 1
      if c<> ".":
        x = ML+i*(W-2*ML)/8 - 25
        y = MT+j*(W-2*MT)/8 + 12
        p = pieces[c]
        
        canvas.draw_image(pions,
                         (
						 pions_center[0]+p[1]*pions_size[0],
                         pions_center[1]+p[0]*pions_size[1]),
                         pions_size,
                         (x,y),
                         pions_size2,
                         0
        )
    j += 1  
  
  
  
  if count < len(partie):
    canvas.draw_text(partie[count],(20,20),24,'Blue')
    jeu.move(partie[count])
    jeu.advance()
  
  count += 1
  
canvas.clear_timers()
count = 0
timer = canvas.create_timer(2000, render)
timer.start()
