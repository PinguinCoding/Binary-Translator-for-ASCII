import pytest
from translator import Translator


@pytest.fixture()
def translator():
    return Translator()


def test_turn_to_4_bits_function(translator):
    translator.BINARY_TEXT = "00111100"
    assert translator.turn_to_4_bits() == ["0011", "1100"]
    translator.BINARY_TEXT = "001111001"
    assert translator.turn_to_4_bits() == ["0011", "1100"]
    translator.BINARY_TEXT = "0011110011"
    assert translator.turn_to_4_bits() == ["0011", "1100"]
    translator.BINARY_TEXT = "00111100111"
    assert translator.turn_to_4_bits() == ["0011", "1100"]
    translator.BINARY_TEXT = "001111001111"
    assert translator.turn_to_4_bits() == ["0011", "1100", "1111"]


def test_turn_to_hexa_function(translator):
    translator.BINARY_TEXT = "00111100111"
    assert translator.turn_to_hexadecimal() == ["3C"]
    translator.BINARY_TEXT = "001111001111"
    assert translator.turn_to_hexadecimal() == ["3C", "F"]
    translator.BINARY_TEXT = "00111100111100"
    assert translator.turn_to_hexadecimal() == ["3C", "F"]
    translator.BINARY_TEXT = "0011110011110000"
    assert translator.turn_to_hexadecimal() == ["3C", "F0"]


def test_turn_to_decimal_function(translator):
    translator.BINARY_TEXT = "00111100"
    assert translator.turn_to_decimal() == [60]
    translator.BINARY_TEXT = "0011110"
    assert translator.turn_to_decimal() == [3]
    translator.BINARY_TEXT = "00111100111100"
    assert translator.turn_to_decimal() == [60, 15]
    translator.BINARY_TEXT = "0011110011110000"
    assert translator.turn_to_decimal() == [60, 240]


def test_turn_to_ascii_function(translator):
    translator.BINARY_TEXT = "00111100"
    assert translator.turn_to_ascii() == '<'
    translator.BINARY_TEXT = "00110011"
    assert translator.turn_to_ascii() == '3'
    translator.BINARY_TEXT = "01001111011011000110000100100000011011010111010101101110011001000110111100100001"
    assert translator.turn_to_ascii() == 'Ola mundo!'
    translator.BINARY_TEXT = "00111100111100111010100100101010101"
    assert translator.turn_to_ascii() == "<NoNNoN*"
