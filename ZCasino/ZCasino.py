from random import randint
from math import ceil

"""
Création du jeu ZCasino.
C'est une roulette ou le joueur mise une somme d'argent sur des numéros allant de 0 à 49
-> les N°pairs sont noirs et les N°impairs sont rouges.
règles :
    ->si le joueur mise sur le même N° que celui de la roulettre gains = 3 X mise plus la mise
    ->si mauvais N° mais bonne couleur : gains = mise + 50%mise
    -> sinon le joueur perd tout
"""

enter_game = True
while enter_game:
    #On demande au joueur de rentrer la mise de départ.

    solde_depart = input("Entrer le montant avec lequel vous voulez jouer : ")
    try :
        solde_depart = int(solde_depart)
    except :
        print("Mettre un nombre entier(pas de lettre , ni de nombre à virgule.")
        continue

    print("Votre solde de départ est de {} $".format(solde_depart))

    #on rentre dans la partie mise.
    continuer = 'o'
    while solde_depart > 0 and continuer =='o' :

        # choix de la mise du joueur:
        mise = input("Entrez votre mise (entier attendu pas de chiffre a virgule ni de lettre) : ")
        try :
            mise = int(mise)
        except:
            print("Attention {} n'est pas acceptable.".format(mise))
            continue
        else :
            if mise > solde_depart :
                print("Vous ne pouvez pas miser plus que votre solde qui est de {}$".format(solde_depart))
                continue
        solde_depart -= mise
        # choix du numéro par le joueur.
        
        numero_joueur = ''
        while not numero_joueur.isdigit():
            numero_joueur = input("Entrer un nombre entre 0 et 49 :")
            if int(numero_joueur) not in  range(50):
                print("Le nombre doit être compris entre 0 et 49. nouvelle essai .....")
                numero_joueur = ''
                continue
        numero_joueur = int(numero_joueur)
        # choix du numéro par l'ordinateur.
        numero_random = randint(0, 49)
        print("Attention la roulette est lancée ......")
        

        # comparaison des résultats
        print("La bille s'est arrétée sur le numéro {}.".format(numero_random))
        if numero_joueur == numero_random :
            gain = mise + 3*mise
            solde_depart = solde_depart + ceil(gain)
            print("Bravo, vous avez trouvé le bon numéro. Vous avez gagnez : {}$. Votre solde est donc de {}$".format(gain, solde_depart))
        elif numero_joueur%2 == numero_random%2:
            gain = mise + mise*0.5
            solde_depart = solde_depart +ceil(gain)
            print("Bravo, vous avez trouvé la bonne couleur. Vous avez gagnez : {}$. Votre solde est donc de {}$".format(gain, solde_depart))
        else :
            print("Dommage vous avez perdu. votre solde est de {0}$".format(solde_depart))

        continuer = ''
        while not (continuer == 'o' or continuer == 'n'):
            continuer = (input("Continuer à miser ou partir ??? (o/n): ")).lower()
            if continuer == 'o':
                continue
            elif continuer == 'n':
                print("Merci et à bentôt !")
                break
        enter_game = False           

print("Vous partez avec la somme de {0}$".format(solde_depart))