# -*- coding: utf-8 -*-

class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, object):
        # remember we take('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

def peek(word_list):
   if word_list:
       word = word_list[0]
       return word[0]
   else:
       return None

peek1 = peek([('verb', 'eat')])
print peek1

def match(word_list, expecting):
   if word_list:
       word = word_list.pop(0)

       if word[0] == expecting:
           return word
       else:
           return None
   else:
        return None

match1 = match([('verb', 'eat'), ('noun', 'apple')], 'verb')
print match1

def skip(word_list, word_type):
    while peek(word_list) == word_type:
       print  match(word_list, word_type)

skip1 = skip([('verb', 'eat'), ('direction', 'good')], 'stop')
print skip1

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)


