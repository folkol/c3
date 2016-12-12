"""xor(m1, m2) -> m3"""
from funcs import *

if __name__ == "__main__":
    message1 = '1c0111001f010100061a024b53535009181c'
    message2 = '686974207468652062756c6c277320657965'
    result = xor(message1, message2)

    assert_equals('746865206b696420646f6e277420706c6179', result)
