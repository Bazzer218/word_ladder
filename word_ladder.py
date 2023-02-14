#!/bin/python3

from collections import deque
import copy

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    errors = 0
    for i in list(range(len(word1))):
        if word1[i] != word2[i]:
            errors += 1
    
    if errors != 1:
        return False
    else:
        return True


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == []:
        return False
    
    if len(ladder) == 1:
        return True

    for i in list(range(len(ladder)-1)):
        if _adjacent(ladder[i],ladder[i+1]) == False:
            return False
    return True

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    if len(start_word) != len(end_word):
        return None

    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    with open('words5.dict') as d:
        dictionary = [x.strip() for x in d.readlines()]
    #dictionary_copy = copy.copy(dictionary) 
    while len(queue) != 0:      
        current_stack = queue.popleft() 
        dictionary_copy = copy.copy(dictionary)
        dictionary_copy = [d for d in dictionary_copy if d not in current_stack]
        for i in dictionary_copy:
            if _adjacent(i,current_stack[-1]):
                if i == end_word:
                    current_stack.append(i)
                    return current_stack
                else:
                    stack_copy = copy.copy(current_stack)
                    stack_copy.append(i)
                    queue.append(stack_copy)
                    dictionary_copy.remove(i)
    return None
        
        
        
        #for i in dictionary:
         #   if _adjacent(i,stack[0]):
          #      if i == end_word:
           #         stack_copy = copy.copy(stack)
            #    else:
                    
                    
             #       stack_copy.append(i)
              #      queue.append(stack_copy)
               #     dictionary.pop(i)
                #    dictionary.remove(i)
    #return None        

#while len(queue) != 0:



