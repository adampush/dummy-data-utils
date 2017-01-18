"""This is a friendly little catch-all module for functionized utility
snippets!"""

import random
import os
from os import path


FILE_PATH_WORD_LIST_3ESL = path.dirname(path.abspath(__file__)) + os.sep + '3esl.txt'


def lod(n_dicts=3, n_keyvals=3):
    """Create a List of dictionaries (LOD) having n_dicts dictionaries each 
    with n_keyvals elements. The keys are incrementally generated integers
    and the values are randomly generated integers."""
    listofdicts = []
    for x in range(n_dicts):
        d = {index: random.randint(-2**32, 2**32) for index in range(n_keyvals)}
        listofdicts.append(d)
    
    return listofdicts

def load_word_list():
    """Create a List with English words by reading them in from a file.
    Currently using the '3esl.txt' list available from http://wordlist.aspell.net"""
    lst = []
    with open(FILE_PATH_WORD_LIST_3ESL) as f:
        for line in f:
            lst.append(line.strip())
    return lst

def lod_words(n_dicts=3, n_keyvals=3):
    """Create a List of n_dicts Dictionaries (LOD). The Dictionaries have
    keys that are incrementing integers and values that are words chosen
    randomly from a word list. There are n_keyvals key/value pairs in each
    Dictionary."""
    word_list = load_word_list()
    lod = []
    for x in range(n_dicts):
        rand_word = lambda wl: wl[random.randint(0, len(wl) - 1)]
        d = {index: rand_word(word_list) for index in range(n_keyvals)}
        lod.append(d)
    return lod
