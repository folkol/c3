from funcs import *


def xor(s1, s2):
    return ints_to_hex([a ^ b for a, b in zip(hex_to_ints(s1), hex_to_ints(s2))])


if __name__ == "__main__":
    message1 = '1c0111001f010100061a024b53535009181c'
    message2 = '686974207468652062756c6c277320657965'
    result = xor(message1, message2)

    assert_equals('746865206b696420646f6e277420706c6179', result)
