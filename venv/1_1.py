"""
hex -> base64 encoding

References:
    https://en.wikipedia.org/wiki/Hexadecimal
    https://en.wikipedia.org/wiki/Base64
"""


def hex_to_base64(hex_string):
    def chunkify(lst, n):
        for pos in range(0, len(lst), n):
            yield lst[pos:pos + n]

    def to_base64(ints):
        """Converts a list of ints, interpreted as byte values, to base64.

        No padding support, which means that len(ints) must be a multiple of 3."""
        def to_binary_string(i):
            """Encodes the given number i as a binary string and strips the leading '0b'."""
            strip_0b = bin(i)[2:]
            return strip_0b.zfill(8)

        from string import ascii_uppercase, ascii_lowercase, digits
        numerals = ascii_uppercase + ascii_lowercase + digits + '+/'

        binary_string = ''.join(to_binary_string(x) for x in ints)
        return ''.join([numerals[int(x, 2)] for x in chunkify(binary_string, 6)])

    as_ints = [int(chars, 16) for chars in chunkify(hex_string, 2)]
    return ''.join(to_base64(x) for x in chunkify(as_ints, 3))


if __name__ == '__main__':
    message = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    encoded = hex_to_base64(message)
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert encoded == expected, "Expected '{}', but got '{}'.".format(expected, encoded)
