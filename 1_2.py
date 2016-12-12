def xor(m1, m2):
    pass


if __name__ == "__main__":
    m1 = '1c0111001f010100061a024b53535009181c'
    m2 = '686974207468652062756c6c277320657965'
    result = xor(m1, m2)
    expected = '746865206b696420646f6e277420706c6179'

    assertEquals