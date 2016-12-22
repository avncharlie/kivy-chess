from kivy.app import App

from kivy.clock import Clock

from kivy.core.window import Window

from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

from kivy.properties import NumericProperty

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
    pass

class ChessboardApp(App):
    def test(self, *args):
        print("YEAAH BOI")
    def build(self):
        game = ChessGame()

        for child in game.children:
                if type(child) == ChessboardCentered:
                    board = child.children[0]

        for num in range(64):
            button = ChessCell(id=str(num))
            board.add_widget(button)
        
        return game

if __name__ == '__main__':
    ChessboardApp().run()
