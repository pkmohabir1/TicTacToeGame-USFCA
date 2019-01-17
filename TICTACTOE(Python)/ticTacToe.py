import random
import turtle
import time

wn = turtle.Screen()


class DrawGrid: 
		def __init__(self):
			self.grid = turtle.Turtle()
			self.grid.pensize(15)
			self.grid.pu()#pen up
			self.grid.sety(-300)
			self.grid.setx(-100)
			self.grid.hideturtle()
		
		def Grid(self):
		
			self.grid.pd()#pen down
			self.grid.left(90)
			self.grid.forward(600)
			
			self.grid.pu()#pen up
			self.grid.right(90)
			self.grid.forward(200)
			
			self.grid.pd()#pen down
			self.grid.right(90)
			self.grid.forward(600)
			self.grid.left(90)
			
			self.grid.pu()#pen up
			self.grid.forward(200)
			self.grid.left(90)
			self.grid.forward(200)
			
			self.grid.pd()#pen down
			self.grid.left(90)
			self.grid.forward(600)
			self.grid.left(180)
			self.grid.forward(600)
			self.grid.left(90)
			
			self.grid.pu()#pen up
			self.grid.forward(200)
			self.grid.left(90)
			
			self.grid.pd()#pen down
			self.grid.forward(600)
			
			self.grid.hideturtle()
			
			
#______________________________________________________________
			
class DrawX:
		def __init__(self): 
			self.x = turtle.Turtle() 
			self.x.color("blue")
			self.x.pensize(8)
			self.x.hideturtle()
			
		def Xchar(self, index):
			n = 150
			
			self.x.pu()
			
			if index == 0: 
				self.x.sety(166.6)
				self.x.setx(-200)
			elif index == 1:
				self.x.sety(166.6)
				self.x.setx(0)
			elif index == 2:
				self.x.sety(166.6)
				self.x.setx(200)
			elif index == 3:
				self.x.sety(-33.4)
				self.x.setx(-200)
			elif index == 4:
				self.x.sety(-33.4)
				self.x.setx(0)
			elif index == 5:
				self.x.sety(-33.4)
				self.x.setx(200)
			elif index == 6:
				self.x.sety(-233.4)
				self.x.setx(-200)
			elif index == 7: 
				self.x.sety(-233.4)
				self.x.setx(0)
			else: 
				self.x.sety(-233.4)
				self.x.setx(200)
			
			self.x.pu()#pen up
			
			self.x.forward(66.6)
			
			self.x.pd()#pen down
			self.x.left(135)
			self.x.forward(n)
			self.x.left(135)
			
			self.x.pu()#pen up
			self.x.forward(n/1.41)
			
			self.x.pd()#pen down
			self.x.left(135)
			self.x.forward(n)
			
			self.x.hideturtle()

#______________________________________________________________	
			
class DrawO: 
	def __init__(self): 
		self.o = turtle.Turtle()
		self.o.color("red")
		self.o.pensize(8)
		self.o.hideturtle()
		
	def Ochar(self, index): 
	
		self.o.speed(100000)
		n = 200
		
		self.o.pu()
		
		if index == 0: 
			self.o.sety(166.6)
			self.o.setx(-200)
		elif index == 1:
			self.o.sety(166.6)
			self.o.setx(0)
		elif index == 2:
			self.o.sety(166.6)
			self.o.setx(200)
		elif index == 3:
			self.o.sety(-33.4)
			self.o.setx(-200)
		elif index == 4:
			self.o.sety(-33.4)
			self.o.setx(0)
		elif index == 5:
			self.o.sety(-33.4)
			self.o.setx(200)
		elif index == 6:
			self.o.sety(-233.4)
			self.o.setx(-200)
		elif index == 7: 
			self.o.sety(-233.4)
			self.o.setx(0)
		else: 
			self.o.sety(-233.4)
			self.o.setx(200)
			
		self.o.pd()
		
		for i in range(n): 
			self.o.forward(2)
			self.o.left(180-((n-2)*180)/n)
			
		self.o.hideturtle()	
			

class WinningLine: 
	def __init__(self): 
		self.w = turtle.Turtle()
		self.w2 = turtle.Turtle()
		self.w3 = turtle.Turtle()
		self.w4 = turtle.Turtle()
		self.w5 = turtle.Turtle()
		self.w6 = turtle.Turtle()
		self.w7 = turtle.Turtle()
		self.w8 = turtle.Turtle()
# --------------------------------		
		self.w.color("green")
		self.w2.color("green")
		self.w3.color("green")
		self.w4.color("green")
		self.w5.color("green")
		self.w6.color("green")
		self.w7.color("green")
		self.w8.color("green")
