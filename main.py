from kivy.app import App
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

from kivy.properties import NumericProperty

import chess
import chess.uci

board = chess.Board()
engine = chess.uci.popen_engine("stockfish")

class Chessboard(GridLayout):
    
    def on_size(self, *args):
        board_dimensions = sorted([self.width, self.height])[0]

        self.row_force_default = True
        self.col_force_default = True

        self.row_default_height = board_dimensions/self.rows
        self.col_default_width = board_dimensions/self.columns


class ChessboardCentered(BoxLayout):
    def on_size(self, *args):
        board_dimensions = sorted([self.width, self.height])[0]
        self.padding = [(self.width-board_dimensions)/2, 
            (self.height-board_dimensions)/2, 0, 0]

class ChessCell(Button):
    pass 

class ChessGame(BoxLayout):
    def gen_board_from_fen(self, *args):
       board_repr = []

       for row in str(board.fen).split(' ')[4].split('/'):
           row = row.replace("Board('", '')

           row_repr = ''
           for peice in row:
               if peice.isalpha():
                   row_repr += peice
               else:
                   row_repr += int(peice) * '.'
           board_repr.append(row_repr)

       return board_repr

class ChessboardApp(App):
    def build(self):
        game = ChessGame()

        for child in game.children:
                if type(child) == ChessboardCentered:
                    c_board = child.children[0]

        for num in range(64):
            button = ChessCell(id=str(num))
            c_board.add_widget(button)

        # you are making the engine move
        
        return game

if __name__ == '__main__':
   ChessboardApp().run()
