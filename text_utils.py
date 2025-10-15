text = 'the fox ran down the road'


def word_counter(text):
    words = text.split(' ')
    return len(words)


def vowel_counter(text):
    counter = 0
    for chr in text:
        if chr in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    return counter
