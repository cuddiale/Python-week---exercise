# # Leggi una stringa in input all'interno di un loop. 
# Se la stringa è uguale a "stop" interrompi il programma, altrimenti verifica se la stringa è un palindromo, 
# in caso positivo stampa "Parola è un palindromo"inserendo la parola inserita in input al posto di Parola, 
# altrimenti stampa "parola non è un palindromo".

word = input()

while word!="stop":
    
    is_palindrome = True
    word_len = len(word)

    for i in range(word_len):
        
        j = word_len -1 -i

        if word[i] != word[j]:
           
            is_palindrome = False
            
            break
    
        if is_palindrome:

            print(word, "è un palindromo")
        
        else:
            
            print("Non è un palindromo")
        
        word = input()
