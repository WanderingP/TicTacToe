"""Tic Tac Toe"""

import random 


in_game = False
quit = False
players = [0,'X','O']
board = [' ']*10

#The game grid display

def grid(board):
	'''Parameter should be a list that contains 10 items. Prints a 3X3 grid.'''

	print('	  |	  |	  ')
	print('   ' + board[1] + '  |  ' + board[2] + '   |  ' + board[3])
	print('	  |	  |	  ')
	print('-----------------')
	print('	  |	  |	')
	print('   ' + board[4] + '  |  ' + board[5] + '   |  ' + board[6])
	print('	  |	  |	')
	print('-----------------')
	print('	  |	  |	  ')
	print('   ' + board[7] + '  |  ' + board[8] + '   |  ' + board[9])
	print('	  |	  |	 ')


def full_board(board):
	'''Parameter should be a list of more than 2 items. Returns True if no whitespaces in list.'''
	return ' ' not in board[1:]

	
def check_win(board,x):
	'''Parameters: Board is a list that contains 10 items. X is a character that could be located in a list. Checks wether 1 of 8 permutations is True.'''

	return board[1] == x and board[2] == x and board[3] == x or board[4] == x and board[5] == x and board[6] == x or board[7] == x and board[8] == x and board[9] == x or board[1] == x and board[4] == x and board[7] == x or board[2] == x and board[5] == x and board[8] == x or board[3] == x and board[6] == x and board[9] == x or board[1] == x and board[5] == x and board[9] == x or board[7] == x and board[5] == x and board[3] == x					

				
def marker(board, player, position):
	'''Parameters: Board is a list. Player is the character. Position is the place within the list in which player shall be placed.'''
	board[position] = player
	  


def reset():
	'''No parameters. Fuction is added to an object. Creates a list'''

	b = [' '] * 10

	return b

	

def is_valid(board,a):

	return board[a] == ' '

			
def player_select():
		return random.choice((-1,1))


def space_check(board,position):
	return board[position] == ' '



while quit == False:

	print('Welcome to two player Tic Tac Toe.')

	cue = (input('Type 1 to play a game, 2 for the instructions or 5 to quit: '))

	cue = int(cue)

		

	if cue == 1:

		in_game = True

	elif cue == 2:

		print('The aim of the game is to place three of your characters in a row. You will play as either X or O. You can win by creating a horizontal, vertical or diagonal line.' )

		print('Here is your game grid.')

		grid(board)

		board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

		print("Each cell has a numeric value that you will use to fill in your X's and O's. The grid below shows those values.")

		grid(board)

		print('You must take turns to enter a number. The corresponding place on the grid will be marked.')

		board = reset()

		cue = str(input('If you would like to start a game press 1 or press 5 to quit: '))

		if cue == 5:

			quit == True

		else:

			in_game = True

	else:

		quit = True




	while in_game == True:
		board = reset()
		cue = int(input('Are you ready to play? Press 1 to continue or 5 to quit: '))
		if cue == 5:
			in_game = False
		else:
			toggle = player_select()
			player = players[toggle]
			print(player, 'will start.')
			game_on = True

			while game_on == True:
				grid(board)
				position = int(input('Player %s, please choose a position between 1-9: '%(player)))
				if board[position] == ' ':
					marker(board,player,position)
				else:
					print('That was not a valid input')
					

				if check_win(board,player) == True:
					grid(board)
					print(player, 'has won the game!')
					game_on = False

				else:
					if full_board(board) == True:
						grid(board)
						print('Its a draw!')
						game_on = False
						break
					else:
						toggle *= -1
						player = players[toggle]
					
				  
