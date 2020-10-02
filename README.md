# OC P5 - OpenFoodFacts

## 1. Présentation
La startup *Pur Beurre* connait bien les habitudes alimentaires françaises. Leur restaurant, Ratatouille, remporte un succès croissant et attire toujours plus de visiteurs sur la butte de Montmartre.  
L'équipe a remarqué que leurs clients voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer.  
Remplacer le Nutella par une pâte aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ?  
Leur idée est donc de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

---
## 2. Fonctionnalités
Plusieurs fonctionnalités sont nécessaires pour la réalisation de ce projet:
- Rechercher un aliment à remplacer
- Trouver des aliments de substitution
- Pouvoir sauvegarder les aliments de substitution trouvés

---
## 3. Pré-requis
Python >= 3.6  
Il est nécessaire d'avoir une instance de base de données mysql    
Pour le développement, j'ai utilisé une image Docker de mysql  
`docker run -it -p 3306:3306 -e MYSQL_ROOT_PASSWORD='PASSWORD_HERE' mysql:latest`  
-> Modifiez le mot de passe et gardez le de côté, on en aura encore besoin 😉

---
## 4. Utilisation

- Clonez le repo et `cd` à l'intérieur
- Modifiez `openfoodfacts/settings.py` :
    - ligne 10, modifiez si besoin l'`user` de la base de données
    - ligne 11, modifiez le mot de passe de la base de données
- Créez un environement virtuel : `python -m venv venv`
- Activez l'environement virtuel :
    - Windows : `.\venv\Scripts\Activate.ps1`
    - Linux / Mac : `source venv/bin/activate`
- Installez les dépendances : `pip install -r requirements.txt`
- Lancez le programme :
    - option 1 : comme un module : `python -m openfoodfacts`
    - option 2 : comme un script : `python run.py`
