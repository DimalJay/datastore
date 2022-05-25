import itertools as its
import random

def generateRandom(length=20):
    words_num = "1234567890"
    words_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    # r = [x for x in its.product(words_num, repeat=3)][0]
    #for x in range(8):
    words_num_s = [x for x in words_num]
    words_letter_s = [x for x in words_letter]
    gen = ''

    chars = words_letter_s + words_num_s
    for _ in range(length):
        random.shuffle(chars)
        gen += chars[random.randrange(0, len(chars))]
    return gen
