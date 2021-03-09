#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:32:31 2021

@author: parth
"""
import random
import sys

board = [" " for i in range(10)]
    
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('-----------')

def winning_position(board):
    if (
        (
            (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or 
            (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or 
            (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or 
            (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or 
            (board[3] == 'X' and board[5] == 'X' and board[7] == 'X') or
            (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or
            (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or
            (board[3] == 'X' and board[6] == 'X' and board[9] == 'X')
        ) or
        (
            (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or 
            (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or 
            (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or 
            (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or 
            (board[3] == 'O' and board[5] == 'O' and board[7] == 'O') or
            (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or
            (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or
            (board[3] == 'O' and board[6] == 'O' and board[9] == 'O')
        )):
        return True
    else:
        return False

def board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
        
def player_input(board):
    n = int(input("Enter box number: "))
    while winning_position(board)==False:

        if board_full(board)==True:
            printBoard(board)
            print('Game Over')
            sys.exit()

        if (n > 0 and n < 10):

            if board[n] == " ":
                board[n] = "X"
                comp_input(board)

            else:
                print(n, " is taken")
                player_input(board)

        elif(n < 0 or n > 9):
            print("Enter a valid number: ")
            player_input(board) 

    printBoard(board)
    print("Game Over")
    sys.exit()
    
def comp_input(board):

    g = [1,3,7,9]
    c = random.choice(g)
    z = [2,4,6,8]
    e = random.choice(z)
    f = [5]
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    while winning_position(board)==False:

        if board_full(board) == True:
            printBoard(board)
            print('Game Over')
            sys.exit()

        for let in ['O']:
            for i in possibleMoves:
                board_copy = board[:]
                board_copy[i] = let
                if winning_position(board_copy) == True:
                    board[i] = 'O'
                    printBoard(board)
                    
                    if winning_position(board) == True:
                        printBoard(board)
                        print('Game Over')
                        sys.exit()

                    player_input(board)

        for let in ['X']:
            for i in possibleMoves:
                board_copy = board[:]
                board_copy[i] = let
                if winning_position(board_copy) == True:
                    board[i] = 'O'
                    printBoard(board)
                    player_input(board)
                    
                    if winning_position(board) == True:
                        printBoard(board)
                        print('Game Over')
                        sys.exit()
  
        for i in possibleMoves:
            if i in g:
                if board[c] == ' ':
                    board[c] = 'O'
                    printBoard(board)
                    player_input(board)

                else:
                    comp_input(board)

                    if winning_position(board) == True:
                        printBoard(board)
                        print("Game over")
                        sys.exit()

        for i in possibleMoves:
            if i in f:
                if board[5] == ' ':
                    board[5] = 'O'
                    printBoard(board)
                    player_input(board)

                else:
                    comp_input(board)

                    if winning_position(board) == True:
                        printBoard(board)
                        print('Game Over')
                        sys.exit()
                   
        for i in possibleMoves:
            if i in z:
                if board[e] == ' ':
                    board[e] = 'O'
                    printBoard(board)
                    player_input(board)
                else:
                    comp_input(board)

                    if winning_position(board) == True:
                        printBoard(board)
                        print('Game Over')
                        sys.exit()
                             
        else:
            comp_input(board)

        printBoard(board)
        player_input(board)
  
    printBoard(board)
    print("Game Over")
    sys.exit()

printBoard(board)
player_input(board)