import requests

# URL de l'API
url = "http://localhost/maintenance/wp-json/maintenance-pack/v1/backup/"

# Paramètres éventuels pour la requête GET
# params = {
#     "param1": "valeur1",
#     "param2": "valeur2"
# }

# En-têtes HTTP si nécessaire (exemple pour une API qui demande une clé)
#headers = {
#   "Authorization": "Bearer VOTRE_CLE_API",
#   "Accept": "application/json"
#}

# Faire la requête GET
# response = requests.get(url, params=params, headers=headers)
response = requests.get(url)
# Vérifier le code de retour
if response.status_code == 200:
    data = response.json()  # Convertir la réponse JSON en dictionnaire Python
    print("Données reçues :", data)
else:
    print(f"Erreur {response.status_code} : {response.text}")
