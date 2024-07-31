original_sentence=input()
dictio = {
        'A': 'f', 'B': 'g', 'C': 'h', 'D': 'i', 'E': 'j', 'F': 'k', 'G': 'l', 'H': 'm', 'I': 'n', 'J': 'o', 'K': 'p', 'L': 'q', 'M': 'r',
        'N': 's', 'O': 't', 'P': 'u', 'Q': 'v', 'R': 'w', 'S': 'x', 'T': 'y', 'U': 'z', 'V': 'a', 'W': 'b', 'X': 'c', 'Y': 'd', 'Z': 'e',
        'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r',
        'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e'
    }
encrypted_sentence=""

for char in original_sentence:
    if char in dictio:
        encrypted_sentence += dictio[char]
    else:
        encrypted_sentence += char 
print("The encrypted sentence is: ",encrypted_sentence)
