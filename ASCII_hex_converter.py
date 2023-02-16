class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join([chr(int(h[i:i + 2], 16)) for i in range(0, len(h), 2)])

    @staticmethod
    def to_hex(s):
        return ''.join([hex(ord(c))[2:] for c in s])


def main():
    print('ASCII hex converter')
    while True:
        question = int(input('1. encode to hex.\n'
                             '2. decode from hex\n'
                             '0. exit\n: '))
        if question == 0:
            break
        elif question == 1:
            print('->', Converter.to_hex(input("Enter text\n: ")))
        elif question == 2:
            print('->', Converter.to_ascii(input("Enter hexadecimal\n: ")))
        else:
            print('Try again')
            continue

        while True:
            print('Would you like to continue?')
            repeat = int(input('1. yes\n2. no\n: '))
            if repeat == 1:
                break
            elif repeat == 2:
                return
            else:
                print('Try again')


if __name__ == '__main__':
    main()
