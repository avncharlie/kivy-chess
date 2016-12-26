from kivy.app import App
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

from kivy.properties import NumericProperty

import chess
import chess.uci

import os

class Chessboard(GridLayout):
    def gen_image_dict(self, *args, image_dir='cp-images'):
        if image_dir[-1] != '/':
            image_dir += '/'
        d = {'p': image_dir + 'BlackPawn.png',
                'r': image_dir + 'BlackRook.png',
                'n': image_dir + 'BlackKnight.png',
                'b': image_dir + 'BlackBishop.png',
                'q': image_dir + 'BlackQueen.png',
                'k': image_dir + 'BlackKing.png',
                'P': image_dir + 'WhitePawn.png',
                'R': image_dir + 'WhiteRook.png',
                'N': image_dir + 'WhiteKnight.png',
                'B': image_dir + 'WhiteBishop.png',
                'Q': image_dir + 'WhiteQueen.png',
                'K': image_dir + 'WhiteKing.png',
            }
        return d
        
    def update_positions(self, board, *args):
        # Can't call ids directly for some reason so ...
        # Dictionary mapping ids to children (Chess cells)
        ids = {child.id: child for child in  self.children}

        # Get the board positions from the fen
        b = str(board.fen).split(' ')[4].replace('/', '')[7:]
        # Replace empty spaces with dots
        for num in range(1, 10):
            b = b.replace(str(num), '.'*num)

        # Generate dictionary that maps pieces to images
        image_dict = self.gen_image_dict()

        # Map Chess cell ids to board positions
        for x in zip(range(64), list(b)):
            if x[1] != '.':
                image = image_dict[x[1]]
            else:
                image = 'cp-images/transparency.png'
            ids[str(x[0])].children[0].source = image
            
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
    def draw_board(self, *args):
        for child in self.children:
            if type(child) == ChessboardCentered:
                c_board = child.children[0]
    
        for num in range(64):
            button = ChessCell(id=str(num))
            c_board.add_widget(button)

    def update_board(self, board, *args):
        self.ids.board.update_positions(board)
    
    def chesscell_clicked(self, id, *args):
        print(id)


class ChessboardApp(App):
    def build(self):
        board = chess.Board()
        engine = chess.uci.popen_engine("stockfish")

        game = ChessGame()
        game.draw_board()
        game.update_board(board)
        
        return game

if __name__ == '__main__':
   ChessboardApp().run()
