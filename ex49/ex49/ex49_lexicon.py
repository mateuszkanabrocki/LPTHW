direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verb = ['go', 'stop', 'kill', 'eat', 'run']
stop = ['the', 'in', 'of', 'from', 'at', 'it', 'a']
noun = ['door', 'bear', 'princess', 'cabinet']


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
