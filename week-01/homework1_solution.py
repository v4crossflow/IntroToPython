#!/usr/bin/env python

"""
Chris' solution to the week 1 homework problem.

Note that we hadn't talked about loops yet, so this is a solution with no loops.

Note also that there is nore than one way to skin a cat -- or code a function
"""


def print_grid(size):
    """
    print a 2x2 grid with a total size of size
    """
    N = 2
    s = (size-1) / 2 # size of one grid box
    # top row
    top = ('+' + ' -'*s)*N + ' +' +'\n'
    middle = ('|' + ' '*2*s)*N + ' |' + '\n'

    row = top + middle*s

    grid = row*N + top

    print grid
 

def print_grid2(N, s):
    """
    print a NxN grid with each box of size s
    """
    # top row
    top = ('+' + ' -'*s)*N + ' +' +'\n'
    middle = ('|' + ' '*2*s)*N + ' |' + '\n'

    row = top + middle*s

    grid = row*N + top

    print grid

def print_grid3(size):
    """
    same as print_grid, but calling print_grid2 to do the work
    """
    N = 2
    s = (size-1) / 2 # size of one grid box
    print_grid2(N, s)

print_grid(11)
print_grid(7)

print_grid2(3,3)
print_grid2(3,5)

print_grid3(11)