# --------------------------------	
		self.w.pensize(7)
		self.w2.pensize(7)
		self.w3.pensize(7)
		self.w4.pensize(7)
		self.w5.pensize(7)
		self.w6.pensize(7)
		self.w7.pensize(7)
		self.w8.pensize(7)
# --------------------------------
		self.w.pu()
		self.w2.pu()
		self.w3.pu()
		self.w4.pu()
		self.w5.pu()
		self.w6.pu()
		self.w7.pu()
		self.w8.pu()
# --------------------------------	
		self.w.hideturtle()
		self.w2.hideturtle()
		self.w3.hideturtle()
		self.w4.hideturtle()
		self.w5.hideturtle()
		self.w6.hideturtle()
		self.w7.hideturtle()
		self.w8.hideturtle()
		
	def diagnolRight(self):#negative slope
		self.w.sety(300)
		self.w.setx(-300)
		self.w.pd()#pen down
		self.w.right(45)
		self.w.forward(848.53)

	def diagnolLeft(self):
		self.w2.sety(300)
		self.w2.setx(300)
		self.w2.pd()#pen down
		self.w2.left(225)
		self.w2.forward(848.53)
		
	def downLeft(self): 
		self.w3.sety(300)
		self.w3.setx(-200)
		self.w3.pd()
		self.w3.right(90)
		self.w3.forward(600)
	
	def downMiddle(self): 
		self.w4.sety(300)
		self.w4.setx(0)
		self.w4.pd()
		self.w4.right(90)
		self.w4.forward(600)
		
	def downRight(self): 
		self.w5.sety(300)
		self.w5.setx(200)
		self.w5.pd()
		self.w5.right(90)
		self.w5.forward(600)
		
	def horizontalUpper(self):
		self.w6.sety(200)
		self.w6.setx(300)
		self.w6.pd()
		self.w6.left(180)
		self.w6.forward(600)
		
	def horizontalMiddle(self): 
		self.w7.sety(0)
		self.w7.setx(300)
		self.w7.pd()
		self.w7.left(180)
		self.w7.forward(600)	
		
	def horizontalLower(self):
		self.w8.sety(-200)
		self.w8.setx(300)
		self.w8.pd()
		self.w8.left(180)
		self.w8.forward(600)
		

