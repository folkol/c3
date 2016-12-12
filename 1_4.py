onethree = __import__('1_3')


if __name__ == "__main__":
    with open("1_4.txt") as f:
        message_candidates = (onethree.decode(line.strip(), x) for line in f for x in range(0, 256))
        print(max(message_candidates, key=onethree.score))
