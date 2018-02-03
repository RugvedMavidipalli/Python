import turtle, linkedliststackqueue

def drawtree(t):
	class branch:
		def __init__(self,length,width,heading,x,y):
			self.length = length
			self.width = width
			self.heading = heading
			self.x = x
			self.y = y
		def draw(self):
			t.penup()
			t.goto(self.x,self.y)
			t.pendown()
			t.seth(self.heading)
			t.width(self.width)
			t.forward(self.length)

	stack = linkedliststackqueue.Stack()
	
	stack.push(branch(200,20,90,0,-200))
	while stack.isEmpty() != True:
		b = stack.pop()
		b.draw()
		tx = t.xcor()
		ty = t.ycor()
		if b.length*0.6 >= 10:
			stack.push(branch(b.length*0.6, b.width*0.6, b.heading-45, tx,ty)) 
			stack.push(branch(b.length*0.6, b.width*0.6, b.heading+45, tx,ty)) 

def main():
	t = turtle.Turtle()
	screen = t.getscreen()
	t.speed(100)
	drawtree(t)    
	t.ht()
	screen.exitonclick()
    

if __name__ == "__main__":
	main()
