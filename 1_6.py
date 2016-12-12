from funcs import *


def hamming_distance(str1, str2):
    def byte_distance(byte1, byte2):
        if not byte1 or not byte2:
            return 8
        byte_string1 = format(byte1, '08b')
        byte_string2 = format(byte2, '08b')
        return len([1 for c1, c2 in zip(byte_string1, byte_string2) if c1 != c2])

    from itertools import zip_longest
    return sum(byte_distance(i, j) for i, j in zip_longest(str1, str2))


if __name__ == "__main__":
    s1 = b'this is a test'
    s2 = b'wokka wokka!!!'
    assert_equals(37, hamming_distance(s1, s2))

    # There's a file here. It's been base64'd after being encrypted with repeating-key XOR.
    with open('1_6.txt') as f:
        from base64 import standard_b64decode as decode

        cipher_text = decode(f.read())

    print(cipher_text)

    def score(key_len):
        """Returns a score for this key length.

        The score is the normalized edit distance between two words grabbed from the cipher text."""
        word1 = cipher_text[0:key_len]
        word2 = cipher_text[key_len:key_len * 2]
        print(word1, word2)
        return hamming_distance(word1, word2) / key_len


    print(sorted([x for x in range(2, 40)], key=score)[:3])
