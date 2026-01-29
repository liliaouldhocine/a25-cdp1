def calcularice():
    """
    Fonction principale de la calculatrice
    """
    print("=== CALCULATRICE SIMPLE ===")
    
    while True:
        # Afficher le menu
        print("\nOpérations disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quitter")

        try: 
            choix = input("Quel est votre choix (1-5) : ")
            if choix == '5':
                print("Merci d'avoir utilisé la calculatrice. Au revoir !")
                break;

            if choix not in ['1', '2', '3', '4']:
                raise ValueError("Choix invalide. Veuillez entrer un nombre entre 1 et 5")
            
            try : 
                num1 = float(input("Entrez le premier nombre : "))
                num2 = float(input("Entrez le deuxième nombre : "))
            except ValueError: 
                raise ValueError("Veuillez entrer un nombre valide.")
            
            if choix == '1': # addition
                resultat = num1 + num2
                operateur = "+"
            elif choix == '2':  # soustraction
                resultat = num1 - num2
                operateur = "-"
            elif choix == '3':  # multiplication
                resultat = num1 * num2
                operateur = "*"
            elif choix == '4':  # division
                if num2 == 0:
                    raise ZeroDivisionError("Division par zéro est impossible ! ")
                resultat = num1 / num2
                operateur = "/"
        
            # affichage du resultat 
            print(f"Résultat : {num1} {operateur} {num2} = {resultat}")
            
        except ValueError as ve : 
            print(f"Erreur : {ve}")
        except ZeroDivisionError as zde: 
            print(f"Erreur: {zde}")
        except Exception as e: 
            print(f"Erreur inattendue : {e}")


calcularice()