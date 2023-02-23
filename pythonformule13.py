import streamlit as st

def calcul_prix_min(nb_ecoles, nb_siret, montant_taxe):
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

st.title("Calcul du prix minimum")

nb_ecoles = st.number_input("Nombre d'écoles", min_value=0, step=1)
nb_siret = st.number_input("Nombre de Siret actifs", min_value=0, step=1)
montant_taxe = st.number_input("Montant de la taxe", min_value=0.0, step=0.01)

tranche_effectif = st.selectbox("Tranche effectif", ["10 à 19 salariés", "20 à 49 salariés", "50 à 99 salariés",
                                                      "100 à 199 salariés", "200 à 249 salariés", "250 à 499 salariés",
                                                      "500 à 999 salariés", "1 000 à 1 999 salariés", "2 000 à 4 999 salariés",
                                                      "5 000 à 9 999 salariés", "10 000 salariés et plus"])

prix_min = calcul_prix_min(nb_ecoles, nb_siret, montant_taxe)

if montant_taxe > prix_min:
    resultat = "PROFITABLE"
else:
    resultat = "PAS PROFITABLE"

if resultat == "PROFITABLE":
    st.write("<h1 style='color:green;'>Résultat : {}</h1>".format(resultat), unsafe_allow_html=True)
else:
    st.write("<h1 style='color:red;'>Résultat : {}</h1>".format(resultat), unsafe_allow_html=True)

st.subheader("Prix minimum:")
prix_min_arrondi = round(prix_min, 2)
st.write(prix_min_arrondi)
