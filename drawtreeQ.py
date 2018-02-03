import linkedliststackqueue, math

def drawtree():
	class branch:
		def __init__(self,length,width,heading,x,y):
			self.length = length
			self.width = width
			self.heading = heading
			self.x = x
			self.y = y
		def draw(self):
			print('penup')
			print('goto, ' + str(self.x) + ', ' + str(self.y) + ', 1, white')
			print('pendown')
			angle = math.radians(self.heading)
			newx = self.x + math.cos(angle) * self.length
			newy = self.y + math.sin(angle) * self.length
			print('goto, ' + str(newx) + ', ' + str(newy) + ', ' + str(self.width) \
                                + ', black')
			self.x = newx
			self.y = newy

	queue = linkedliststackqueue.Queue()
	queue.enqueue(branch(200,20,90,0,-200))
	while queue.isEmpty() != True:
		b = queue.dequeue()
		b.draw()
		if b.length*0.6 >= 10:
			queue.enqueue(branch(b.length*0.6, b.width*0.6, b.heading-45, b.x,b.y)) 
			queue.enqueue(branch(b.length*0.6, b.width*0.6, b.heading+45, b.x,b.y)) 

def main():
	drawtree()    
    

if __name__ == "__main__":
	main()
