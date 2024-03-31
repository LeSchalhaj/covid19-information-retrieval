# Algorithme de Recherche d'Information sur le COVID-19

Ce TP implémente un algorithme de recherche d'information pour un corpus de documents sur le COVID-19. Il permet d'exécuter des requêtes booléennes ainsi que des recherches textuelles complexes pour trouver des informations pertinentes dans un ensemble de documents textuels.

## Fonctionnalités

- **Prétraitement du texte** : Nettoyage, tokenisation, suppression des mots vides, et lemmatisation.
- **Construction d'une matrice d'incidence** : Représentation des documents et des termes pour faciliter la recherche d'information.
- **Indexation** : Création d'un index inversé pour optimiser les recherches dans le corpus.
- **Requêtes booléennes** : Support des opérateurs logiques AND, OR, et NOT pour des recherches précises.
- **Recherches textuelles complexes** : Utilisation de TF-IDF et de la similarité cosinus pour trouver les documents les plus pertinents basés sur des requêtes textuelles.

## Installation

Assurez-vous d'avoir Python 3.x installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :
- NLTK
- NumPy
- scikit-learn

Vous pouvez installer ces dépendances en utilisant `pip` :

# Exemples de Requêtes
Requêtes booléennes : disease AND severe, NOT plasma AND risk of infection
Requêtes textuelles complexes : antibody treatments, genomic analysis of SARS-CoV-2


