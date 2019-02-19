#Tp OC dictionnaire ordonné.

class DictionnaireOrdonne(object):
    """Classe qui créera des dictionnaires ordonnés"""

    def __init__(self,dico = {}, **kwargs):
        self._cle = []
        self._val = []
        
        #Ajout suite à la lecture du corrigé proposé.
        if not isinstance(dico,(dict, DictionnaireOrdonne)):
            raise TypeError("Le type attendu est soit un dictionnaire(usuel ou ordonné)")

        # quelque soit le type d'objet entré dans le constructeur,
        # on itère dedans et on rempli self.key et self.val

        for key, val in kwargs.items():
            self._cle.append(key)
            self._val.append(val)
        for key, val in dico.items():
            self._cle.append(key)
            self._val.append(val)

    def __repr__(self):
        """Fonction creer la representation de de mon dictionnaire"""
        chaine = '{'
        for i in range(len(self._cle)):
            if (i+1) == len(self._cle):
                chaine = chaine + "{0}:{1}".format(self._cle[i], self._val[i])
            else: 
                chaine = chaine + "{0}:{1}".format(self._cle[i], self._val[i]) + ', '
        chaine += '}'
        return chaine
    # ajout suite à la correction (avant je n'utilisais que str pas repr. J'ai donc inversé)
    def __str__(self):
        return repr(self)

    def __getitem__(self, item):
        """Fonction d'affichage de la valeur"""
        if item in self._cle :
            i = self._cle.index(item)
            return self._val[i]
        else :
            return None


    def __setitem__(self, item, n_valeur):
        """Foncion qui creer une clé et qui ajoute/modifie sa valeur"""
        if item not in self._cle:
            self._cle.append(item)
            self._val.append(n_valeur)
        else :
            i = self._cle.index(item)
            self._val[i] = n_valeur


    def __delitem__(self, item):
        if item in self._cle:
            i = self._cle.index(item)
            del self._cle[i]
            del self._val[i]
        else :
            #Ajout après lecture du corrigé.
            raise KeyError(" le clé : {0} ne se trouve pas dans le dictionnaire".format(item))

    def __contains__(self, item):
        if item in self._cle :
            return True
        else :
            return False


    def __len__(self):
        return len(self._cle)

    def sort(self, reverse = False):
        """Methode qui tri notre dictionnaire"""
        if reverse == False :
            self._cle.sort()
            self._val.sort()            
        elif reverse == True:
            self._cle.sort(reverse = True) 
            self._val.sort(reverse = True)


    def keys(self):
        """generateur de cle"""
        for item in self._cle:
            yield item
    
    def values(self):
        """generateur de valeur"""
        for item in self._val:
            yield item

    def items(self):
        """generateur d'un tuple (cle, valeur)"""
        for i in range(len(self._cle)):
            yield (self._cle[i], self._val[i])

    def __add__(self, other):
        self._cle = self._cle + other._cle
        self._val = self._val + other._cle
        return self


