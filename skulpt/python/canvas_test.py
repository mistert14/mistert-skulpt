#canvas_test
import canvas
canvas.clear_timers()
canvas.clear()
y = 0
angle = 0
def draw(cvs):
  global y, angle
  
  canvas.draw_line((0,0),(500,500),4,'Red')
  canvas.draw_image(img,(100,100),(200,200),(160,y),(40,40),angle)
  y = y +0.1
  angle = angle + 1
  
canvas.set_draw_handler(draw)
canvas.start('Yellow')
img = canvas.load_image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Maple_Leaf_%28from_roundel%29.png/220px-Maple_Leaf_%28from_roundel%29.png")
