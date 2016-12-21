from kivy.app import App

from kivy.clock import Clock

from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

from kivy.properties import NumericProperty

class Chessboard(GridLayout):
    def on_size(self, *arg):
        board_dimensions = sorted([self.width, self.height])[0]

        self.row_force_default = True
        self.col_force_default = True

        self.row_default_height = board_dimensions/8
        self.col_default_width = board_dimensions


class ChessboardCentered(BoxLayout):
    def on_size(self, *args):
        board_dimensions = sorted([self.width, self.height])[0]
        self.padding = [(self.width-board_dimensions)/2, 
            (self.height-board_dimensions)/2, 0, 0]

class ChessGame(BoxLayout):
    pass

class ChessboardApp(App):
    def build(self):
        return ChessGame()

if __name__ == '__main__':
    ChessboardApp().run()
