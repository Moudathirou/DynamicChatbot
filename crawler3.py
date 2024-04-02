
import requests
from bs4 import BeautifulSoup

def ajuster_liens(url_de_base, contenu_html):
    soup = BeautifulSoup(contenu_html, 'html.parser')
    liens_ajustes = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            # Si le lien commence déjà par 'http', on le garde tel quel.
            if href.startswith('http'):
                liens_ajustes.append(href)
            else:
                # Ajouter un slash si le lien ne commence pas par '/'.
                href_ajuste = href if href.startswith('/') else '/' + href
                liens_ajustes.append(url_de_base.rstrip('/') + href_ajuste)
    return liens_ajustes

# Utilisation de la fonction
"""url = "https://orbicall.com/"
response = requests.get(url)
liens_ajustes = ajuster_liens(url, response.text)
liens_ajustes = list(set(liens_ajustes))  # supprimer les doublons

# Écriture des liens dans un fichier texte
with open('liens.txt', 'w') as f:
    for lien in liens_ajustes:
        f.write("%s\n" % lien)"""

#print("Les liens ont été écrits dans le fichier liens.txt")





