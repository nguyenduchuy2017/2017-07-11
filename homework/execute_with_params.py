#! /usr/bin/python
# -*- coding: utf8 -*-

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-name", '--name_value', type=str,
                    help= "Choose word for filter! (Ex. 'hello')")

parser.add_argument("-score", '--score_value', type=int,
                    help= "Choose number of the best moody for tweets! (Ex. '10', '-12')")

args = parser.parse_args()
name = args.name_value
score = args.score_value

if __name__ == '__main__':

        if ( score > 0 and score <= 400 ):
            print ("Congrate", name, " your score is ", score , "and your level is 1 " )
        elif ( score > 400 and score <= 800 ):
            print ("Congrate", name, " your score is ", score , "and your level is 2 ")
        elif ( score > 800 ):
            print ("Congrate", name, " your score is ", score , "and your level is 3")
        else :
            print("Please, enter your score > 0 :")