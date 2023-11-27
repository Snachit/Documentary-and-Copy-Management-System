class Documentair:
    count = 0 
    def __init__(self, titre, date_sortie):
        self.titre = titre  
        self.date_sortie = date_sortie 
        Documentair.count += 1
        self.code = Documentair.count
        
    
    def set_titre(self, value):
        self.titre = value

    def get_titre(self):
        return self.titre
    
    def set_date_sortie(self, value):
        self.date_sortie = value

    def get_date_sortie(self):
        return self.date_sortie
    
    def get_code(self):
        return self.code
    
    def ToString(self):
        return f"""Titre :{self.titre}
Date de sortie: {self.date_sortie}
Code :{self.code} """
    
    def Equal(self, doc2):
        if self.code == doc2.code:
            return True 
        else:
            return False
        
class Exemplaire(Documentair):
    def __init__(self, titre, date_sortie, numero, date_achat):
        super().__init__(titre, date_sortie)
        self.numero = numero 
        self.date_achat = date_achat
    
    def set_numero(self, value):
        self.numero = value 

    def get_numero(self):
        return self.numero 
    
    def set_date_achat(self, value):
        self.date_achat = value 

    def get_date_achat(self):
        return self.date_achat

    def ToString(self):
        return f"""{super().ToString()}
date d'achat: {self.date_achat}
Numero: {self.numero}"""
    
    def Equal(self, doc2):
        if self.numero == doc2.numero :
            return True


doc1 = Documentair("Habbat", "11/11/2023")
doc2 = Documentair("Road to berlin", "12/1/2024" )
doc3 = Exemplaire("ALL OR NOTHING ", "01/10/2022", 12, "09/11/2023")
doc4 = Exemplaire("ALL OR NOTHING ", "01/10/2022", 13, "09/11/2023")
print(doc1.ToString()) 
print("--------------")
print(doc1.Equal(doc2))
print("---------------")
print(doc3.ToString())
print("---------------")
print(doc3.Equal(doc4))

