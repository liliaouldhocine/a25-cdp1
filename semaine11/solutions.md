## **Exercice 1 : Gestionnaire de Contacts**

```python
"""
Gestionnaire de Contacts
Solution complète
"""

class ContactError(Exception):
    """Base exception pour les erreurs de contact"""
    pass

class ContactExisteDejaError(ContactError):
    pass

class ContactNonTrouveError(ContactError):
    pass

class FormatTelephoneError(ContactError):
    pass

class FormatEmailError(ContactError):
    pass

class GestionnaireContacts:
    def __init__(self):
        self.contacts = {}

    def valider_telephone(self, telephone):
        """Valide le format du téléphone (10 chiffres)"""
        telephone = telephone.strip()

        if not telephone.isdigit():
            raise FormatTelephoneError("Le téléphone doit contenir uniquement des chiffres")

        if len(telephone) != 10:
            raise FormatTelephoneError("Le téléphone doit avoir 10 chiffres")

        return True

    def valider_email(self, email):
        """Valide le format de l'email"""
        email = email.strip()

        if '@' not in email:
            raise FormatEmailError("Email invalide: doit contenir '@'")

        if '.' not in email:
            raise FormatEmailError("Email invalide: doit contenir '.'")

        if email.count('@') != 1:
            raise FormatEmailError("Email invalide: doit contenir exactement un '@'")

        # Vérifier que @ n'est pas au début ou à la fin
        if email.startswith('@') or email.endswith('@'):
            raise FormatEmailError("Email invalide: '@' ne peut pas être au début ou à la fin")

        # Vérifier qu'il y a un point après le @
        partie_apres_arobase = email.split('@')[1]
        if '.' not in partie_apres_arobase:
            raise FormatEmailError("Email invalide: doit contenir un '.' après le '@'")

        return True

    def ajouter_contact(self, nom, telephone, email):
        """Ajoute un nouveau contact"""
        try:
            # Validation des entrées
            nom = nom.strip()
            if not nom:
                raise ValueError("Le nom ne peut pas être vide")

            self.valider_telephone(telephone)
            self.valider_email(email)

            # Vérifier si le contact existe déjà
            if nom in self.contacts:
                raise ContactExisteDejaError(f"Le contact '{nom}' existe déjà")

            # Ajouter le contact
            self.contacts[nom] = {
                'telephone': telephone,
                'email': email
            }
            print(f"Contact '{nom}' ajouté avec succès!")

        except (ValueError, FormatTelephoneError, FormatEmailError) as e:
            raise ContactError(f"Impossible d'ajouter le contact: {e}")

    def rechercher_contact(self, nom):
        """Recherche un contact par nom"""
        nom = nom.strip()

        if nom in self.contacts:
            contact = self.contacts[nom]
            print(f"\nContact trouvé:")
            print(f"  Nom: {nom}")
            print(f"  Téléphone: {contact['telephone']}")
            print(f"  Email: {contact['email']}")
            return contact
        else:
            raise ContactNonTrouveError(f"Contact '{nom}' non trouvé")

    def supprimer_contact(self, nom):
        """Supprime un contact"""
        nom = nom.strip()

        if nom in self.contacts:
            del self.contacts[nom]
            print(f"Contact '{nom}' supprimé avec succès!")
        else:
            raise ContactNonTrouveError(f"Contact '{nom}' non trouvé")

    def afficher_contacts(self):
        """Affiche tous les contacts"""
        if not self.contacts:
            print("Aucun contact enregistré.")
            return

        print(f"\n=== LISTE DES CONTACTS ({len(self.contacts)}) ===")
        for nom, infos in self.contacts.items():
            print(f"\nNom: {nom}")
            print(f"  Téléphone: {infos['telephone']}")
            print(f"  Email: {infos['email']}")

    def sauvegarder(self, nom_fichier="contacts.txt"):
        """Sauvegarde les contacts dans un fichier"""
        try:
            with open(nom_fichier, 'w', encoding='utf-8') as f:
                for nom, infos in self.contacts.items():
                    ligne = f"{nom}|{infos['telephone']}|{infos['email']}\n"
                    f.write(ligne)

            print(f"Contacts sauvegardés dans '{nom_fichier}'")

        except PermissionError:
            raise ContactError(f"Permission refusée pour écrire dans '{nom_fichier}'")
        except Exception as e:
            raise ContactError(f"Erreur lors de la sauvegarde: {e}")

    def charger(self, nom_fichier="contacts.txt"):
        """Charge les contacts depuis un fichier"""
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                lignes = f.readlines()

            contacts_charges = 0
            for ligne in lignes:
                ligne = ligne.strip()
                if ligne:  # Ignorer les lignes vides
                    try:
                        parties = ligne.split('|')
                        if len(parties) == 3:
                            nom, telephone, email = parties
                            self.contacts[nom] = {
                                'telephone': telephone,
                                'email': email
                            }
                            contacts_charges += 1
                        else:
                            print(f"Format invalide ignoré: {ligne}")
                    except Exception as e:
                        print(f"Erreur lors du chargement de la ligne: {ligne} - {e}")

            print(f"{contacts_charges} contacts chargés depuis '{nom_fichier}'")

        except FileNotFoundError:
            print(f"Fichier '{nom_fichier}' non trouvé. Démarrage avec une liste vide.")
        except PermissionError:
            raise ContactError(f"Permission refusée pour lire '{nom_fichier}'")
        except Exception as e:
            raise ContactError(f"Erreur lors du chargement: {e}")

def menu():
    """Menu principal"""
    gestionnaire = GestionnaireContacts()

    # Charger les contacts existants
    try:
        gestionnaire.charger()
    except ContactError as e:
        print(f"Avertissement: {e}")

    while True:
        print("\n=== GESTIONNAIRE DE CONTACTS ===")
        print("1. Ajouter un contact")
        print("2. Rechercher un contact")
        print("3. Supprimer un contact")
        print("4. Afficher tous les contacts")
        print("5. Sauvegarder les contacts")
        print("6. Charger les contacts")
        print("7. Quitter")

        choix = input("Votre choix (1-7): ").strip()

        if choix == '1':
            try:
                nom = input("Nom: ")
                telephone = input("Téléphone (10 chiffres): ")
                email = input("Email: ")
                gestionnaire.ajouter_contact(nom, telephone, email)
            except ContactError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '2':
            try:
                nom = input("Nom à rechercher: ")
                gestionnaire.rechercher_contact(nom)
            except ContactNonTrouveError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '3':
            try:
                nom = input("Nom à supprimer: ")
                gestionnaire.supprimer_contact(nom)
            except ContactNonTrouveError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '4':
            gestionnaire.afficher_contacts()

        elif choix == '5':
            try:
                nom_fichier = input("Nom du fichier (défaut: contacts.txt): ").strip()
                if not nom_fichier:
                    nom_fichier = "contacts.txt"
                gestionnaire.sauvegarder(nom_fichier)
            except ContactError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '6':
            try:
                nom_fichier = input("Nom du fichier (défaut: contacts.txt): ").strip()
                if not nom_fichier:
                    nom_fichier = "contacts.txt"

                # Demander confirmation si des contacts existent déjà
                if gestionnaire.contacts:
                    confirmation = input("Cela écrasera les contacts actuels. Continuer? (o/n): ")
                    if confirmation.lower() != 'o':
                        print("Chargement annulé.")
                        continue

                gestionnaire.charger(nom_fichier)
            except ContactError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '7':
            # Sauvegarder avant de quitter
            try:
                sauvegarder = input("Sauvegarder les contacts avant de quitter? (o/n): ")
                if sauvegarder.lower() == 'o':
                    gestionnaire.sauvegarder()
            except ContactError as e:
                print(f"Erreur lors de la sauvegarde: {e}")

            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 7.")

if __name__ == "__main__":
    menu()
```

