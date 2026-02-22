import csv
import os

FILENAME = "produits.csv"
FIELDS = ["id", "nom", "description", "prix", "quantite"]

def charger_produits():
    """Reads products from the CSV file."""
    produits = []
    if not os.path.exists(FILENAME):
        return produits
    
    with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric types for professional data handling
            row['prix'] = float(row['prix'])
            row['quantite'] = int(row['quantite'])
            produits.append(row)
    return produits

def sauvegarder_produits(produits):
    """Writes the list of products to the CSV file."""
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(produits)
    print(f"Données enregistrées dans {FILENAME}.")

def ajouter_produit():
    """Interactively adds a new product with ID validation."""
    produits_existants = charger_produits()
    ids_existantes = [p['id'] for p in produits_existants]

    print("\n--- Ajouter un nouveau produit ---")
    new_id = input("ID du produit: ")
    
    if new_id in ids_existantes:
        print("Erreur: Ce produit existe déjà.")
        return

    nouveau = {
        "id": new_id,
        "nom": input("Nom: "),
        "description": input("Description: "),
        "prix": float(input("Prix: ")),
        "quantite": int(input("Quantité: "))
    }
    
    produits_existants.append(nouveau)
    sauvegarder_produits(produits_existants)

def afficher_inventaire():
    """Displays all products in a formatted layout."""
    produits = charger_produits()
    print("\n--- Inventaire Actuel ---")
    for p in produits:
        print(f"ID: {p['id']} | {p['nom']} | {p['prix']}€ | Stock: {p['quantite']}")