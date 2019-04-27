# import ex49_lexicon
# __Import__ ('C:\Windows\System32\projects\ex49\ex49')
# path ='C:\Windows\System32\projects\ex49\ex49_lexicon'
# print(path)
# a='\u005C'
# file=open(f"C:{a}Windows{a}System32{a}projects{a}ex49{a}ex49_lexicon")

direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verb = ['go', 'stop', 'kill', 'eat', 'run']
stop = ['the', 'in', 'of', 'from', 'at', 'it', 'a']
noun = ['door', 'bear', 'princess', 'cabinet']


class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # take ('noun','princess') return 'princess'
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def scan(sentence):
    sentence_cleaned = sentence.strip()
    for i in '.,;:?!':
        sentence_cleaned = sentence_cleaned.replace(i, '')

    words_lowercase = sentence_cleaned.lower().split()
    words = sentence_cleaned.split()
    lexicon = []
    adress = -1

    for i in words_lowercase:
        adress += 1
        if i in direction:
            lexicon.append(('direction', i))

        elif i in verb:
            lexicon.append(('verb', i))

        elif i in stop:
            lexicon.append(('stop', i))

        elif i in noun:
            lexicon.append(('noun', i))

        else:
            try:
                lexicon.append(('number', int(i)))

            except ValueError:
                lexicon.append(('error', words[adress]))

    return lexicon


# take ('noun','princess') return 'noun'
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


# take ('noun','princess') and 'noun' pop and return ('noun','princess')
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
    return word_list

def parse_verb(word_list):
    #skip stop marks, numbers and again stop marks
    # in case there is a stop mark following th enumber
    skip(word_list, 'stop')
    skip(word_list, 'number')
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next. Don't know the word.")


def parse_object(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'number')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next. Don't know the word.")


def parse_subject(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'number')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next. Don't know the word.")


def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

# sen = parse_sentence(ex49_lexicon.scan('the bear run south?'))
# print(sen.subject, sen.verb, sen.object)


# input_obj = parse_sentence(scan(input("Type the sentence:> ")))
# print(input_obj.subject, input_obj.verb, input_obj.object)