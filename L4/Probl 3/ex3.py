
import random

def play_game():
    characters = ['piatra', 'hartie', 'foarfece']   #lista obiectelor jocului
    player_score = 0    #scorul jucatorului
    computer_score = 0  #scorul calculatorului

    for _ in range(3):      #3 runde
        computer_choice = random.choice(characters)     #se genereaza un obiect aleatoriu
        print("Disponibile: piatra, hartie, foarfece")
        user_choice = input("Alege un obiect: ").lower()    #se retine alegerea jucatorului, modificandu-se
                                                                    #in caractere mici
        if user_choice in characters:   #daca cuvantul introdus este corect, in lista se va afisa
            print(f"Calculatorul a ales: {computer_choice}")        #alegerea calculatorului
            if user_choice == computer_choice:      #daca s-a ales la fel se afiseaja mesajul egalitate
                print("Egalitate!")
            #se iau in considerare toate situatiile de castig iar daca vreuna este valabila se va afisa mesaj
            elif (user_choice == 'piatra' and computer_choice == 'foarfece') or \
                 (user_choice == 'foarfece' and computer_choice == 'hartie') or \
                 (user_choice == 'hartie' and computer_choice == 'piatra'):
                print("Ai câștigat această rundă!")
                player_score += 1       #creste scorul jucatorului
            else:
                print("Calculatorul a câștigat această rundă!")
                computer_score += 1     #daca nu sunt valabile creste scorul calculatorului
        else:
            #daca cuvantul introdus de jucator nu este valid se afiseaza mesaj
            print("Te rog să alegi un obiect valid: piatră, hârtie sau foarfece")

    if player_score > computer_score:   #se compara scorurile si se afiseaza mesaj cu castigatorul
        print("Felicitări, ai câștigat jocul!")
    elif player_score < computer_score:
        print("Calculatorul a câștigat jocul. Mai încercăm?")
    else:       #daca scorul este egal, se afiseaza remiza
        print("Este remiză!")

play_game()