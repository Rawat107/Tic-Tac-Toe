import math
import random

class Player():
  def __init__(self, letter):
    #letter is x or o
    self.letter = letter

  # we want every one to get their move in a given game
  def get_move(self, game):
    pass

class RandomCpu(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square

class HumanPlayer(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    valid_square = False
    val = None
    while not valid_square:
      square = input(self.letter + '\'s turn. Input moves (0-8): ')
      # we are going to check if its a correct value by trying to cast
      # It into an integers, if not an integer, then we say its invalid
      # If that spot in not available we will also say its invalid.
      try:
        val = int(square)  
        if val not in game.available_moves():
          raise ValueError
        valid_square = True  #If everythinf successfull.
      except ValueError:
        print('Invalid Square')

    return val

class SmartCpu(Player):
  def __init__(self, letter):
    super().__init__(letter)

  def get_move(self, game):
    if len(game.available_moves()) == 9:
      square = random.choice(game.available_moves()) #randomly choose one
    else:
      #get the square based off the minimax algorithm
      square = self.minimax(game, self.letter)['position']
    return square

  def minimax(self, ss, player): # ss because at every single iteration of minimax we pass in a representation of screenshot of that state.
    
    max_player = self.letter  #yourself!!
    
    other_player = 'O' if player == 'X' else 'X' #the other player ... whatever the letter is not

    #first we want to check if the previous move is a winner
    #This is our base case
    if ss.current_winner == other_player:
      #we should return position AND score becuase we need to keep track of the score
      # for minimax to work
      return {'position': None, 'score': 1 * (ss.num_empty_square() + 1) if other_player == max_player else -1 * (ss.num_empty_square() + 1)} #
      
    elif not ss.empty_squares(): #no empty square
      return {'position': None, 'score': 0}

    if player == max_player:
      best = {'position': None, 'score': -math.inf} #each score should maximize (the largest)
    else:
      best = {'position': None, 'score': math.inf} # each score should minimize

    for possible_move in ss.available_moves():
      #step1: make a move, try that spot
      ss.make_moves(possible_move, player)
      #step2: recurse using minimize to simulate a game after making that move
      sim_score = self.minimax(ss, other_player)
      #step3: undo the move
      ss.board[possible_move] = ' '
      ss.current_winner = None
      sim_score['position'] = possible_move #otherwise this will get messed up from the recusrsion part
      
      #step4: update the dictionaries if necessary
      if player == max_player: # we are trying to maximize max player
        if sim_score['score'] > best['score']:
          best = sim_score # replace the best
          
      else: # but minimize the other player 
        if sim_score['score'] < best['score']:
          best = sim_score # replace the best

    return best
    
    
        
