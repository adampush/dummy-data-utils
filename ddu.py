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

def lod_words(n_dicts=3, keyvals=3):
    """Create a List of Dictionaries (LOD) with number of Dictionaries equal
    to n_dicts. Argument keyvals determines how many entries will be in each
    Dictionary and what the keys are. If keyvals is an integer, the keys will
    be incrementing integers from 0 to keyvals - 1, inclusive. If keyvals is a
    set, tuple or list then the keys will be the elements of keyvals (the elements
    must be unique). The values of each Dictionary will be words chosen randomly 
    from a word list."""
    # TODO add a kwarg takes list of keys so user could provide own keys
    word_list = load_word_list()
    lod = []
    for x in range(n_dicts):
        # Lambda function returns list element at random index
        rand_word = lambda wl: wl[random.randint(0, len(wl) - 1)]

        # Create dictionary according to keyvals argument type
        if type(keyvals) is int:
            d = {index: rand_word(word_list) for index in range(keyvals)}
        elif type(keyvals) in {tuple, set, list}:
            d = {key: rand_word(word_list) for key in keyvals}
        else:
            raise TypeError
        lod.append(d)

    return lod

def search_lod_for_key_val(key, value, lod):
    """Search a List of Dictionaries (LOD) for a key/value pair and return a 
    generator object that contains dictionaries that match. This function
    is kind of pointless because the function signature is more characters
    in length than the generator-creating expression that it executes, but
    maybe it is a little more readable."""
    return (d for d in lod if d[key] == value)
