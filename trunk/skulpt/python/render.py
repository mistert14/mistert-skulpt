import document
import canvas

canvas.clear()

count = 0
a = 250
b = 250
points = []
lining = True

def debug(info):
  console = document.getElementById("output")
  console.innerHTML = ""
  console.innerHTML = str(info)
  
def get_mouse():
  mouse = document.getElementById("mouse").innerHTML
  if mouse == 'mouse ...':
    return []
  else:
    return mouse.split(':')
def get_kb():
  kb = document.getElementById("editor").value
  debug(kb)
  if kb == '':
    return ""
  else:
    return kb
 
def render():
  global count, timer,a,b, points, lining
  canvas.clear()
  
  c = get_kb()
 
  if c == '37':
    #canvas.draw_text(250,250,"<-")
    lining = False
  if c == '39':
    #canvas.draw_text(250,250,"<-")
    lining = True
    
  ms = get_mouse()
  if len(ms) > 0:
    if not (ms in points):
      points.append(ms)
      count += 1
    for p in points:
      canvas.draw_circle(p[0],p[1],2)
  if lining:
    for i in range(len(points)-1):
      canvas.draw_line(points[i+1][0],points[i+1][1],
                       points[i][0],points[i][1])
                         
        
  
  #debug(points)
  #if count == 100:
    #timer.stop()
  
timer = canvas.create_timer(10, render)
timer.start()
  