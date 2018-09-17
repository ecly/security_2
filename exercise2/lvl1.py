import string

INPUT = "YRIRY GJB CNFFJBEQ EBGGRA"

# https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-pytho://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
def caesar(plaintext, shift):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


if __name__ == "__main__":
    for i in range(26):
        print(caesar(INPUT, i))

