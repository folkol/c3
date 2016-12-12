def chunkify(lst, n):
    """Given a list of a number n, yield consecutive chunks of size n."""
    for pos in range(0, len(lst), n):
        yield lst[pos:pos + n]


def hex_to_ints(hex_string):
    """Converts the hex string to a list of ints by converting chunks of 2 chars to int."""
    return [int(chars, 16) for chars in chunkify(hex_string, 2)]


def ints_to_hex(ints):
    as_hex = (format(x, '02x') for x in ints)
    return ''.join(as_hex)


def ints_to_base64(ints):
    """Converts a list of ints, interpreted as byte values, to base64.

    No padding support, which means that len(ints) must be a multiple of 3."""

    from string import ascii_uppercase, ascii_lowercase, digits
    numerals = ascii_uppercase + ascii_lowercase + digits + '+/'

    as_binary = (format(i, '08b') for i in ints)
    as_binary_string = ''.join(as_binary)
    return ''.join([numerals[int(x, 2)] for x in chunkify(as_binary_string, 6)])


def hex_to_base64(hex_string):
    as_ints = hex_to_ints(hex_string)
    as_base64 = (ints_to_base64(x) for x in chunkify(as_ints, 3))
    return ''.join(as_base64)


def assert_equals(expected, actual):
    assert expected == actual, "Expected '{}', but got '{}'.".format(expected, actual)
