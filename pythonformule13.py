import streamlit as st

# Initialiser les variables
nego = 165

# Définir la fonction pour calculer le prix minimum
def calcul_prix_min(nb_ecoles, nb_siret):
    traitement = nb_ecoles * 7.5
    if nb_ecoles == 1:
        saisie = nb_siret * 1.2
    elif nb_siret == 1:
        saisie = nb_ecoles * 1.2
    else:
        saisie = (nb_ecoles + nb_siret) * 1.2
    extraction = saisie
    total_heure = (nego + traitement + saisie + extraction) / 60
    cout_revient = total_heure * 47.96158822
    seuil_rentabilite = cout_revient * 1.5
    prix_min = cout_revient * 4
    return prix_min

# Définir la liste déroulante pour tranche_effectif
tranche_effectif_options = {
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

# Définir l'interface utilisateur
st.title("Calcul : Profitabilité 13%")
st.write("Entrez les valeurs pour calculer le prix minimum et vérifier la profitabilité.")
nb_ecoles = st.number_input("Nombre d'écoles", min_value=0)
nb_siret = st.number_input("Nombre de Siret actifs", min_value=0)
tranche_effectif = st.selectbox("Tranche effectif", options=list(tranche_effectif_options.keys()))

if st.button("Calculer"):
    prix_min = calcul_prix_min(nb_ecoles, nb_siret)
    resultat = "PROFITABLE" if tranche_effectif_options[tranche_effectif] > prix_min else "PAS PROFITABLE"
    st.write(f"Résultat : {resultat}", unsafe_allow_html=True)
    if resultat == "PROFITABLE":
        st.markdown(f"<h1 style='color: green'>{resultat}</h1>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='color: red'>{resultat}</h1>", unsafe_allow_html=True)
    st.write(f"Prix minimum : {prix_min:.2f}")
