from funcs import *


def hamming_distance(s1, s2):
    def byte_distance(byte1, byte2):
        if not byte1 or not byte2:
            return 8
        byte_string1 = format(ord(byte1), '08b')
        byte_string2 = format(ord(byte2), '08b')
        return len([1 for c1, c2 in zip(byte_string1, byte_string2) if c1 != c2])
    from itertools import zip_longest
    return sum(byte_distance(i, j) for i, j in zip_longest(s1, s2))


if __name__ == "__main__":
    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    assert_equals(37, hamming_distance(s1, s2))
