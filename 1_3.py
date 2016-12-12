"""Decrypt xor cipher by means of frequency analysis.

References:
        http://www.rinkworks.com/words/letterfreq.shtml
"""

from funcs import *
from funcs import ints_to_ascii

onetwo = __import__('1_2')


def decode(hex_string, key):
    """Decrypts the xor-ciphered and hex encoded message."""
    as_ints = hex_to_ints(hex_string)
    return ints_to_ascii([i ^ key for i in as_ints])


def score(message):
    """Calculates a message score by means of frequency analysis."""
    common_letters = 'etaoin shrdlu'
    return len([c for c in message if c.lower() in common_letters])


if __name__ == "__main__":
    ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    message_candidates = (decode(ciphertext, x) for x in range(0, 256))
    print(max(message_candidates, key=score))
