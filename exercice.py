#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import turtle


def ellisoid_volume(a=1, b=1, c=1, density=1):
    V = (4/3) * math.pi * a * b * c
    return (V, V * density)


def most_frequent_letter(sentence):
    letters = {}
    for c in sentence:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1

    # sort the items of the list (tuples) by their count, then return the char from the first item
    return sorted(letters.items(), key=lambda item: item[1])[-1][0]


def draw_tree():
    def draw_branch(length = 10.0, branches_left=0):
        turtle.pensize(int(length // 20))
        turtle.forward(length)
        if branches_left > 0:
            turtle.left(15)
            draw_branch(length / 1.2, branches_left - 1)
            turtle.right(30)
            draw_branch(length / 1.2, branches_left -1)
            turtle.left(15)
        turtle.back(length)

    turtle.color('red')
    turtle.setheading(90)
    draw_branch(100.0, 7)
    turtle.done()


def is_dna_sequence_valid(sequence: str):
    if len(sequence) != 0 and (sequence.count('a') + sequence.count('t') + sequence.count('g') + sequence.count('c')) == len(sequence):
        return True
    else:
        return False


def input_dna():
    chain = input("Entrez la chaine principale d'ADN a tester: ")
    while not is_dna_sequence_valid(chain):
        chain = input("Sequence invalide. Veuillez entrer une nouvelle sequence: ")

    sequence = input("Entrez la sequence dont la proportion est a tester: ")
    while not is_dna_sequence_valid(sequence):
        sequence = input("Sequence invalide. Veuillez entrer une nouvelle sequence: ")

    return chain, sequence

    
def dna_sequence_proportion(chain, sequence):
    return chain.count(sequence) * len(sequence) / len(chain)


def query_dna():
    chain, sequence = input_dna()
    proportion = dna_sequence_proportion(chain, sequence) * 100
    print(f"Il y a {proportion:.2f} % de \"{sequence}\".")


if __name__ == '__main__':
    query_dna()
