def break_words(stuff):
    #this quote will be visible through help() in python ^^ -> "documentation comments"
    """This function will break up words for us.""" 
    print(">>>>break words: ", stuff)
    words = stuff.split(" ")
    print("<<<<break words: ", words)
    return words

def sort_words(words):
    """Sorts the words."""
    print(f">>>>sort words: {words}")
    print(f"<<<<sort words: {sorted(words)}")
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    print(f">>>>print first word: {words}")
    word = words.pop(0)
    print("<<<<print first word:", word)
    print(word)

def print_last_word(words):
    """Prints the last word after popping if off."""
    print(f">>>>print last word: {words}")
    word = words.pop(-1)
    print("<<<<print last word:", word)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    print(">>>>sort sentence: ", sentence)
    words = break_words(sentence)
    print(f">>>>sort sentence: {words}")
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last word of the sentence."""
    print(">>>>print first and last: ", sentence)
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    print(">>>>print first and last: exit")

def print_first_and_last_sorted(sentence):
    """Sorts the words, then prints the first and the last one."""
    print(">>>>print first and last sorted: ", sentence)
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    print(">>>>print first and last sorted: exit")
