from nose.tools import *
from ex49.parser import *
# import ex49_lexicon

def test_sentence():
    sent_test = Sentence(['noun', 'sub'], ['verb', 'ver'], ['noun', 'obj'])
    assert_equal(sent_test.subject, 'sub')
    assert_equal(sent_test.verb, 'ver')
    assert_equal(sent_test.object, 'obj')


def test_peek():
    peek_test1 = [('noun', 'princess'), ('verb', 'eat'), ('error', 'hm')]
    peek_test2 =[]
    assert_equal(peek(peek_test1), 'noun')
    assert_equal(peek(peek_test2), None)


def test_match():
    match_test1 = [('noun', 'princess'), ('verb', 'eat'), ('error', 'hm')]
    match_test2 = []
    match_test3 = [('noun', 'princess'), ('verb', 'eat'), ('error', 'hm')]
    assert_equal(match(match_test1, 'noun'), ('noun', 'princess'))
    assert_equal(match(match_test2, 'noun'), None)
    assert_equal(match(match_test3, 'verb'), None)
    

def test_skip():
    skip_test = [('noun', 'princess'), ('noun', 'hat'), ('error', 'hm')]
    assert_equal(skip(skip_test, 'error'), skip_test)
    assert_equal(skip(skip_test, 'noun'), [('error', 'hm')])


def test_parse_verb():
    parse_verb_test1 = [('stop', 'The'), ('stop', 'The'), ('verb', 'go'), ('error', 'hm')]
    parse_verb_test2 = [('stop', 'The'), ('noun', 'Jeff'), ('error', 'hm')]
    assert_equal(parse_verb(parse_verb_test1), ('verb', 'go'))
    assert_raises(ParserError, parse_verb, parse_verb_test2)


def test_parse_object():
    parse_object_test1 = [('stop', 'The'), ('number', '2'), ('noun', 'bear'), ('error', 'hm')]
    parse_object_test2 = [('stop', 'The'), ('direction', 'left'), ('error', 'hm')]
    parse_object_test3 = [('stop', 'The'), ('stop', 'in'), ('verb', 'go'), ('error', 'hm')]
    assert_equal(parse_object(parse_object_test1), ('noun', 'bear'))
    assert_equal(parse_object(parse_object_test2), ('direction', 'left'))
    assert_raises(ParserError, parse_object, parse_object_test3)


def test_parse_subject():
    parse_object_test1 = [('stop', 'The'), ('stop', 'The'), ('number', '2'), ('noun', 'bear'), ('error', 'hm')]
    parse_object_test2 = [('stop', 'The'), ('verb', 'run'), ('error', 'hm')]
    parse_object_test3 = [('stop', 'The'), ('stop', 'in'), ('direction', 'right'), ('error', 'hm')]
    assert_equal(parse_subject(parse_object_test1), ('noun', 'bear'))
    assert_equal(parse_subject(parse_object_test2), ('noun', 'player'))
    assert_raises(ParserError, parse_subject, parse_object_test3)


def test_parse_sentence():
    parse_sen_test1 = [('stop', 'The'), ('noun', 'bear'), ('verb', 'eat'), ('noun', 'princess')]
    parse_sen_test2 = [('stop', 'The'), ('verb', 'eat'), ('noun', 'princess')]
    parse_obj1 = parse_sentence(parse_sen_test1)
    parse_obj2 = parse_sentence(parse_sen_test2)
    assert_equal(parse_obj1.subject, 'bear')
    assert_equal(parse_obj1.verb, 'eat')
    assert_equal(parse_obj1.object, 'princess')
    assert_equal(parse_obj2.subject, 'player')
    assert_equal(parse_obj2.verb, 'eat')
    assert_equal(parse_obj2.object, 'princess')
