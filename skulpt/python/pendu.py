#pendu
#pendu
import canvas
import urllib2
url = "http://mrt2.no-ip.org/skulpt/donne_mot.php"
t = urllib2.urlopen(url)
mots =  t.readlines()
mots.pop(-1)
mot = ''.join(str(x) for x in mots) 


errors = 1

canvas.clear()

def dessine(mot,p,e):
  global to_find
  for i in range(len(mot)):
    if mot[i] in to_find:
      canvas.draw_line((i+1)*e+(i)*p,60,(i+1)*(e+p),60)
    else:
      a = (i+1)*e+(i)*p
      b = (i+1)*(e+p)
      canvas.draw_text( (a+b)/2 , 50 , mot[i])

def process():
  global errors
  
  if (errors >= 1):
    canvas.draw_line(100,400,200,400)
  if (errors >= 2):
    canvas.draw_line(100,400,200,400)  
  if (errors >= 3):
    canvas.draw_line(150,400,150,150)
  if (errors >= 4):
    canvas.draw_line(150,150,300,150)
  if (errors >= 5):
    canvas.draw_line(225,150,150,230)
  if (errors >= 6):
    canvas.draw_line(300,150,300,180)
  if (errors >= 7):
    canvas.draw_circle(300,200,20)
  if (errors >= 8):
    canvas.draw_line(300,220,300,300)
  if (errors >= 9):
    canvas.draw_line(300,300,330,360)
  if (errors >= 10):
    canvas.draw_line(300,300,270,360)
  if (errors >= 11):
    canvas.draw_line(300,240,330,300)
  if (errors >= 12):
    canvas.draw_line(300,240,270,300)



n = len(mot)
p = 1000.0 / ( 3*n + 1 )
e = p / 2

lettres = []
to_find = []

for c in mot:
  if not(c in to_find):
    to_find.append(c)

while (len(to_find)>0) and (errors<12):
  dessine(mot,p,e)
  lettre = input('Donne une lettre: ')
  ch = lettre[0].upper()
  if ch in ['A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z','-']:
    if not(ch in lettres):
      lettres.append(ch)
    if ch in mot:
      to_find.remove(ch)
    else:
      errors += 1
      process()
    
    dessine(mot,p,e)
 
if (errors >= 12):
  canvas.draw_text( 200 , 250 , "YOU LOOSE :(")
else:
  canvas.draw_text( 200 , 250 , "YOU WIN :)")
errors = 0  