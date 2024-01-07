import customtkinter as ctk
from random import choice, shuffle

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Rock Paper Scissors")
        self.geometry("500x400")
        self.resizable(False, False)
        self.iconbitmap("icon.ico")
        self.rowconfigure((0, 1), weight = 1, uniform = "a")
        self.columnconfigure(0, weight = 1, uniform = "a")

        #variables
        self.player_move = ctk.StringVar(value = None)
        self.moves_list = ["Rock", "Paper", "Scissors"]
        self.computer_move = choice(self.moves_list)
        self.winner = ctk.StringVar(value = None)
        self.comp_move = ctk.StringVar(value = "Press Any Button To Start...")

        #player buttons
        PlayerButtons(self, self.player_move, self.computer_move, self.moves_list, self.winner, self.comp_move)

        #text
        TextOutput(self, self.winner, self.comp_move)

        self.mainloop()

class PlayerButtons(ctk.CTkFrame):
    def __init__(self, parent, player_move, computer_move, moves_list, winner, comp_move):
        self.player_move = player_move
        self.computer_move = computer_move
        self.moves_list = moves_list
        self.winner = winner
        self.comp_move = comp_move

        super().__init__(parent, fg_color = "#fff44f", corner_radius = 0)
        self.grid(row = 1 ,column = 0, sticky = "news")

        self.columnconfigure((0, 1, 2), weight = 1, uniform = "a")
        self.rowconfigure(0, weight = 1, uniform = "a")

        #buttons
        font = ctk.CTkFont("Fira Code", 25, "bold")
        self.rock_button = ctk.CTkButton(self, text = "Rock", border_width = 3,
        border_color = "black", command = lambda: self.check_move(self.rock_button),
        font = font)
        self.rock_button.grid(column = 0, row = 0, sticky = "news", rowspan = 1,
                               padx = 10, pady = 10)

        self.paper_button = ctk.CTkButton(self, text = "Paper", border_width = 3,
        border_color = "black", command = lambda: self.check_move(self.paper_button),
        font = font)
        self.paper_button.grid(column = 1, row = 0, sticky = "news", rowspan = 1,
                               padx = 10, pady = 10)

        self.scissors_button = ctk.CTkButton(self, text = "Scissors", border_width = 3,
        border_color = "black", command = lambda: self.check_move(self.scissors_button),
        font = font)
        self.scissors_button.grid(column = 2, row = 0, sticky = "news", rowspan = 1,
                               padx = 10, pady = 10)

    def check_move(self, button):
        self.player_move.set(button.cget("text"))
        shuffle(self.moves_list)
        self.computer_move = choice(self.moves_list)
        if self.player_move.get() == self.computer_move:
            self.winner.set("The Game Is A Tie :)")
            self.comp_move.set("Comp Played The Same Move ")

        else:
            if self.player_move.get() == "Rock" and self.computer_move == "Paper":
                self.winner.set("Comp Wins!")
                self.comp_move.set("Comp Played Paper")
            elif self.player_move.get() == "Rock" and self.computer_move == "Scissors":
                self.winner.set("You Win! :D")
                self.comp_move.set("Comp Played Scissors")
            elif self.player_move.get() == "Paper" and self.computer_move == "Rock":
                self.winner.set("You Win! :D")
                self.comp_move.set("Comp Played Rock")
            elif self.player_move.get() == "Paper" and self.computer_move == "Scissors":
                self.winner.set("Comp Wins!")
                self.comp_move.set("Comp Played Scissors")
            elif self.player_move.get() == "Scissors" and self.computer_move == "Rock":
                self.winner.set("Comp Wins!")
                self.comp_move.set("Comp Played Rock")
            elif self.player_move.get() == "Scissors" and self.computer_move == "Paper":
                self.winner.set("You Win! :D")
                self.comp_move.set("Comp Played Paper")

class TextOutput(ctk.CTkFrame):
    def __init__(self, parent, winner, comp_move):
        super().__init__(parent, fg_color = "#fff44f", corner_radius = 0)
        self.grid(row = 0, column = 0, sticky = "news")

        font = ctk.CTkFont("Fira Code", 40, "bold")
        main_Text = ctk.CTkLabel(self, text = " ", textvariable = winner, font = font, text_color = "black")
        main_Text.place(relx = 0.5, rely = 0.5, anchor = "center")

        font2 = ctk.CTkFont("Fira Code", 15, "bold")
        move_text = ctk.CTkLabel(self, text = " ", textvariable = comp_move, font = font2, text_color = "black")
        move_text.place(relx = 0.5, rely = 0.8, anchor = "center")

if __name__ == '__main__':
    app = App()
    print(__name__)