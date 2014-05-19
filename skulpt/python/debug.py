#default
import toto
toto.clear()
toto.grid()

url = "http://mrt2.no-ip.org/skulpt/assets/cards.jfitz.png"

card_size = (73, 98)
card_center = (36.5, 49)

card_back_size = (71, 96)
card_back_center = (35.5, 48)

toto.draw_image(url, card_center, card_size, card_center, card_size )