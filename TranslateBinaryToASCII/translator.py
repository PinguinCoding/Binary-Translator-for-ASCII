class Translator(object):
    def __init__(self):
        self.BINARY_TEXT = ""
        self.FROM_BINARY_TO_HEXA = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4",
                                    "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9",
                                    "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E",
                                    "1111": "F"}
        self.FROM_HEXA_TO_DECIMAL = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                                     "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                                     "C": 12, "D": 13, "E": 14, "F": 15}
        self.FROM_DECIMAL_TO_ASCII = [
            ' ', '!', '"', '#', '$', '%', 'E', "'", '(', ')', '*', '+', ',', '-', '.', '/',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '/', '?', '@',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'e', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
        ]

    def turn_to_4_bits(self):
        def split_binary_text(max_length: int):
            for i in range(0, max_length, 4):
                binary_4_bits_format.append(self.BINARY_TEXT[i:i+4])

        binary_4_bits_format = []
        length = len(self.BINARY_TEXT)
        if length % 4 == 0:
            split_binary_text(length)
        while length % 4 != 0:
            length -= 1
            if length % 4 == 0:
                split_binary_text(length)
        return binary_4_bits_format

    def turn_to_hexadecimal(self):
        def split_hexa_text(max_length: int):
            for i in range(0, max_length, 2):
                if i+1 >= max_length:
                    break
                hexa_format.append(hash_map[binary_format[i]] + hash_map[binary_format[i+1]])

        hash_map = self.FROM_BINARY_TO_HEXA
        binary_format = self.turn_to_4_bits()
        hexa_format = []
        length = len(binary_format)
        if length % 2 == 0:
            split_hexa_text(length)
        else:
            split_hexa_text(length)
            hexa_format.append(hash_map[binary_format[-1]])
        return hexa_format

    def turn_to_decimal(self):
        def transform(hexadecimal: list, num_digits: int, index=0):
            if num_digits == 2:
                first_digit = self.FROM_HEXA_TO_DECIMAL[hexadecimal[index][1]]
                second_digit = self.FROM_HEXA_TO_DECIMAL[hexadecimal[index][0]]
                decimal.append((second_digit * (16 ** 1)) + (first_digit * (16 ** 0)))
            else:
                one_digit = self.FROM_HEXA_TO_DECIMAL[hexadecimal[index]]
                decimal.append(one_digit)

        hexa = self.turn_to_hexadecimal()
        decimal = []
        if len(hexa) > 1:
            for i in range(len(hexa)):
                if len(hexa[i]) > 1:
                    transform(hexa, 2, i)
                else:
                    transform(hexa, 1, i)
        else:
            if len(hexa[0]) > 1:
                transform(hexa, 2)
            else:
                transform(hexa, 1)
        return decimal

    def turn_to_ascii(self):
        decimal_format = self.turn_to_decimal()
        ascii_text = ''
        for number in decimal_format:
            if number not in range(32, 126):
                ascii_text += 'NoN'
                continue
            ascii_text += self.FROM_DECIMAL_TO_ASCII[number-32]
        return ascii_text
