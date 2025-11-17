error = 405

# if error == 500:
#     print("Erreur serveur")
# elif error == 400: 
#     print("Mauvaise requête")
# elif error == 404 or error == 406 or error == 405: 
#     print("Resource non trouvée")
# else: 
#     print("Erreur inconnue")

match error: 
    case 500: 
       print("Erreur serveur")
    case 400: 
        print("Mauvaise requête")
    case 404 | 406 | 405:
        print("Ressource non trouvée")
    case _: 
        print("Erreur inconnue")