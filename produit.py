
class produit():
    
    def créer(self, collection):
    
        collection.insert_one({"_id": 1,"prenom": "t-shirt", "prix": 350})
        produit_un = {"_id": 2,"prenom": "chaussures", "prix": 200}
        produit_deux = {"_id": 3,"prenom": "lunettes", "prix": 400}
        collection.insert_many([produit_un,produit_deux])

    def mettreàjour(self, collection):
        collection.update_one({"prenom": "t-shirt"},
            {"$set":
                {
                    "prenom": "t-shirt",
                    "prix": 1000
                }
            }) 

    def supprimer(self, collection):
    
        collection.delete_one({"prenom": "chaussures"})
        résultats = collection.find()

        for résultat in résultats:
            print(résultat['prenom'])

    