from Player import HumanPlayer, RandomCpu, SmartCpu
import time
class TicTacToe:
  def __init__(self):
    self.board = [' ' for _ in range(9)] # we will use a single list to represent 3*3 board
    self.current_winner = None

  def print_board(self):
    # this is just getting rows
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')

  @staticmethod
  def printboard_num():
    # 0 | 1 | 2 etc (tell us what number correspond to what box)
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')

  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == ' ']
    # move = []
    # for i, spot in enumerate(self.board):
    #   #[x, x, o] --> (0, x), (1, x), (2, O)
    #   if spot == ' ':
    #     move.append(i)

  def empty_squares(self):
    return ' ' in self.board

  def num_empty_square(self):
    return self.board.count(' ')

  def make_moves(self, square, letter):
    # If valid move, then make the move (assign sqaure to letter)
    # then return true. if invalid , return false
    if self.board[square] == ' ':
      self.board[square] = letter 
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False

  def winner(self, square, letter):
    # winner if 3 in a row anywherem we have to check all of these!
    # first let's check the row
    row_ind = square//3
    row = self.board[row_ind*3 : (row_ind + 1) * 3]
    if all([spot == letter for spot in row]):
      return True

    # check column
    col_ind = square % 3
    column = [self.board[col_ind+i*3] for i in range(3)]
    if all([spot == letter for spot in column]):
      return True

    # check diagonals 
    # but only if the square is an even number (0, 2, 4, 6)
    # these are the only moves possible to win a diagonal
    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diag  
      if all([spot == letter for spot in diagonal1]):
        return True
      diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left       
      if all([spot == letter for spot in diagonal2]):
        return True

    return False 
      
    
def play(game, x_player, o_player, print_game=True):
  # return the winner of the game(the letter) or None for a tie
  if print_game:
    game.printboard_num()

  letter = 'X' # Starting letter
  # iterate while game still have some empty sqaure
  # (we don't have to worry about winner because we'll just return that
  # which break out of loop)
  while game.empty_squares():
    # to get mmove from appropriate player
    if letter == 'O':
      square = o_player.get_move(game)
    else:
      square = x_player.get_move(game)

    # ler' define a functon to make a mvove
    if game.make_moves(square, letter):
      if print_game:
        print(letter + f' make a move to square {square}')
        game.print_board()
        print('') # just empty line

      if game.current_winner:
        if print_game:
          print(letter + ' Win!')
        return letter
      # after we made our move we need alternate letters
      letter = 'O' if letter == 'X' else 'X' # switches player
      # if letter == 'X':
      #   letter = 'O'
      # else:
      #   letter = 'X'
    time.sleep(0.9)
    
  if print_game:
    print('It\'s a tie!')
      
if __name__ == '__main__':
  
  o_player = HumanPlayer('O')
  x_player = SmartCpu('X')
  t = TicTacToe()
  play(t, x_player, o_player, print_game=True)
