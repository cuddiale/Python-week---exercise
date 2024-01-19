# Definiscci una funzione che, prendendo in input due parole, verifica se le due parole sono anagrammi.

def are_anagrams(word1, word2):
    if len(word1)!=len(word2):
        return False
    
    word_list = list(word1)

    for c in word2:
        if c in word_list:
            word_list.remove(c)
        else:
            return False
    
    return True

word1 = input("Prima parola: ")

word2 = input("Seconda parola: ")

anagrams = are_anagrams(word1, word2)

if anagrams:
    print(word1 + "e" + word2 +" sono anagrammi")
else:
    print(word1 + "e" + word2 +" NON sono anagrammi")