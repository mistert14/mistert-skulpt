#cards
import canvas
import games
import document

play = document.getElementById('chk').checked
if play == 'True':
  music = canvas.load_sound("http://mrt2.no-ip.org/skulpt/assets/Epoq-Lepidoptera.ogg")
  music.play()

canvas.clear()


image = canvas.load_image("http://mrt2.no-ip.org/skulpt/assets/cards.jfitz.png")

card_size = (73, 98)
card_center = (0, 0)

desk = games.Deck()

def tick():
  global desk, image, card_size, card_center
  for i in range(6):
    carte = desk.give_card()
    canvas.draw_image(image, (card_size[0]*carte[0],card_size[1]*carte[1]), card_size, (74*i,0), card_size )

timer = canvas.create_timer(1000, tick)
timer.start()