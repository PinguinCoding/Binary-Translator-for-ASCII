from translator import Translator
myTranslator = Translator()

myTranslator.BINARY_TEXT = str(input("Digite o texto em binario: "))
print("Hexadecimal: {0}".format(myTranslator.turn_to_hexadecimal()))
print("Decimal: {0}".format(myTranslator.turn_to_decimal()))
print("Text (ASCII): {0}".format(myTranslator.turn_to_ascii()))