---

## **Exercice 3 : Système de Réservation de Salles**

```python
"""
Système de Réservation de Salles
Solution complète
"""

from datetime import datetime, timedelta

class ReservationError(Exception):
    pass

class SalleIndisponibleError(ReservationError):
    pass

class DateInvalideError(ReservationError):
    pass

class DureeInvalideError(ReservationError):
    pass

class SalleInexistanteError(ReservationError):
    pass

class Reservation:
    def __init__(self, salle, date_debut, duree_heures, utilisateur):
        self.salle = salle
        self.date_debut = date_debut
        self.duree_heures = duree_heures
        self.utilisateur = utilisateur
        self.date_fin = date_debut + timedelta(hours=duree_heures)
        self.id = id(self)  # ID unique simple

    def chevauche(self, autre_reservation):
        """Vérifie si deux réservations se chevauchent"""
        if self.salle != autre_reservation.salle:
            return False

        # Vérifier si les plages de temps se chevauchent
        deb1, fin1 = self.date_debut, self.date_fin
        deb2, fin2 = autre_reservation.date_debut, autre_reservation.date_fin

        return not (fin1 <= deb2 or fin2 <= deb1)

    def __str__(self):
        return (f"Réservation {self.id}: {self.salle} "
                f"le {self.date_debut.strftime('%d/%m/%Y %H:%M')} "
                f"({self.duree_heures}h) par {self.utilisateur}")

class Salle:
    def __init__(self, nom, capacite):
        self.nom = nom
        self.capacite = capacite
        self.reservations = []

    def est_disponible(self, date_debut, duree_heures):
        """Vérifie si la salle est disponible pour une plage horaire"""
        # Créer une réservation temporaire pour le test
        reservation_test = Reservation(self.nom, date_debut, duree_heures, "test")

        # Vérifier les chevauchements avec les réservations existantes
        for reservation in self.reservations:
            if reservation.chevauche(reservation_test):
                return False

        return True

    def ajouter_reservation(self, reservation):
        """Ajoute une réservation à la salle"""
        if not self.est_disponible(reservation.date_debut, reservation.duree_heures):
            raise SalleIndisponibleError(
                f"La salle {self.nom} n'est pas disponible à cette date/heure"
            )

        self.reservations.append(reservation)
        return True

    def annuler_reservation(self, reservation_id):
        """Annule une réservation par son ID"""
        for i, reservation in enumerate(self.reservations):
            if reservation.id == reservation_id:
                del self.reservations[i]
                return True

        return False

    def afficher_reservations(self):
        """Affiche toutes les réservations de la salle"""
        if not self.reservations:
            print(f"Aucune réservation pour la salle {self.nom}")
            return

        print(f"\n=== RÉSERVATIONS POUR {self.nom} ({len(self.reservations)}) ===")
        for reservation in sorted(self.reservations, key=lambda r: r.date_debut):
            print(f"  - {reservation}")

class SystemeReservation:
    def __init__(self):
        self.salles = {}
        self.reservations = []
        self.reservation_id_counter = 1

    def ajouter_salle(self, nom, capacite):
        """Ajoute une nouvelle salle au système"""
        if nom in self.salles:
            print(f"La salle '{nom}' existe déjà.")
            return False

        self.salles[nom] = Salle(nom, capacite)
        print(f"Salle '{nom}' (capacité: {capacite}) ajoutée avec succès.")
        return True

    def reserver_salle(self, nom_salle, date_str, heure_str, duree, utilisateur):
        """Réserve une salle pour une date, heure et durée données"""
        try:
            # Validation des entrées
            if nom_salle not in self.salles:
                raise SalleInexistanteError(f"La salle '{nom_salle}' n'existe pas.")

            if duree <= 0 or duree > 12:
                raise DureeInvalideError("La durée doit être entre 1 et 12 heures.")

            # Parser la date et l'heure
            try:
                date_heure_str = f"{date_str} {heure_str}"
                date_debut = datetime.strptime(date_heure_str, "%d/%m/%Y %H:%M")
            except ValueError:
                raise DateInvalideError("Format de date/heure invalide. Utilisez JJ/MM/AAAA HH:MM")

            # Vérifier que la date n'est pas dans le passé
            maintenant = datetime.now()
            if date_debut < maintenant:
                raise DateInvalideError("Impossible de réserver dans le passé.")

            # Vérifier la disponibilité
            salle = self.salles[nom_salle]
            if not salle.est_disponible(date_debut, duree):
                raise SalleIndisponibleError(
                    f"La salle '{nom_salle}' n'est pas disponible à cette date/heure."
                )

            # Créer et ajouter la réservation
            reservation = Reservation(nom_salle, date_debut, duree, utilisateur)
            salle.ajouter_reservation(reservation)
            self.reservations.append(reservation)

            print(f"Réservation confirmée!")
            print(f"  Salle: {nom_salle}")
            print(f"  Date: {date_debut.strftime('%d/%m/%Y %H:%M')}")
            print(f"  Durée: {duree} heures")
            print(f"  Utilisateur: {utilisateur}")
            print(f"  ID de réservation: {reservation.id}")

            return reservation.id

        except (SalleInexistanteError, DateInvalideError,
                DureeInvalideError, SalleIndisponibleError) as e:
            raise
        except Exception as e:
            raise ReservationError(f"Erreur lors de la réservation: {e}")

    def annuler_reservation(self, reservation_id):
        """Annule une réservation par son ID"""
        try:
            reservation_id = int(reservation_id)

            # Trouver la réservation
            reservation_a_annuler = None
            for reservation in self.reservations:
                if reservation.id == reservation_id:
                    reservation_a_annuler = reservation
                    break

            if not reservation_a_annuler:
                raise ReservationError(f"Réservation {reservation_id} non trouvée.")

            # Annuler dans la salle
            salle = self.salles[reservation_a_annuler.salle]
            if not salle.annuler_reservation(reservation_id):
                raise ReservationError(f"Erreur lors de l'annulation dans la salle.")

            # Supprimer de la liste globale
            self.reservations = [r for r in self.reservations if r.id != reservation_id]

            print(f"Réservation {reservation_id} annulée avec succès.")
            return True

        except ValueError:
            raise ReservationError("ID de réservation invalide.")
        except KeyError:
            raise ReservationError("Salle non trouvée pour cette réservation.")
        except Exception as e:
            raise ReservationError(f"Erreur lors de l'annulation: {e}")

    def afficher_reservations_salle(self, nom_salle):
        """Affiche toutes les réservations d'une salle"""
        if nom_salle not in self.salles:
            print(f"La salle '{nom_salle}' n'existe pas.")
            return

        self.salles[nom_salle].afficher_reservations()

    def afficher_reservations_date(self, date_str):
        """Affiche toutes les réservations d'une date spécifique"""
        try:
            date_recherche = datetime.strptime(date_str, "%d/%m/%Y")

            reservations_date = []
            for reservation in self.reservations:
                if reservation.date_debut.date() == date_recherche.date():
                    reservations_date.append(reservation)

            if not reservations_date:
                print(f"Aucune réservation trouvée pour le {date_str}")
                return

            print(f"\n=== RÉSERVATIONS DU {date_str} ({len(reservations_date)}) ===")
            for reservation in sorted(reservations_date, key=lambda r: r.date_debut):
                print(f"  - {reservation}")

        except ValueError:
            print("Format de date invalide. Utilisez JJ/MM/AAAA")

def menu_reservation():
    """Menu du système de réservation"""
    systeme = SystemeReservation()

    # Ajouter quelques salles par défaut
    salles_par_defaut = [
        ("Salle A", 20),
        ("Salle B", 30),
        ("Salle C", 50),
        ("Salle de Réunion", 10)
    ]

    for nom, capacite in salles_par_defaut:
        systeme.ajouter_salle(nom, capacite)

    while True:
        print("\n=== SYSTÈME DE RÉSERVATION DE SALLES ===")
        print("1. Réserver une salle")
        print("2. Annuler une réservation")
        print("3. Afficher les réservations d'une salle")
        print("4. Afficher les réservations d'une date")
        print("5. Ajouter une nouvelle salle")
        print("6. Quitter")

        choix = input("Votre choix: ").strip()

        if choix == '1':
            try:
                nom_salle = input("Nom de la salle: ").strip()
                date_str = input("Date (JJ/MM/AAAA): ").strip()
                heure_str = input("Heure de début (HH:MM): ").strip()
                duree = float(input("Durée (heures): ").strip())
                utilisateur = input("Votre nom: ").strip()

                systeme.reserver_salle(nom_salle, date_str, heure_str, duree, utilisateur)

            except (SalleIndisponibleError, DateInvalideError,
                    DureeInvalideError, SalleInexistanteError) as e:
                print(f"Erreur de réservation: {e}")
            except ValueError:
                print("Erreur: Durée invalide.")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '2':
            try:
                reservation_id = input("ID de la réservation à annuler: ").strip()
                systeme.annuler_reservation(reservation_id)
            except ReservationError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '3':
            nom_salle = input("Nom de la salle: ").strip()
            systeme.afficher_reservations_salle(nom_salle)

        elif choix == '4':
            date_str = input("Date (JJ/MM/AAAA): ").strip()
            systeme.afficher_reservations_date(date_str)

        elif choix == '5':
            nom_salle = input("Nom de la nouvelle salle: ").strip()
            try:
                capacite = int(input("Capacité: ").strip())
                if capacite <= 0:
                    print("Erreur: La capacité doit être positive.")
                else:
                    systeme.ajouter_salle(nom_salle, capacite)
            except ValueError:
                print("Erreur: Capacité invalide.")

        elif choix == '6':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 6.")

if __name__ == "__main__":
    menu_reservation()
```

