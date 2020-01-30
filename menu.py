from produit import produit 
class menu():

    def __init__(self):
        self.produits = produit() 

    def menu(self):
        print("Menu")
        print('1. Créer un produit')
        print('2. Mettre à jour un produit')
        print('3. Supprimer un produit')
        print("Qu'est-ce que vous voulez faire?")