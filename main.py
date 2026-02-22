import inventory

def gerer_personnel():
    """Personnel Management logic (Parts 1 & 2)."""
    # Initial list of people [cite: 11]
    personnes = [
        ("Ahmed", "Ahmadi", 26), ("Salma", "Salimi", 19),
        ("Amin", "Amini", 17), ("Zahra", "Zahiri", 30),
        ("Sami", "Raqutti", 41), ("Yassine", "Yassini", 18)
    ]

    print("\n--- Gestion du Personnel ---")
    # Calculate average age [cite: 12]
    avg = sum(p[2] for p in personnes) / len(personnes)
    print(f"Moyenne d'âge: {avg:.2f} ans")

    # Filter adults [cite: 14]
    majeurs = [p[1] for p in personnes if p[2] >= 18]
    print(f"Membres majeurs: {', '.join(majeurs)}")

def menu_principal():
    while True:
        print("\n==============================")
        print("   SYSTÈME DE GESTION V1.0")
        print("==============================")
        print("1. Afficher l'Inventaire (CSV)")
        print("2. Ajouter un Produit (CSV)")
        print("3. Statistiques du Personnel")
        print("4. Quitter")
        
        choix = input("\nChoisissez une option: ")
        
        if choix == '1':
            inventory.afficher_inventaire()
        elif choix == '2':
            inventory.ajouter_produit()
        elif choix == '3':
            gerer_personnel()
        elif choix == '4':
            print("Fermeture du programme...")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    menu_principal()