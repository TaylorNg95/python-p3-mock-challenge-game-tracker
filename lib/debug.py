#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    game1 = Game('COD')
    game2 = Game('League')

    player1 = Player('taylor')
    player2 = Player('spencer')

    result1 = Result(player1, game1, 500)
    result2 = Result(player1, game1, 600)
    result3 = Result(player2, game2, 750)
    result4 = Result(player2, game2, 850)
    result5 = Result(player1, game2, 350)
    result6 = Result(player1, game2, 450)
    result7 = Result(player2, game1, 900)
    result8 = Result(player2, game1, 1000)

    ipdb.set_trace()
