from funcs import *


def encrypt(msg, key):
    from itertools import cycle
    as_ints = ascii_to_ints(msg)
    return ints_to_hex(i ^ ord(k) for i, k in zip(as_ints, cycle(key)))


if __name__ == "__main__":
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    ciphertext = encrypt(message, "ICE")

    expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632427276527' \
               '2a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    assert_equals(expected, ciphertext)
