'''
# cree BDD
CREATE DATABASE badge;

# cree table avec nom des colone
CREATE TABLE  badge(id int(2) NOT NULL AUTO_INCREMENT, num_badge INTEGER ,num_porte_entree INTEGER, date_heure_entree datetime, date_heure_sortie datetime, PRIMARY KEY(id) );

#cree des donnee dans la BDD
INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES("56734942",1,"2023-10-03 15:20:16","2023-10-03 17:46:52");
INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES("98756513",2,"2023-05-24 20:12:52","2023-05-25 05:59:59");
INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES("15632894",1,"2023-06-21 06:29:22","2023-06-21 17:01:28");
INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES("84756215",1,"2023-10-01 08:25:35","2023-10-01 19:46:54");
INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES("95156164",3,"2023-09-24 15:45:54","2023-09-24 14:56:54");
INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES("56734942",2,"2023-10-09 13:53:15","2023-10-09 19:02:34");
'''

########################################
###     IMPORTATION MODULE / BDD     ###
########################################

from datetime import datetime

import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="azerty",
database="badge",)

#######################################
###             FONCTION            ### 
#######################################
  
def tracabilite_chronologique (badge):
    cursor = conn.cursor()
    cursor.execute(""" SELECT num_badge,num_porte_entree ,date_heure_entree, date_heure_sortie FROM badge WHERE num_badge = %s ORDER BY date_heure_sortie ;""",(badge,))
    result = cursor.fetchall()
    for x in result:
        print(x)


def tracabilite_entre_date(badge,entree,sortie):
    cursor = conn.cursor()
    cursor.execute(""" SELECT num_badge,num_porte_entree ,date_heure_entree, date_heure_sortie FROM badge WHERE num_badge = %s AND date_heure_entree BETWEEN %s and %s;""",(badge,entree,sortie,))
    result = cursor.fetchall()
    for x in result:
        print(x)


def del_badge(badge):
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM badge WHERE num_badge = %s ; """,(badge,))
    result = cursor.fetchall()
    for x in result:
        print(x)


def del_date(date_heure_sortie):
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM badge WHERE date_heure_sortie = %s ; """,(date_heure_sortie,))
    result = cursor.fetchall()
    for x in result:
        print(x)


def badge_manuel (badge,porte,entree,sortie):
    cursor = conn.cursor()
    cursor.execute(""" INSERT INTO badge (num_badge, num_porte_entree, date_heure_entree, date_heure_sortie) VALUES(%s,%s,%s,%s);""",(badge,porte,entree,sortie))
    conn.commit()


def correction_badge(sortie,badge):
    cursor = conn.cursor()
    cursor.execute(""" UPDATE badge SET date_heure_sortie  = %s WHERE num_badge = %s; """,(sortie,badge,))
    result = cursor.fetchall()
    for x in result:
        print(x)


def affichage ():
    cursor = conn.cursor()
    cursor.execute(""" SELECT* FROM badge """)
    result = cursor.fetchall()
    for x in result:
        print(x)

################################
###       INTERFACE          ###
################################

print("\n\nBoujours et bienvenue sur la base de donnée des badges RFID.")

while(True):
    print("""
    *** MENU DES BADGE RFID ***
    1 - Afficher les données du badge souhaité par ordre chronologique          
    2 - Afficher les données du badge souhaité entre deux date demandé          
    3 - Effacer un badge   
    4 - Effacer la date de sortie d'un badge                                                            
    5 - Ajouter une entrée manuellement                     
    6 - Modifier des information sur un badge                                   
    7 - Afficher toute les donnée de la base de donnée                          
    """)

    valeur = int(input(" Entrer votre choix : "))

    if valeur == 1 :                                                    #afficher les donnee du badge demande par ordre chronologique
        badge = int(input("Entrer le numero du badge : "))

        print("\nVoila l'historique du badge numéro :",badge,"\n")
        tracabilite_chronologique(badge)
        print("\nRetour au menu principal \n\n")


    elif valeur == 2 :                                                  #afficher les donnee du badge d'une date x a x 
        badge = int(input("Entrer le numero du badge : "))
        entree = input("date de debut (format AAAA-MM-JJ HH:MM:SS) : ")
        sortie = input ("date de fin (format AAAA-MM-JJ HH:MM:SS) : ")
        print("\n")

        print("\nVoila l'historique du badge numéro :",badge,"\n")
        tracabilite_entre_date(badge,entree,sortie)
        print("\nRetour au menu principal \n\n")


    elif valeur == 3 :                                                  #supprime avec un badge
        badge = int(input("Entrer le numéro du badge : "))

        del_badge(badge)
        print("\nLe badge numero",badge,"a bien été suprimé.")
        print("Retour au menu principal \n\n")


    elif valeur == 4 :                                                  #supprimer avec une date
        date_heure_sortie = (input("Entrer la date de sortie du badge (format AAAA-MM-JJ HH:MM:SS) : "))

        del_date(date_heure_sortie)
        print("\nLa date de sortie a bien été suprimé.")
        print("Retour au menu principal \n\n")


    elif valeur == 5 :                                                  #cree un nouveeau badge
        badge = str(input("\nEntrer le numero du badge : "))
        porte = int(input("Entrer le numero de la porte : "))
        entree = datetime.now()
        sortie = datetime.now()

        badge_manuel(badge,porte,entree,sortie)
        print(" \nNouveau badge enregistré avec comme numéro :",badge)
        print("Retour au menu principal \n\n")


    elif valeur == 6 :                                                  #modifie date d'un badge
        badge = int(input("\nEntrer le numero du badge : "))
        sortie = input("Entrer la nouvelle date de sortie du badge (format AAAA-MM-JJ HH:MM:SS) : ")

        correction_badge(sortie,badge)
        print("\n\nLe badge numéro :",badge,"a bien été modifié.")
        print("Retour au menu principal \n\n")


    elif valeur == 7 :                                                  #affiche toute la BDD
        print("\nVoila la base de donnée : \n")
        affichage()
        print("\nRetour au menu principal \n\n")


'''
menu        3/4   faire sous menu
afficher    3/4   meilleur affichage date
ajouter     4/4
modifier    4/4
supprimer   3/4   
total       17/20
'''
