
class produit():
    
    def créer(self, collection):
        option = input("Vous voulez entrer un produit?" "Oui/Non \n")

        while not option == 'Non':
            prenom = input("Entrez un produit: \n")
            prix = float(input("Entrez un prix: \n"))
            collection.insert_one({"prenom" : prenom , "prix" : prix })

            option = input("Vous voulez entrer un nouveau produit?" "Oui/Non \n")



    def mettreàjour(self, collection):
        option = input("Vous voulez mettre à jour un produit?" "Oui/Non \n")
        while not option == 'Non':
            prenomChanger = input("Entrez le produit: \n")
            prenom = input("Entrez un nouveau produit: \n")
            prix = float(input("Entrez un nouveau prix: \n"))
            collection.update_one({"prenom": prenomChanger},
                {"$set":
                    {
                        
                        "prenom": prenom,
                        "prix": prix
                    }
                }) 
            print('Enregistrement mis à jour')
            option = input("Vous voulez mettre à jour un nouveau produit?" "Oui/Non \n")

    def supprimer(self, collection):
        option = input("Vous voulez supprimer un produit?" "Oui/Non \n")
        while not option == 'Non':
            prenomSupprimer = input("Entrez le produit: \n")
            collection.delete_one({"prenom": prenomSupprimer})
            print("Enregistrement supprimé")
            option = input("Vous voulez supprimer un nouveau produit?" "Oui/Non \n")
        
            

    