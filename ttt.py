import sys
import copy

minmax=0
alpha_beta=0

# ttt.py
#
# Implementation of regular min max and alpha beta puring algorithm
# to find optimum move against human player
#
# Usage: Run the file and provide input as reqested


######################################
# Prints the current status of game
######################################
def printboard(board):
	"""0 is O, 1 is X, 2 is blank"""
	print " --- --- ---"
	for i in range(3):
		print "|",
		for j in range(3):
			if(board[i][j]==2):
				print "  |",
			elif(board[i][j]==1):
				print "X |",
			else:
				print "O |",
		print "\n --- --- ---"

######################################
# checks if board is full or someone won
######################################
def terminalTest(board):
	"""checks diagonally,vertically,and horizontally if someone has won
	or if board is full
	if user won returns -1
	if computer won returns 1
	if board is full retrun 0
	else returns null"""
	for i in range(3):
		#checks every row
		if(board[0][i]!=2 and board[0][i]==board[1][i] and board[0][i]==board[2][i]):
			if(board[0][i]==1):
				return -1
			else:
				return 1
		#checks every column
		if(board[i][0]!=2 and board[i][0]==board[i][1] and board[i][0]==board[i][2]):
			if(board[i][0]==1):
				return -1
			else:
				return 1
	#checks 1 diagonal
	if(board[0][2]!=2 and board[0][2]==board[1][1] and board[0][2]==board[2][0]):
		if(board[0][2]==1):
			return -1
		else:
			return 1
		   
	#checks other diagonal
	if(board[0][0]!=2 and board[0][0]==board[1][1] and board[0][0]==board[2][2]):
		if(board[0][0]==1):
			return -1
		else:
			return 1
	
	#if board has blank space left return nothing
	for i in range(3):
		for j in range(3):
			if(board[i][j]==2):
				return
	#no blank space means tie
	return 0

######################################
# minmax algo
######################################
def minimax_decision(state):
	v=-2
	for i in range(3):
		for j in range(3):
			if(state[i][j]==2):
				newstate=copy.deepcopy(state)
				newstate[i][j]=0
				value=min_value(newstate)
				if v<value:
					v=value
					toreturnstate=copy.deepcopy(newstate)
	return toreturnstate

######################################
# max function
######################################
def max_value(state):
	global minmax
	minmax+=1
	if terminalTest(state):
		return terminalTest(state)
	if terminalTest(state)==0:
		return 0
	v=-2
	for i in range(3):
		for j in range(3):
			if(state[i][j]==2):
				newstate=copy.deepcopy(state)
				newstate[i][j]=0
				v=max(v,min_value(newstate))
	return v
	
######################################
# min function
######################################
def min_value(state):
	global minmax
	minmax+=1
	if terminalTest(state):
		return terminalTest(state)
	if terminalTest(state)==0:
		return 0
	v=2
	for i in range(3):
		for j in range(3):
			if(state[i][j]==2):
				newstate=copy.deepcopy(state)
				newstate[i][j]=1
				v=min(v,max_value(newstate))
	return v

######################################
# alpha beta algo
######################################
def alpha_beta_search(state):
	v=-2
	for i in range(3):
		for j in range(3):
			if(state[i][j]==2):
				newstate=copy.deepcopy(state)
				newstate[i][j]=0
				value=abmin(newstate,-2,2)
				if v<value:
					v=value
					toreturnstate=copy.deepcopy(newstate)
	return toreturnstate

######################################
# max function of alpha beta
######################################
def abmax(state,alpha,beta):
	global alpha_beta
	alpha_beta+=1
	if terminalTest(state):
		return terminalTest(state)
	if terminalTest(state)==0:
		return 0
	v=-2
	for i in range(3):
		for j in range(3):
			if(state[i][j]==2):
				newstate=copy.deepcopy(state)
				newstate[i][j]=0
				v=max(v,abmin(newstate,alpha,beta))
				if v>=beta:
					return v
				alpha=max(alpha,v)
	return v

######################################
# min function of alpha beta
######################################
def abmin(state,alpha,beta):
	global alpha_beta
	alpha_beta+=1
	if terminalTest(state):
		return terminalTest(state)
	if terminalTest(state)==0:
		return 0
	v=2
	for i in range(3):
		for j in range(3):
			if(state[i][j]==2):
				newstate=copy.deepcopy(state)
				newstate[i][j]=1
				v=min(v,abmax(newstate,alpha,beta))
				if v<=alpha:
					return v
				beta=min(beta,v)
	return v	

######################################
# finds next move of computer player
######################################
def findnext(board):
	global minmax
	minmax=0
	global alpha_beta
	alpha_beta=0
	nextstep=copy.deepcopy(minimax_decision(board))
	board=copy.deepcopy(alpha_beta_search(board))
	print "Total search node generated for regular min max: \t",
	print minmax
	print "Total search node generated for alpha beta pruning: \t",
	print alpha_beta
	printboard(board)
	#printboard(nextstep)
	return board
#########################
# Main program
#########################	
def main():
	board = [[2 for x in xrange(3)] for x in xrange(3)] 
	printboard(board)
	userschance = True
	while True:
		if userschance:
			i=input("Enter row number\n")
			j=input("Enter column number\n")
			board[i-1][j-1]=1
			printboard(board)
		else:
			board=copy.deepcopy(findnext(board))
		userschance=not userschance
		if terminalTest(board) or terminalTest(board)==0:
			break
	if terminalTest(board)==0:
		print "Draw"
	if terminalTest(board)==1:
		print "You lost!!!!!!!!"
	if terminalTest(board)==-1:
		print "You Won!!!!!!!!"
# Execute the main program.
main()
