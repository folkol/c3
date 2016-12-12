"""
hex -> base64 encoding

References:
    https://en.wikipedia.org/wiki/Hexadecimal
    https://en.wikipedia.org/wiki/Base64
"""
from funcs import hex_to_base64, assert_equals

if __name__ == '__main__':
    message = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    encoded = hex_to_base64(message)

    assert_equals('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t', encoded)
