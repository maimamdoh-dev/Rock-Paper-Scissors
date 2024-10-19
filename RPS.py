from tkinter import *
from PIL import Image, ImageTk # type: ignore
import random

game = Tk()
game.title("Rock Papper Scissor")
game.geometry("700x600")

rock = ImageTk.PhotoImage(Image.open("1.png"))
paper = ImageTk.PhotoImage(Image.open("2.png"))
scissors = ImageTk.PhotoImage(Image.open("3.png"))
choices = [rock, paper, scissors]


P_wins = 0
C_wins = 0

#Define the Play function
def play(player_choise):
    global choices, P_wins, C_wins

    
    player.config(image=player_choise)
  
    computer_choice = random.choice(choices)
    computer.config(image=computer_choice)

    
    if player_choise == choices[0] and computer_choice == choices[0]:
        score.config(text=f'Draw\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='blue')

    if player_choise == choices[0] and computer_choice == choices[1]:
        C_wins += 1
        score.config(text=f'Computer Win\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='red')

    if player_choise == choices[0] and computer_choice == choices[2]:
        P_wins += 1
        score.config(text=f'Player Win\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='green')

    if player_choise == choices[1] and computer_choice == choices[0]:
        P_wins += 1
        score.config(text=f'Player Win\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='green')

    if player_choise == choices[1] and computer_choice == choices[1]:
        score.config(text=f'Draw\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='blue')

    if player_choise == choices[1] and computer_choice == choices[2]:
        C_wins += 1
        score.config(text=f'Computer Win\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='red')

    if player_choise == choices[2] and computer_choice == choices[0]:
        C_wins += 1
        score.config(text=f'Computer Win\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='red')

    if player_choise == choices[2] and computer_choice == choices[1]:
        P_wins += 1
        score.config(text=f'Player Win\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='green')

    if player_choise == choices[2] and computer_choice == choices[2]:
        score.config(text=f'Draw\n Score: {P_wins} for Player VS {C_wins} for Computer', fg='blue')
    


score = Label(game, text='Score: ', font=('arial',20,'bold'))
score.pack(pady=10)


computer = Label(game, image=rock)
computer.pack(pady=10)
player = Label(game, image=rock)
player.pack(pady=10)


frame = Frame(game)
frame.pack()


btn_r = Button(frame, image=rock, bd=0, command= lambda: play(choices[0]))
btn_r.grid(row=0, column=0, padx=20,pady=10)

btn_p = Button(frame, image=paper, bd=0, command= lambda: play(choices[1]))
btn_p.grid(row=0, column=1, padx=20,pady=10)

btn_s = Button(frame, image=scissors, bd=0, command= lambda: play(choices[2]))
btn_s.grid(row=0, column=2, padx=20,pady=10)


game.mainloop()