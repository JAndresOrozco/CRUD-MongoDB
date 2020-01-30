from produit import produit 
from pymongo import MongoClient
MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
db = client['prueba']
collection = db['produits'] 

app = produit() 
# app.créer(collection)
# app.supprimer(collection)
app.mettreàjour(collection)