#bookRecommendreApp_Flask

#English:

This project contains all the files necessary to launch a Flask application that recommends files from the title of a book entered by a user.

In this part I will describe each of the documents and what they contain but first here is a presentation of the final application through screenshots.

* description of the different files:
       - books_after_process.csv : contains over 4000 books and is made from a file downloaded from Kaggle. Then I did the cleaning by deleting useless columns, deleting empty rows, deleting books without authors or summaries, deleting books whose authors or summaries had different characters than those used in English, etc. Finally I concatenated the columns that will be useful for the recommendation system in a column that I called all_data
        - recommender.py 
        - app.py
        - index.py
        - book_detains.py

#Français:

Ce projet contient tous les fichiers nécessaires au lancement d'une application Flask qui recommande des fichiers à partir du titre d'un livre rentré par un utilisation.

Dans cette partie je vais décrire chacun des documents et ce qu'ils contiennent mais d'abord voici une présentation de l'application finale à travers des captures d'écran.

* description of the different files:
        - books_after_process.csv : contient plus de 4000 livres et est fait à partir d'une fichier téléchargé sur Kaggle. Ensuite j'ai effectué le nettoyage en supprimer des colonnes inutiles, en supprimant les lignes vides, les libres sans auteurs ou sans résumé, en supprimant les livres dont les auteurs ou les résumés avaient des caractères différents de ceux utilisés en anglais, etc. Enfin j'ai concaténè les colonnes qui me seront utiles pour le système de recommandation dans une colonne que j’ai appelé all_data
        - recommender.py : 
        - app.py
        - index.py
        - book_detains.py
