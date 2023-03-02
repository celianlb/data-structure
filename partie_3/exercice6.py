def parenthese(math):
    parenthese_ouvrante=0
    parenthese_fermante=0
    for caractere in math:
        if caractere=="(":
            print(caractere)
            parenthese_ouvrante=parenthese_ouvrante+1
            print(parenthese_ouvrante)
        elif caractere==")":
            print(caractere)
            parenthese_fermante=parenthese_fermante+1
            print(parenthese_fermante)

        
    if parenthese_fermante!=parenthese_ouvrante:
        print("paranthese manquante")    
math="2x(2+5)"
parenthese(math)