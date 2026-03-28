# Uni-ChatBot

Assistant conversationnel intelligent base sur les intentions pour les renseignements universitaires.

## Description du Projet
Uni-ChatBot est un systeme de chatbot concu pour automatiser les reponses aux questions frequentes des etudiants. Le projet utilise le Traitement du Langage Naturel (NLP) pour comprendre les questions des utilisateurs et un reseau de neurones profond pour classifier ces questions par categories.

## Outils et Technologies
* Langage : Python.
* Traitement de texte : NLTK (Natural Language Toolkit)
* Calcul numerique : NumPy
* Stockage de donnees : JSON.
* Environnement de developpement : Google Colab / VS Code

## Dataset Choisi
Le dataset est un fichier JSON structuré nommé chatbot.json. Il est organise en plusieurs intentions (intents) comprenant :
* Tag : L'identifiant unique de la categorie (greetings,goodbye,creator,...etc).
* Patterns : Les differentes facons dont un utilisateur peut poser une question.
* Responses : Les reponses predefinies que le bot peut selectionner.



## Phase de Pretraitement des donnees
Le prétraitement est l'étape cruciale pour transformer le texte brut en données numeriques exploitables par l'IA.

### 1. Tokenisation
Chaque phrase du dataset est decoupée en tokens.

### 2. Lemmatisation
Tous les mots sont convertis en minuscules et réduits a leur racine. Par exemple, "studying" ou "studies" deviennent "study". Cela permet au modèle de traiter différentes formes d'un meme mot comme une seule entité, reduisant ainsi la complexité du vocabulaire.

