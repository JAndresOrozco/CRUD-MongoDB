from produit import produit 
class Menu():

    def __init__(self):
        self.produit = produit() 

    def menu(self, collection):
        print("--------Menu-------")
        print('1. Créer un produit')
        print('2. Mettre à jour un produit')
        print('3. Supprimer un produit')
        print('4. Sortir')
        option = input("Qu'est-ce que vous voulez faire? \n")
        if(option == '1'):
            self.produit.créer(collection)
            self.menu(collection)
        
        if(option == '2'):
            self.produit.mettreàjour(collection)
            self.menu(collection)

        if(option == '3'):
            self.produit.supprimer(collection)
            self.menu(collection)
        