---

## **Exercice 4 : Quiz Interactif avec Score**

```python
"""
Quiz Interactif avec Score
Solution complète
"""

import random
import time

class QuizError(Exception):
    pass

class FormatQuestionError(QuizError):
    pass

class FichierQuizError(QuizError):
    pass

class Question:
    def __init__(self, texte, options, reponse_correcte):
        self.texte = texte
        self.options = options
        self.reponse_correcte = reponse_correcte  # Index 0-based

    def poser(self):
        """Pose la question et retourne True si réponse correcte"""
        print(f"\n{self.texte}")

        for i, option in enumerate(self.options, 1):
            print(f"  {i}. {option}")

        while True:
            try:
                choix = input(f"Votre réponse (1-{len(self.options)}): ").strip()
                if not choix:
                    continue

                choix_int = int(choix) - 1  # Convertir en index 0-based

                if 0 <= choix_int < len(self.options):
                    return self.verifier_reponse(choix_int)
                else:
                    print(f"Veuillez choisir un nombre entre 1 et {len(self.options)}")

            except ValueError:
                print("Veuillez entrer un nombre valide.")
            except Exception as e:
                print(f"Erreur: {e}")

    def verifier_reponse(self, reponse_utilisateur):
        """Vérifie si la réponse est correcte"""
        return reponse_utilisateur == self.reponse_correcte

    def __str__(self):
        return f"Q: {self.texte} | R: {self.options[self.reponse_correcte]}"

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.temps_total = 0
        self.reponses = []  # Pour stocker les réponses données

    def charger_questions(self, nom_fichier="questions.txt"):
        """Charge les questions depuis un fichier"""
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                lignes = f.readlines()

            if not lignes:
                raise FichierQuizError("Le fichier de questions est vide")

            questions_chargees = 0
            for i, ligne in enumerate(lignes, 1):
                try:
                    ligne = ligne.strip()
                    if not ligne or ligne.startswith('#'):  # Ignorer lignes vides et commentaires
                        continue

                    parties = ligne.split('|')
                    if len(parties) != 6:
                        raise FormatQuestionError(
                            f"Format invalide à la ligne {i}: attendu 6 parties, obtenu {len(parties)}"
                        )

                    texte = parties[0].strip()
                    options = [opt.strip() for opt in parties[1:5]]
                    reponse_correcte = int(parties[5].strip()) - 1  # Convertir en index 0-based

                    # Validation
                    if not texte:
                        raise FormatQuestionError(f"Texte vide à la ligne {i}")

                    if len(options) != 4:
                        raise FormatQuestionError(f"4 options requises à la ligne {i}")

                    if any(not opt for opt in options):
                        raise FormatQuestionError(f"Option vide à la ligne {i}")

                    if not (0 <= reponse_correcte < 4):
                        raise FormatQuestionError(
                            f"Réponse invalide à la ligne {i}: doit être entre 1 et 4"
                        )

                    question = Question(texte, options, reponse_correcte)
                    self.questions.append(question)
                    questions_chargees += 1

                except ValueError as e:
                    raise FormatQuestionError(f"Erreur de valeur à la ligne {i}: {e}")
                except Exception as e:
                    raise FormatQuestionError(f"Erreur à la ligne {i}: {e}")

            if questions_chargees == 0:
                raise FichierQuizError("Aucune question valide trouvée dans le fichier")

            print(f"{questions_chargees} questions chargées avec succès!")

        except FileNotFoundError:
            raise FichierQuizError(f"Fichier '{nom_fichier}' non trouvé")
        except PermissionError:
            raise FichierQuizError(f"Permission refusée pour lire '{nom_fichier}'")
        except Exception as e:
            raise FichierQuizError(f"Erreur lors du chargement: {e}")

    def demarrer(self):
        """Démarre le quiz"""
        if not self.questions:
            raise QuizError("Aucune question disponible. Chargez d'abord des questions.")

        # Mélanger les questions
        questions_melangees = self.questions.copy()
        random.shuffle(questions_melangees)

        print(f"\n=== DÉBUT DU QUIZ ({len(questions_melangees)} questions) ===")
        print("Répondez aux questions en entrant le numéro de la réponse.")
        input("Appuyez sur Entrée pour commencer...")

        debut = time.time()

        for i, question in enumerate(questions_melangees, 1):
            print(f"\n--- Question {i}/{len(questions_melangees)} ---")

            debut_question = time.time()
            correcte = question.poser()
            temps_question = time.time() - debut_question

            if correcte:
                print("✓ Correct!")
                self.score += 1
            else:
                print(f"✗ Incorrect. La bonne réponse était: {question.options[question.reponse_correcte]}")

            # Stocker la réponse
            self.reponses.append({
                'question': question.texte,
                'temps': temps_question,
                'correcte': correcte
            })

            time.sleep(1)  # Pause courte entre les questions

        self.temps_total = time.time() - debut

    def afficher_resultat(self):
        """Affiche le résultat final"""
        if not self.reponses:
            print("Aucun résultat à afficher.")
            return

        total = len(self.reponses)
        pourcentage = (self.score / total) * 100 if total > 0 else 0

        print("\n" + "="*50)
        print("=== RÉSULTATS DU QUIZ ===")
        print("="*50)
        print(f"Score: {self.score}/{total} ({pourcentage:.1f}%)")
        print(f"Temps total: {self.temps_total:.1f} secondes")
        print(f"Temps moyen par question: {self.temps_total/total:.1f} secondes")

        # Afficher les questions avec les réponses
        print("\n--- DÉTAIL DES RÉPONSES ---")
        for i, reponse in enumerate(self.reponses, 1):
            statut = "✓" if reponse['correcte'] else "✗"
            print(f"{i:2d}. {statut} {reponse['question'][:50]}... ({reponse['temps']:.1f}s)")

    def sauvegarder_resultat(self, nom_utilisateur):
        """Sauvegarde le résultat dans un fichier"""
        try:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            nom_fichier = f"resultat_{nom_utilisateur}_{timestamp}.txt"

            with open(nom_fichier, 'w', encoding='utf-8') as f:
                f.write(f"RÉSULTAT DU QUIZ - {nom_utilisateur}\n")
                f.write(f"Date: {time.strftime('%d/%m/%Y %H:%M:%S')}\n")
                f.write("="*50 + "\n\n")

                total = len(self.reponses)
                pourcentage = (self.score / total) * 100 if total > 0 else 0

                f.write(f"SCORE FINAL: {self.score}/{total} ({pourcentage:.1f}%)\n")
                f.write(f"TEMPS TOTAL: {self.temps_total:.1f} secondes\n\n")

                f.write("DÉTAIL DES QUESTIONS:\n")
                f.write("-"*50 + "\n")

                for i, reponse in enumerate(self.reponses, 1):
                    statut = "CORRECT" if reponse['correcte'] else "INCORRECT"
                    f.write(f"\nQUESTION {i} ({statut}, {reponse['temps']:.1f}s):\n")
                    f.write(f"  {reponse['question']}\n")

            print(f"Résultat sauvegardé dans '{nom_fichier}'")

        except Exception as e:
            raise QuizError(f"Erreur lors de la sauvegarde: {e}")

def creer_fichier_questions_exemple():
    """Crée un fichier exemple de questions"""
    questions = [
        "Quelle est la capitale de la France?|Paris|Londres|Berlin|Madrid|1",
        "Combien font 2 + 2?|3|4|5|6|2",
        "Quel langage de programmation utilise 'print'?|Java|C++|Python|JavaScript|3",
        "Quelle planète est appelée 'Planète Rouge'?|Venus|Mars|Jupiter|Saturne|2",
        "Qui a peint la Joconde?|Van Gogh|Picasso|Leonard de Vinci|Michel-Ange|3",
        "Quelle est la plus grande planète du système solaire?|Terre|Mars|Jupiter|Saturne|3",
        "En quelle année a été fondée l'ONU?|1945|1918|1950|1939|1",
        "Quel est le symbole chimique de l'or?|Ag|Fe|Au|Pb|3",
        "Combien de continents y a-t-il sur Terre?|5|6|7|8|3",
        "Quel animal est le plus rapide?|Guépard|Lion|Éléphant|Tortue|1"
    ]

    try:
        with open("questions.txt", "w", encoding="utf-8") as f:
            f.write("# Fichier de questions pour le quiz\n")
            f.write("# Format: question|option1|option2|option3|option4|numero_reponse_correcte\n\n")
            for question in questions:
                f.write(question + "\n")
        print("Fichier de questions exemple créé avec succès!")
        print("10 questions disponibles.")
    except Exception as e:
        print(f"Erreur lors de la création du fichier: {e}")

def menu_quiz():
    """Menu du quiz"""
    quiz = Quiz()

    print("=== QUIZ INTERACTIF ===")

    while True:
        print("\nMenu Principal:")
        print("1. Charger des questions")
        print("2. Démarrer le quiz")
        print("3. Afficher les résultats")
        print("4. Sauvegarder les résultats")
        print("5. Créer un fichier de questions exemple")
        print("6. Quitter")

        choix = input("Votre choix (1-6): ").strip()

        if choix == '1':
            nom_fichier = input("Nom du fichier (défaut: questions.txt): ").strip()
            if not nom_fichier:
                nom_fichier = "questions.txt"

            try:
                quiz.charger_questions(nom_fichier)
            except FichierQuizError as e:
                print(f"Erreur: {e}")
                creer_fichier = input("Créer un fichier exemple? (o/n): ")
                if creer_fichier.lower() == 'o':
                    creer_fichier_questions_exemple()
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '2':
            if not quiz.questions:
                print("Veuillez d'abord charger des questions.")
                continue

            try:
                quiz.demarrer()
            except QuizError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '3':
            quiz.afficher_resultat()

        elif choix == '4':
            if not quiz.reponses:
                print("Aucun résultat à sauvegarder. Faites d'abord un quiz.")
                continue

            nom_utilisateur = input("Votre nom: ").strip()
            if not nom_utilisateur:
                nom_utilisateur = "Anonyme"

            try:
                quiz.sauvegarder_resultat(nom_utilisateur)
            except QuizError as e:
                print(f"Erreur: {e}")
            except Exception as e:
                print(f"Erreur inattendue: {type(e).__name__}: {e}")

        elif choix == '5':
            creer_fichier_questions_exemple()

        elif choix == '6':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 6.")

if __name__ == "__main__":
    menu_quiz()
```

