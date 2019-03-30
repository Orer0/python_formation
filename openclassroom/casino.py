import os
from random import randrange
from math import ceil

player_cash = 1000
while player_cash > 0:
    print("Votre mise actuelle est de", player_cash)

    print("Montant de votre mise : \n")
    player_mise = input()

    print("Misez un numero entre 0 et 49 : ")
    player_num = input()
    player_num = int(player_num)
    player_mise = int(player_mise)
    player_cash = int(player_cash)
    if player_num >= 0 and player_num <= 49:
        print("Good choice")

    while player_num < 0 or player_num > 49:
        print("Nombre invalide, veuillez saisir un nombre entre 0 et 49")
        player_num = input()

    print("le croupier procede au jeu\n")

    croupier_num = randrange(50)

    if croupier_num == player_num:
        print("YOU WIN MAX CASH\n")
        player_mise = ceil(player_mise*3)
        player_cash = player_cash + player_mise
    elif croupier_num % 2 == 0 and player_num % 2 == 0:
        print("YOU WIN 50%\n")
        player_mise = ceil(player_mise / 2)
        player_cash = player_cash - player_mise
    else:
        player_cash = player_cash - player_mise
        print("YOU LOOSE\n")

    print("Your cash is of", player_cash)
