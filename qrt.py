# Copyright (C) 2020 Greenweaves Software Limited

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

#  qrt Incomplete Characters

import argparse
import os
import time
from helpers import read_strings

def tuples(n):
    for i in range(n):
        for j in range(n):
            if i==j: continue
            for k in range(n):
                if k in [i,j]: continue
                for l in range(n):
                    if l in [i,j,k]: continue
                    if i<j and k<l and i<k:
                        yield i,j,k,l

def qrt(taxa,characters):
    def isConsistent(selector):
        for char in characters:
            character = [char[i] for i in selector]
            if any(c is None for c in character): continue
            if character[0]==character[1] and character[2]==character[3] and character[0]!=character[2]: return True
        return False
    
    for (i,j,k,l) in tuples(len(taxa)):     
        selector =  [i,j,k,l]
        if isConsistent(selector):
            yield [taxa[m] for m in selector]


def expand_character(s):
    return [int(c) if c.isdigit() else None for c in s]

def format(quartet):
    return f'{{{quartet[0]}, {quartet[1]}}} {{{quartet[2]}, {quartet[3]}}}'

if __name__=='__main__':
    start = time.time()
    parser = argparse.ArgumentParser('....')
    parser.add_argument('--sample',   default=False, action='store_true', help='process sample dataset')
    parser.add_argument('--rosalind', default=False, action='store_true', help='process Rosalind dataset')
    args = parser.parse_args()
    if args.sample:
        for quartet in qrt(
                        ['cat', 'dog', 'elephant', ' ostrich', 'mouse', 'rabbit', 'robot'],
                        [expand_character() for character in ['01xxx00', 'x11xx00', '111x00x']]):
            print (format(quartet))
  
    if args.rosalind:
        Input  = read_strings(f'data/rosalind_{os.path.basename(__file__).split(".")[0]}.txt')
        
        with open(f'{os.path.basename(__file__).split(".")[0]}.txt','w') as f:
            for quartet in qrt(Input[0].split(),
                               [expand_character(character) for character in Input[1:]]):
                Result = format(quartet)
                print (Result)
                f.write(f'{Result}\n')
                
    elapsed = time.time()-start
    minutes = int(elapsed/60)
    seconds = elapsed-60*minutes
    print (f'Elapsed Time {minutes} m {seconds:.2f} s')    
