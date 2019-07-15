#!/usr/bin/env python3

def main():
    anotheremptylist = []

    ## This will throw an ERROR
    ## the extend method expects exactly one argument
    anotheremptylist.extend('10.0.0.1', 'retro_game_server')

    print(anotheremptylist)

main()
