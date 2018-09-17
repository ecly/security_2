import lvl1



CIPHER = "OMQEMDUEQMEK"
SHIFT = ord('A') - ord('M')

if __name__ == "__main__":
    print(lvl1.caesar(CIPHER, SHIFT))
