#!/usr/bin/env python
# coding: utf-8

# In[12]:


# exercice 1
def transform(chain):
    parti1 = set(map(int, chain[0].split(', ')))
    parti2 = set(map(int, chain[1].split(', ')))
    
    nombres_communs = sorted(list(parti1.intersection(parti2)))
    
    # Trouver le nom, prénom et classe
    nom_utilisateur = "Mouhoumed"
    prenom_utilisateur = "Kader"
    classe_utilisateur = "Master1AI"

    # Ajouter le nom, prénom et classe à la fin de la chaîne résultante
    if nombres_communs:
        resultat_str = ','.join(map(str, nombres_communs))
        resultat_str += f":{nom_utilisateur}_{prenom_utilisateur}_{classe_utilisateur}"
        return resultat_str
    else:
        return None

if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out1 = transform(arr1)
    print(out1)  # Chaîne des entiers communs avec nom, prénom et classe

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out3 = transform(arr3)
    print(out3)  # None


# In[10]:


# exercice 2
liste1 = []
for i in range(1200, 2000, 135):
    liste1.append(i)

liste2 = []
for i in liste1:
    if i % 2 == 0:
        liste2.append(i * 2)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = []
e = []

for x in numbers:
    if x % 2 == 0:
        o.append(x)
    else:
        e.append(x)

print(liste1)
print(liste2)
print(o)
print(e)


# In[11]:


# Une autre manière d’additionner deux nombres entiers
a = 12
b = 8
resultat = a + b
print(resultat)


# In[8]:


# exercice 3
import sqlite3

def find_missing_and_store(arr):
    # Trouver le nombre manquant dans le tableau
    missing_number = sum(range(min(arr), max(arr)+1)) - sum(arr)

    # Stocker le nombre manquant dans une table SQLite
    conn = sqlite3.connect('missing_number.db')
    cursor = conn.cursor()

    # Créer la table s'il n'existe pas
    cursor.execute('CREATE TABLE IF NOT EXISTS missing_numbers (number INTEGER);')

    # Insérer le nombre manquant dans la table
    cursor.execute('INSERT INTO missing_numbers VALUES (?);', (missing_number,))

    # Commit et fermer la connexion
    conn.commit()
    conn.close()

    return missing_number

# Exemple d'utilisation
tableau_exemple = [7, 4, 6, 1, 3, 8, 2]
resultat = find_missing_and_store(tableau_exemple)
print(f"Le nombre manquant est {resultat} et a été stocké dans la base de données SQLite.")


# In[ ]:




