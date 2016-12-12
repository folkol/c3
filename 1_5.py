from funcs import *
from funcs import encrypt_repeating_key_xor

if __name__ == "__main__":
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    ciphertext = encrypt_repeating_key_xor(message, "ICE")

    expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632427276527' \
               '2a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    assert_equals(expected, ciphertext)
