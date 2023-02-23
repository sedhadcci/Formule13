import streamlit as st

def calcul_prix_min(nb_ecoles, nb_siret, tranche_effectif, montant_taxe):
    # définition des variables
    NEGO = 165
    traitement = nb_ecoles * 7.5

    if nb_ecoles == 1:
        saisie = nb_siret * 1.2
    elif nb_siret == 1:
        saisie = nb_ecoles * 1.2
    else:
        saisie = (nb_siret + nb_ecoles) * 1.2

    if tranche_effectif:
        tranche_effectif_dict = {
            "10 à 19 salariés​​": 225,
            "20 à 49 salariés​​​​": 450,
            "50 à 99 salariés​​​​": 1125,
            "100 à 199 salariés​​​​": 2251,
            "200 à 249 salariés​​​​": 4503,
            "250 à 499 salariés​​​​": 5629,
            "500 à 999 salariés​​​​": 11258,
            "1 000 à 1 999 salariés​​": 22517,
            "2 000 à 4 999 salariés​​": 45034,
            "5 000 à 9 999 salariés​​": 112687,
            "10 000 salariés et plus​​​​": 225174
        }
        montant_taxe = tranche_effectif_dict[tranche_effectif]

    extraction = saisie

    total_heure = (NEGO + traitement + saisie + extraction) / 60

    cout_revient = total_heure * 47.96158822

    seuil_rentabilite = cout_revient * 1.5

    prix_min = cout_revient * 4

    if montant_taxe > prix_min:
        resultat = "PROFITABLE"
    else:
        resultat = "PAS PROFITABLE"

    return prix_min, resultat

st.title("Calcul : Profitabilité 13%")

nb_ecoles = st.number_input("Nombre d'écoles", min_value=0, step=1)
nb_siret = st.number_input("Nombre de Siret actifs", min_value=0, step=1)

option = st.selectbox("Choisir entre Montant de la taxe et Tranche effectif", ("Montant de la taxe", "Tranche effectif"))

if option == "Montant de la taxe":
    montant_taxe = st.number_input("Entrez le montant de la taxe:", min_value=0.0, step=0.01)
    tranche_effectif = None
else:
    tranche_effectif = st.selectbox("Choisir la tranche effectif:", ("10 à 19 salariés", "20 à 49 salariés", "50 à 99 salariés", "100 à 199 salariés", "200 à 249 salariés", "250 à 499 salariés", "500 à 999 salariés", "1 000 à 1 999 salariés", "2 000 à 4 999 salariés", "5 000 à 9 999 salariés", "10 000 salariés et plus"))

    # Convertir la tranche d'effectif en montant de taxe
    tranche_dict = {
        "10 à 19 salariés": 225,
        "20 à 49 salariés": 450,
        "50 à 99 salariés": 1125,
        "100 à 199 salariés": 2251,
        "200 à 249 salariés": 4503,
        "250 à 499 salariés": 5629,
        "500 à 999 salariés": 11258,
        "1 000 à 1 999 salariés": 22517,
        "2 000 à 4 999 salariés": 45034,
        "5 000 à 9 999 salariés": 112687,
        "10 000 salariés et plus": 225174
    }

    montant_taxe = tranche_dict[tranche_effectif]

prix_min, resultat = calcul_prix_min(nb_ecoles, nb_siret, montant_taxe, None)

if resultat == "PROFITABLE":
    st.write("<h1 style='color:green;'>Résultat : {}</h1>".format(resultat), unsafe_allow_html=True)
else:
    st.write("<h1 style='color:red;'>Résultat : {}</h1>".format(resultat), unsafe_allow_html=True)

st.subheader("Prix minimum:")
prix_min_arrondi = round(prix_min, 2)
st.write(prix_min_arrondi)

