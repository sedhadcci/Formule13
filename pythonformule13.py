import streamlit as st

# définir la formule pour calculer prix_min
def calcul_prix_min(nb_ecoles, nb_siret):
    NEGO = 165
    traitement = nb_ecoles * 7.5

    if nb_ecoles == 1:
        saisie = nb_siret * 1.2
    elif nb_siret == 1:
        saisie = nb_ecoles * 1.2
    else:
        saisie = (nb_siret + nb_ecoles) * 1.2

    extraction = saisie

    total_heure = (NEGO + traitement + saisie + extraction) / 60

    cout_revient = total_heure * 47.96158822

    seuil_rentabilite = cout_revient * 1.5

    prix_min = cout_revient * 4

    return prix_min

# créer l'interface Streamlit
st.title("Calcul du prix minimum")

# ajouter les champs de saisie pour nb_ecoles et nb_siret
nb_ecoles = st.number_input("Nombre d'écoles", min_value=0, step=1)
nb_siret = st.number_input("Nombre de Siret actifs", min_value=0, step=1)

# calculer le prix minimum en utilisant les valeurs saisies
prix_min = calcul_prix_min(nb_ecoles, nb_siret)

# arrondir le résultat à 2 décimales
prix_min_arrondi = round(prix_min, 2)

# afficher le résultat
st.write("</h1>Le prix minimum est de: {:.2f}</h1>".format(prix_min_arrondi))
