import datetime

# Demander à l'utilisateur de spécifier le jour de la semaine et l'heure de fin
jour_choisi = input('Entrez le jour de la semaine ou vous voulez terminé (lundi, mardi, etc.) : ')
heure_choisie = int(input('Entrez l\'heure de fin (0-23) : '))
minute_choisie = int(input('Entrez les minutes de fin (0-59) : '))

# Spécifier la durée de la recherche en jours, heures et minutes
duree_recherche_jours = int(input('Entrez la durée de la recherche/construction en jours : '))
duree_recherche_heures = int(input('Entrez la durée de la recherche/construction en heures : '))
duree_recherche_minutes = int(input('Entrez la durée de la recherche/construction en minutes : '))

# Créer un dictionnaire pour mapper les noms des jours de la semaine aux numéros de 0 (lundi) à 6 (dimanche)
jours_de_la_semaine = {
    'lundi': 0,
    'mardi': 1,
    'mercredi': 2,
    'jeudi': 3,
    'vendredi': 4,
    'samedi': 5,
    'dimanche': 6
}

# Obtenir la date et l'heure actuelles
maintenant = datetime.datetime.now()

# Obtenir le numéro du jour de la semaine choisi
jour_choisi_num = jours_de_la_semaine.get(jour_choisi.lower())
if jour_choisi_num is None:
    print('Jour de la semaine invalide. Assurez-vous d\'utiliser un nom de jour correct.')
else:
    # Calculer la date et l'heure de fin en fonction du jour et de l'heure choisis
    date_fin = maintenant.replace(hour=heure_choisie, minute=minute_choisie, second=0, microsecond=0)

    # Si le jour choisi est déjà passé, ajouter 7 jours pour passer à la semaine suivante
    if jour_choisi_num < maintenant.weekday():
        jours_a_ajouter = 7 - (maintenant.weekday() - jour_choisi_num)
    else:
        jours_a_ajouter = jour_choisi_num - maintenant.weekday()

    date_fin += datetime.timedelta(days=jours_a_ajouter)

    # Calculer la date de début en soustrayant la durée de la recherche/construction à la date de fin
    duree_recherche = datetime.timedelta(days=duree_recherche_jours, hours=duree_recherche_heures, minutes=duree_recherche_minutes)
    date_debut = date_fin - duree_recherche

    # Afficher la date de début recommandée
    print("Pour que la recherche/construction se termine le {} à {}:{:02d}, commencez le {}.".format(
        jour_choisi, heure_choisie, minute_choisie, date_debut.strftime('%Y-%m-%d %H:%M:%S')))

# Ajoutez cette ligne pour maintenir le terminal ouvert
input("Appuyez sur Entrée pour quitter...")
