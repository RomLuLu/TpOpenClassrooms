#Exo 10.50 controle du flux partie 2

def ajout_donnees():
    while 1:
        nom = input("Entrer 'nom' à ajouter <enter> pour quitter : ")      
        if nom == '':
            break          
        if nom in base_donnees:
            print('{} est déjà présent(e).'.format(nom))
        else:
            age = input("Entrer 'age' à ajouter : ")
            taille = input("Entrer 'taille' à ajouter (forme x.xx m) : ")
            base_donnees[nom] = (age, taille)

def consulter_donnees():
    print("liste des noms :")
    liste_nom = list()
    for key in base_donnees.keys():
        print("nom : ", key, end=' | ')    
        liste_nom.append(key)
    while True :
        nom = input("Entrer nom (taper 'enter pour quitter) :")
        if nom == '':
            break
        elif nom not in liste_nom:
            print("Cette personne n'est pas dans la liste !") 
        else:
            print( "{0} - âge : {1} ans - taille : {2} m".format(nom, base_donnees[nom][0], base_donnees[nom][1]))


            
def enregistrerBaseDeDonnee():
    nom_fichier = input("Entrer nom du fichier : ")
    fd = open(nom_fichier, 'w', encoding='utf-8')
    for key, value in base_donnees.items():
        fd.write("{0}@{1}#{2}\n".format(key, value[0], value[1]))
    fd.close()

def importerBaseDeDonnee():
    base_donnees = {}
    nom_fichier = input("Entrer nom du fichier a import + extension : ")
    fichier = open(nom_fichier, 'r', encoding= 'utf-8')
    while True :
        base = fichier.readline()
        if base == '':
            break
        else:
            for c in base :
                if c == '@':
                    base = base.replace(c, ' ')
                elif c == '#':
                    base = base.replace(c, ' ')
                elif c == '\n':
                    base = base.replace(c, ' ')
            base = base.split(' ')
            for item in base:
                base_donnees[base[0]] = (base[1], base[2])
    fichier.close() 

def quitter():
    print("Au revoir")


# programme:


choix = {
    "1": ajout_donnees,
    "2": consulter_donnees,
    "3": enregistrerBaseDeDonnee,
    "4": importerBaseDeDonnee,
    "5": quitter
        } 

base_donnees = {}

while 1:   
    number = input("Entrer votre choix :\n<1>Pour ajouter donneees :\n<2>Pour consulter donnees:\n<3>Pour enregistrer la base de donnee:\n<4>Pour importer une base de donnees:\n<5>Pour quitter:")               
    if number == '5':
        choix[number]()
        break
    choix[number]()
