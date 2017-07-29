# -*- coding: utf-8 -*-

from nose.tools import *
from ex49.parser import *

def test_Sentence():
    sentence = Sentence(('noun', 'apple'), ('verb', 'eat'), ('direction', 'good'))
    assert_equal(sentence.subject, 'apple')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'good')

def test_peek():
    peeka = peek([('verb', 'eat'), ('noun', 'apple'), ('direction', 'good')])
    peekb = peek([])
    assert_equal(peeka, 'verb')
    assert_equal(peekb, None)

def test_match():
    matcha = match([('verb', 'eat'), ('noun', 'apple'), ('direction', 'good')], 'verb')
    matchb = match([('verb', 'eat'), ('noun', 'apple'), ('direction', 'good')], 'noun')
    matchc = match([], 'verb')
    assert_equal(matcha, ('verb', 'eat'))
    assert_equal(matchb, None)
    assert_equal(matchc, None)

def test_skip():
    skipa = skip([('verb', 'eat'), ('noun', 'apple'), ('direction', 'good')], 'stop')
    assert_equal(skipa, None)

