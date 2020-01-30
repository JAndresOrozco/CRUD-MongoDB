from produit import produit 
from pymongo import MongoClient
from menu import Menu
MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
db = client['prueba']
collection = db['produits'] 

app = Menu()
app.menu(collection)
# # app.créer(collection)
# # app.supprimer(collection)
# app.mettreàjour(collection)