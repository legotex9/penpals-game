#-------------------------------------------------------------------------------
# Name:        characters-PenPalsGame
# Purpose:     contains all characters for the penpals birth day game
#
# Author:      Kire Brownback
#
# Created:     23/05/2018
# Copyright:   (c) Kire Brownback 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class characters():
    '''
       health = int()
       speed = int()
       inv = []
       species = ''
       abilities = []
    '''
    class kiraraw():
        health = int(100)
        speed = int(20)
        inv = ['pen','rat']
        species = 'cat'
        abilities = []

    class crow():
        health = int(100)
        speed = int(30)
        inv = ['paint brush','cat']
        species = 'birb'
        abilities = ['flight']

    class cvizzle():
        health = int(100)
        speed = int(20)
        inv = ['hammer','rat']
        species = 'dog'
        abilities = []

    class Steve():
        health = int(25)
        speed = int(1)
        inv = []
        species = 'caterpilar'
        abilities = ['adorabilness']