---

## **Exercice 5 : Convertisseur d'Unités**

```python
"""
Convertisseur d'Unités
Solution complète
"""

class ConversionError(Exception):
    pass

class UniteInvalideError(ConversionError):
    pass

class ValeurInvalideError(ConversionError):
    pass

class Convertisseur:
    # Taux de conversion pour la monnaie (simulé)
    TAUX_MONNAIE = {
        'USD_EUR': 0.85,
        'EUR_USD': 1.18,
        'USD_GBP': 0.73,
        'GBP_USD': 1.37,
        'EUR_GBP': 0.86,
        'GBP_EUR': 1.16,
        'USD_CAD': 1.25,
        'CAD_USD': 0.80,
        'EUR_CAD': 1.46,
        'CAD_EUR': 0.68
    }

    # Unités valides par catégorie
    UNITES = {
        'temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
        'distance': ['Mètres', 'Kilomètres', 'Miles', 'Pieds'],
        'poids': ['Grammes', 'Kilogrammes', 'Livres', 'Onces'],
        'monnaie': ['USD', 'EUR', 'GBP', 'CAD']
    }

    def valider_valeur(self, valeur_str):
        """Valide et convertit une valeur en float"""
        try:
            valeur = float(valeur_str)
            return valeur
        except ValueError:
            raise ValeurInvalideError(f"Valeur invalide: '{valeur_str}'")

    def valider_unite(self, unite, categorie):
        """Valide si l'unité existe dans la catégorie"""
        unite = unite.strip()

        # Vérifier si l'unité existe dans la catégorie
        if unite not in self.UNITES[categorie]:
            # Essayer une correspondance insensible à la casse
            for unite_valide in self.UNITES[categorie]:
                if unite.lower() == unite_valide.lower():
                    return unite_valide

            # Si aucune correspondance, lever une exception
            unites_valides = ', '.join(self.UNITES[categorie])
            raise UniteInvalideError(
                f"Unité '{unite}' invalide pour {categorie}. "
                f"Unités valides: {unites_valides}"
            )

        return unite

    def convertir_temperature(self, valeur, source, cible):
        """Convertit entre Celsius, Fahrenheit et Kelvin"""
        # Conversion vers Celsius (référence commune)
        if source == 'Celsius':
            celsius = valeur
        elif source == 'Fahrenheit':
            celsius = (valeur - 32) * 5/9
        elif source == 'Kelvin':
            celsius = valeur - 273.15
        else:
            raise UniteInvalideError(f"Unité source invalide: {source}")

        # Conversion depuis Celsius vers l'unité cible
        if cible == 'Celsius':
            return celsius
        elif cible == 'Fahrenheit':
            return (celsius * 9/5) + 32
        elif cible == 'Kelvin':
            return celsius + 273.15
        else:
            raise UniteInvalideError(f"Unité cible invalide: {cible}")

    def convertir_distance(self, valeur, source, cible):
        """Convertit entre mètres, km, miles, pieds"""
        # Facteurs de conversion vers les mètres
        facteurs_vers_metres = {
            'Mètres': 1,
            'Kilomètres': 1000,
            'Miles': 1609.34,
            'Pieds': 0.3048
        }

        if source not in facteurs_vers_metres or cible not in facteurs_vers_metres:
            raise UniteInvalideError("Unité de distance invalide")

        # Conversion vers les mètres
        metres = valeur * facteurs_vers_metres[source]

        # Conversion depuis les mètres vers l'unité cible
        return metres / facteurs_vers_metres[cible]

    def convertir_poids(self, valeur, source, cible):
        """Convertit entre grammes, kg, livres, onces"""
        # Facteurs de conversion vers les grammes
        facteurs_vers_grammes = {
            'Grammes': 1,
            'Kilogrammes': 1000,
            'Livres': 453.592,
            'Onces': 28.3495
        }

        if source not in facteurs_vers_grammes or cible not in facteurs_vers_grammes:
            raise UniteInvalideError("Unité de poids invalide")

        # Conversion vers les grammes
        grammes = valeur * facteurs_vers_grammes[source]

        # Conversion depuis les grammes vers l'unité cible
        return grammes / facteurs_vers_grammes[cible]

    def convertir_monnaie(self, valeur, source, cible):
        """Convertit entre devises"""
        source = source.upper()
        cible = cible.upper()

        if source == cible:
            return valeur  # Même devise, pas de conversion

        # Chercher le taux de conversion direct
        cle = f"{source}_{cible}"
        if cle in self.TAUX_MONNAIE:
            return valeur * self.TAUX_MONNAIE[cle]

        # Si pas de taux direct, essayer via USD comme intermédiaire
        if source != 'USD' and cible != 'USD':
            # Conversion source -> USD -> cible
            if f"{source}_USD" in self.TAUX_MONNAIE and f"USD_{cible}" in self.TAUX_MONNAIE:
                valeur_usd = valeur * self.TAUX_MONNAIE[f"{source}_USD"]
                return valeur_usd * self.TAUX_MONNAIE[f"USD_{cible}"]

        # Si aucune conversion possible
        raise UniteInvalideError(
            f"Conversion {source} -> {cible} non supportée. "
            f"Taux disponibles: {', '.join(self.TAUX_MONNAIE.keys())}"
        )

    def convertir(self, categorie, valeur_str, source, cible):
        """Conversion principale avec gestion d'erreurs complète"""
        try:
            # Validation des entrées
            valeur = self.valider_valeur(valeur_str)

            source = self.valider_unite(source, categorie)
            cible = self.valider_unite(cible, categorie)

            # Exécuter la conversion selon la catégorie
            if categorie == 'temperature':
                resultat = self.convertir_temperature(valeur, source, cible)
            elif categorie == 'distance':
                resultat = self.convertir_distance(valeur, source, cible)
            elif categorie == 'poids':
                resultat = self.convertir_poids(valeur, source, cible)
            elif categorie == 'monnaie':
                resultat = self.convertir_monnaie(valeur, source, cible)
            else:
                raise ConversionError(f"Catégorie inconnue: {categorie}")

            # Formater le résultat
            if categorie == 'temperature':
                return f"{valeur:.2f} °{source[0]} = {resultat:.2f} °{cible[0]}"
            elif categorie == 'monnaie':
                return f"{valeur:.2f} {source} = {resultat:.2f} {cible}"
            else:
                return f"{valeur:.2f} {source} = {resultat:.4f} {cible}"

        except (ValeurInvalideError, UniteInvalideError) as e:
            raise
        except Exception as e:
            raise ConversionError(f"Erreur lors de la conversion: {e}")

def menu_convertisseur():
    """Menu du convertisseur"""
    convertisseur = Convertisseur()

    categories = {
        '1': ('temperature', 'Température', ['Celsius', 'Fahrenheit', 'Kelvin']),
        '2': ('distance', 'Distance', ['Mètres', 'Kilomètres', 'Miles', 'Pieds']),
        '3': ('poids', 'Poids', ['Grammes', 'Kilogrammes', 'Livres', 'Onces']),
        '4': ('monnaie', 'Monnaie', ['USD', 'EUR', 'GBP', 'CAD'])
    }

    while True:
        print("\n=== CONVERTISSEUR D'UNITÉS ===")
        for key, (_, nom, unites) in categories.items():
            print(f"{key}. {nom} ({', '.join(unites)})")
        print("5. Quitter")

        choix_categorie = input("Choisissez une catégorie (1-5): ").strip()

        if choix_categorie == '5':
            print("Au revoir!")
            break

        if choix_categorie not in categories:
            print("Choix invalide!")
            continue

        categorie_id, nom_categorie, unites = categories[choix_categorie]

        print(f"\n=== CONVERSION DE {nom_categorie.upper()} ===")

        try:
            # Afficher les unités disponibles
            print(f"Unités disponibles: {', '.join(unites)}")

            # Demander les valeurs
            valeur_str = input(f"Valeur à convertir: ").strip()
            source = input(f"Unité source: ").strip()
            cible = input(f"Unité cible: ").strip()

            # Effectuer la conversion
            resultat = convertisseur.convertir(categorie_id, valeur_str, source, cible)

            print(f"\nRÉSULTAT: {resultat}")

        except ValeurInvalideError as e:
            print(f"Erreur de valeur: {e}")
        except UniteInvalideError as e:
            print(f"Erreur d'unité: {e}")
        except ConversionError as e:
            print(f"Erreur de conversion: {e}")
        except Exception as e:
            print(f"Erreur inattendue: {type(e).__name__}: {e}")

        # Proposer une autre conversion
        continuer = input("\nFaire une autre conversion? (o/n): ").strip()
        if continuer.lower() != 'o':
            print("Au revoir!")
            break

def tests_convertisseur():
    """Fonction de test pour le convertisseur"""
    print("=== TESTS DU CONVERTISSEUR ===")

    convertisseur = Convertisseur()

    tests = [
        ('temperature', '100', 'Celsius', 'Fahrenheit'),
        ('temperature', '32', 'Fahrenheit', 'Celsius'),
        ('distance', '1', 'Kilomètres', 'Mètres'),
        ('distance', '1000', 'Mètres', 'Kilomètres'),
        ('poids', '1', 'Kilogrammes', 'Grammes'),
        ('poids', '1000', 'Grammes', 'Kilogrammes'),
        ('monnaie', '100', 'USD', 'EUR'),
        ('monnaie', '100', 'EUR', 'USD')
    ]

    for categorie, valeur, source, cible in tests:
        try:
            resultat = convertisseur.convertir(categorie, valeur, source, cible)
            print(f"✓ {valeur} {source} -> {resultat}")
        except Exception as e:
            print(f"✗ Erreur: {e}")

if __name__ == "__main__":
    # Option: exécuter les tests
    # tests_convertisseur()

    # Lancer le menu principal
    menu_convertisseur()
```
