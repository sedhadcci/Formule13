import streamlit as st

st.title('Calcul : Profitabilité 13%')

# Entrée utilisateur pour le nombre d'écoles
nb_ecoles = st.number_input("Nombre d'écoles :", value=1)

# Entrée utilisateur pour le nombre de SIRET actifs
nb_siret = st.number_input("Nombre de SIRET actifs :", value=1)

# Entrée utilisateur pour la tranche d'effectif
effectif_list = ["10 à 19 salariés​​", "20 à 49 salariés​​​​", "50 à 99 salariés​​​​", "100 à 199 salariés​​​​", "200 à 249 salariés​​​​", "250 à 499 salariés​​​​", "500 à 999 salariés​​​​", "1 000 à 1 999 salariés​​", "2 000 à 4 999 salariés​​", "5 000 à 9 999 salariés​​", "10 000 salariés et plus​​​​"]
effectif_value = [225, 450, 1125, 2251, 4503, 5629, 11258, 22517, 45034, 112687, 225174]
effectif_dict = dict(zip(effectif_list, effectif_value))
tranche_effectif = st.selectbox("Tranche d'effectif :", options=effectif_list)

# Calcul du prix minimum
nego = 165
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
prix_min = cout_revient * 4 - effectif_dict[tranche_effectif]

# Affichage du résultat
if prix_min > 0:
    resultat = "PROFITABLE"
    resultat_color = "green"
else:
    resultat = "PAS PROFITABLE"
    resultat_color = "red"

st.markdown(f"<h1 style='text-align: center; color: {resultat_color};'>{resultat}</h1>", unsafe_allow_html=True)
st.write(f"Prix minimum : {prix_min:.2f}")
