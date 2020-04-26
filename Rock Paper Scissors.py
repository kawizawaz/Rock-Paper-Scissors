import random
match = {"Rock": ("Scissors", "Paper"), "Paper": ("Rock", "Scissors"),
         "Scissors": ("Paper", "Rock")}
while True:
    c = input("Rock, Paper or Scissors: ")
    if c in match:
        x = random.choice(["Rock", "Paper", "Scissors"])
        print(f'Opponent picked {x}')
        if match[c][0] == x:
            print("Win")
        elif match[c][1] == x:
            print("Lose")
        else:
            print("Tie")




