from tkinter import *
from tkinter import ttk


class Tetris:
    def __init__(self, w, h):
        self.app = Tk()
        self.app.title("Tetris")
        self.style = ttk.Style()
        self.style.configure(
            "BW.TLabel", foreground="black", background="white")
        self.ws = self.app.winfo_screenwidth()
        self.hs = self.app.winfo_screenheight()
        self.w = w
        self.h = h
        self.x = int(self.ws/2-self.w/2)
        self.y = int(self.hs/2-self.h/2)
        self.app.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")

    def game_board(self, x=10, y=10):
        self.game_board = Canvas(self.app)
        self.game_board.place(x=x, y=y)
        self.game_board.configure(
            width=self.w-x*2-4, height=self.h-y*2-4, bg="#38b48b", highlightthickness=2)

    def open(self):
        self.app.mainloop()


class Block:
    shapeNo = [[0, 0], [0, 0], [0, 0], [0, 0]]
    shapeZ = [[0, 1], [0, 0], [1, 0], [1, 1]]
    shapeS = [[0, 1], [0, 0], [1, 0], [1, 1]]
    shapeLine = [[0, 1], [0, 0], [0, 1], [0, 2]]
    shapeT = [[1, 0], [0, 0], [1, 0], [0, 1]]

t = Tetris(500, 700)
t.game_board()
t.open()
