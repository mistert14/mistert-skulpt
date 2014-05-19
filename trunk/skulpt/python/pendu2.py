#pendu2
# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import urllib2
url = "http://mrt2.no-ip.org/skulpt/donne_mot.php"

msg =""
mot = ""
to_find = []
errors = 1
end_game = True
# Handler for mouse click
def init():
    global mot, to_find, url
    t = urllib2.urlopen(url)
    mots =  t.readlines()
    mots.pop(-1)
    mot = ''.join(str(x) for x in mots) 
    to_find = []
    for c in mot:
        if not(c in to_find):
            to_find.append(c)
    end_game = False



def mouse_handler(position):
    global mot, to_find, errors, msg, end_game
    if position[1] <= 18:
        ch =  chr(65+(position[0] // 18))
        if ch in ['A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z','-']:
            if (ch in mot) and (ch in to_find):
                to_find.remove(ch)
                if len(to_find) == 0:
                    end_game = True
                    msg = "YOU WIN!"
            else:
              if (ch in mot):
                return
              else:
                errors += 1
                if errors >=12:
                    end_game = True
                    msg = "YOU LOOSE!"
                    
                
                
def draw(canvas):
    global errors, mot, to_find, msg, end_game
    print to_find
    w = 18
    
    for i in range(26):
        canvas.draw_polygon([[i*w, 0], [(i+1)*w, 0], [(i+1)*w, w], [i*w, w]], 1, 'Yellow', 'Orange')
        canvas.draw_text(chr(65+i), (i*w+3,16),20,'Blue')
    
    n = len(mot)
    p = 1000.0 / ( 3*n + 1 )
    e = p / 2
    
    
    for i in range(len(mot)):
        if mot[i] in to_find:
            canvas.draw_line(
                             ((i+1)*e+(i)*p,60),
                            ((i+1)*(e+p),60),
                            1,
                            'Blue')
        else:
            a = (i+1)*e+(i)*p
            b = (i+1)*(e+p)
            canvas.draw_text(mot[i],  ((a+b)/2 , 50), 28,'Blue')
    
    
    if (errors > 1):
        canvas.draw_line((100,400),(200,400),1,'White')
    if (errors >= 2):
        canvas.draw_line((100,400),(200,400),1,'White')  
    if (errors >= 3):
        canvas.draw_line((150,400),(150,150),1,'White')
    if (errors >= 4):
        canvas.draw_line((150,150),(300,150),1,'White')
    if (errors >= 5):
        canvas.draw_line((225,150),(150,230),1,'White')
    if (errors >= 6):
        canvas.draw_line((300,150),(300,180),1,'White')
    if (errors >= 7):
        canvas.draw_circle((300,200),20,1,'White')
    if (errors >= 8):
        canvas.draw_line((300,220),(300,300),1,'White')
    if (errors >= 9):
        canvas.draw_line((300,300),(330,360),1,'White')
    if (errors >= 10):
        canvas.draw_line((300,300),(270,360),1,'White')
    if (errors >= 11):
        canvas.draw_line((300,240),(330,300),1,'White')
    if (errors >= 12):
        canvas.draw_line((300,240),(270,300),1,'White')

    if (end_game):
         canvas.draw_text(msg,  (200, 250), 28,'Red')
    
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw)
# Start the frame animation
frame.start()
init()