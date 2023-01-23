import time


def afficher_heure():
    while True:
        heure_actuelle = time.localtime()
        heure_formatee = time.strftime("%H:%M:%S", heure_actuelle)
        print(heure_formatee)
        time.sleep(1)


def regler_heure(heure_tuple):
    heure, minute, seconde = heure_tuple
    heure_actuelle = time.localtime()
    heure_actuelle = heure_actuelle[:3] + \
        (heure, minute, seconde) + heure_actuelle[6:]
    time.mktime(heure_actuelle)


def regler_alarme(heure_tuple):
    heure, minute, seconde = heure_tuple
    while True:
        heure_actuelle = time.localtime()
        if heure_actuelle.tm_hour == heure and heure_actuelle.tm_min == minute and heure_actuelle.tm_sec == seconde:
            print("Alarme!")
            break


afficher_heure()