class Game:
	def __init__(self):
		self.player1=[]
		self.player2=[]
		self.board=['0','1','2','3','4','5','6','7','8']
		self.gameGrid = DrawGrid()
		self.gameGrid.Grid()
		
	
	def assignCharacters(self):
		x=random.randrange(2)
		
		if x==1:
			self.player2.append('X')
			self.player1.append('O')
			
		else:
			self.player1.append('X')
			self.player2.append('O')
			
	def whosFirst(self):
		x=random.randrange(2)
		
		if x==0:
			return self.player1
			
		else:
			return self.player2
	
	def firstMove(self,first):
		charX = DrawX()
		charO = DrawO()
		
		if self.player1 == 'X':
			if first==self.player1:
				moveIndex=input('player1 please make a move('+(''.join(self.player1))+'):')
				game.board[moveIndex]=''.join(first)
				charX.Xchar(moveIndex)
				game.printBoard()
			
			else:
				moveIndex=input('player2 please make a move('+(''.join(self.player2))+'):')
				game.board[moveIndex]=''.join(first)
				charO.Ochar(moveIndex)
				game.printBoard()
		else: 
			if first==self.player1:
				moveIndex=input('player1 please make a move('+(''.join(self.player1))+'):')
				game.board[moveIndex]=''.join(first)
				charO.Ochar(moveIndex)
				game.printBoard()
				
				
			
			else:
				moveIndex=input('player2 please make a move('+(''.join(self.player2))+'):')
				game.board[moveIndex]=''.join(first)
				charX.Xchar(moveIndex)
				game.printBoard()
			
	def otherMoves(self,whosTurn):
		charX = DrawX()
		charO = DrawO()
		
		if self.player1 == 'X':
			if whosTurn==self.player1:
				moveIndex=input('player1 please make a move('+(''.join(self.player1))+'):')
				self.board[moveIndex]=''.join(whosTurn)
				charX.Xchar(moveIndex)
				
			elif whosTurn==self.player2:
				moveIndex=input('player2 please make a move('+(''.join(self.player2))+'):')
				self.board[moveIndex]=''.join(whosTurn)
				charO.Ochar(moveIndex)
		else: 
			if whosTurn==self.player1:
				moveIndex=input('player1 please make a move('+(''.join(self.player1))+'):')
				self.board[moveIndex]=''.join(whosTurn)
				charO.Ochar(moveIndex)
				
			elif whosTurn==self.player2:
				moveIndex=input('player2 please make a move('+(''.join(self.player2))+'):')
				self.board[moveIndex]=''.join(whosTurn)
				charX.Xchar(moveIndex)	
			
	def winX(self):
		
		self.draw = WinningLine() 
		
		
		if self.board[0]==self.board[3]==self.board[6]=='X':
			self.draw.downLeft()
			return True
			
		elif self.board[2]==self.board[5]==self.board[8]=='X':
			self.draw.downRight()
			return True
			
		elif self.board[1]==self.board[4]==self.board[7]=='X':
			self.draw.downMiddle()
			return True
			
		elif self.board[0]==self.board[4]==self.board[8]=='X':
			self.draw.diagnolRight()
			return True
			
		elif self.board[2]==self.board[4]==self.board[6]=='X':
			self.draw.diagnolLeft()
			return True
			
		elif self.board[0]==self.board[1]==self.board[2]=='X':
			self.draw.horizontalUpper()
			return True
			
		elif self.board[3]==self.board[4]==self.board[5]=='X':
			self.draw.horizontalMiddle()
			return True
			
		elif self.board[6]==self.board[7]==self.board[8]=='X':
			self.draw.horizontalLower()
			return True
			
		else:
			return False
			
	def winO(self):
		self.draw = WinningLine() 
		
		if self.board[0]==self.board[3]==self.board[6]=='O':
			self.draw.downLeft()
			return True
			
		elif self.board[2]==self.board[5]==self.board[8]=='O':
			self.draw.downRight()
			return True
			
		elif self.board[1]==self.board[4]==self.board[7]=='O':
			self.draw.downMiddle()
			return True
			
		elif self.board[0]==self.board[4]==self.board[8]=='O':
			self.draw.diagnolRight()
			return True
			
		elif self.board[2]==self.board[4]==self.board[6]=='O':
			self.draw.diagnolLeft()
			return True
			
		elif self.board[0]==self.board[1]==self.board[2]=='O':
			self.draw.horizontalUpper()
			return True
			
		elif self.board[3]==self.board[4]==self.board[5]=='O':
			self.draw.horizontalMiddle()
			return True
			
		elif self.board[6]==self.board[7]==self.board[8]=='O':
			self.draw.horizontalLower()
			return True
			
		else:
			return False

	def printBoard(self):
		print self.board[0:3]
		print self.board[3:6]
		print self.board[6:9]
		print 'Please wait...'

	def playGame(self,whosFirst):
		if whosFirst==self.player1:
			whosTurn=self.player2
		else:
			whosTurn=self.player1
			
		winnerX=False
		winnerO=False
		turns=0
		
		while winnerX==False and winnerO==False and turns<9:	
			self.otherMoves(whosTurn)
			self.printBoard()
			winnerX=self.winX()
			winnerO=self.winO()
			
			if whosTurn==self.player1:
				whosTurn=self.player2
			elif whosTurn==self.player2:
				whosTurn=self.player1
				
			turns=turns+1
		
		if winnerX==False and winnerO==False:
			print 'Stalemate'
		elif whosTurn==self.player1:
			print 'Congrats player2'
		elif whosTurn==self.player2:
			print 'Congrats player1'
			
	def printInstructions(self):
		print 'INSTRUCTIONS:'
		time.sleep(2)
		print 'This game follows the same rules as the classic game of tic tac toe.'
		time.sleep(2)
		print 'However, in this verison each player makes moves by inputing the index that corresponds to the box they would like to move in.'
		time.sleep(2)
		print 'Please be careful when inputing your move. Please make sure...'
		time.sleep(2)
		print '(1) that you input a number to make a move in the box that is represented by that index and that the index is within the index range (0-8)'
		time.sleep(2)
		print '(2) that you do not move in a box that is already occupied by an "X" or a "O"'
		time.sleep(2)
		print 'Have fun!'
		time.sleep(2)
#________________________________________MAIN_____________________________________________
game=Game()
game.printInstructions()
whosTurn=[]
game.assignCharacters()
whosFirst=game.whosFirst()

print 'player1 character: ' + ''.join(game.player1)
print 'player2 character: ' + ''.join(game.player2)

if whosFirst==game.player1:
	print 'player1 goes first'
else:
	print 'player2 goes first'
	
game.printBoard()
game.firstMove(whosFirst)

game.playGame(whosFirst)

	
turtle.mainloop()
		







