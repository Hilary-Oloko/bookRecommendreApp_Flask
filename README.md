#bookRecommendreApp_Flask

#English:

This project contains all the files necessary to launch a Flask application that recommends files from the title of a book entered by a user.

In this part I will describe each of the documents and what they contain but first here is a presentation of the final application through screenshots.

Description of the different files:
* books_after_process.csv : contains over 4000 books and is made from a file downloaded from Kaggle. Then I did the cleaning by deleting useless columns, deleting empty rows, deleting books without authors or summaries, deleting books whose authors or summaries had different characters than those used in English, etc. Finally I concatenated the columns that will be useful for the recommendation system in a column that I called all_data
* recommender.py : contains three functions. A function that gives book recommendations from the title of a book in the database, a function that returns a dictionary with the characteristics of three random books and a function that returns the characteristics of a book based on its id.
* app.py : contains the flask application code
* index.py : contains the code of the page where the user will be directed after launching the application. This is where he will be able to do a search in order to get book recommendations. If the book is contained in the CSV file, it will return the number of books that the user wants and he can even go to pages that give details about each book. If the book is not in the csv file, it will display ten books at random
* book_details.py : contains the html code that displays the content of the detail pages according to the book id

#Français:

Ce projet contient tous les fichiers nécessaires au lancement d'une application Flask qui recommande des fichiers à partir du titre d'un livre rentré par un utilisation.

Dans cette partie je vais décrire chacun des documents et ce qu'ils contiennent mais d'abord voici une présentation de l'application finale à travers des captures d'écran.

Description of the different files:
* books_after_process.csv : contient plus de 4000 livres et est fait à partir d'une fichier téléchargé sur Kaggle. Ensuite j'ai effectué le nettoyage en supprimer des colonnes inutiles, en supprimant les lignes vides, les libres sans auteurs ou sans résumé, en supprimant les livres dont les auteurs ou les résumés avaient des caractères différents de ceux utilisés en anglais, etc. Enfin j'ai concaténè les colonnes qui me seront utiles pour le système de recommandation dans une colonne que j’ai appelé all_data
* recommender.py : contient trois fonction. Une fonction qui permet de donner des recommandations de livre à partir du titre d'un livre contenu dans la base de donnée, une fonction qui retourne un dictionnaire avec les caractéristiques de trois livres au hasard et une fonction qui retourne les caractéristiques d'un livre en fonction de son id.
* app.py : contient le code de l'application flask
* index.py : contient le code de la page où l'utilisateur sera dirigé après le lancement de l'application. C'est à ce niveau qu'il pourra faire une recherche afin d'avoir des recommandations de livre. Si le livre est contenu dans le fichier CSV, il retournera le nombre de livre que l'utilisateur voudra et celui-ci pourra même se rendre sur des pages qui donne des détails sur chaque livre. Si le livre n'est pas dans le csv une dizaine de livres au hasard seront afficher
* book_details.py : contient le code html qui permet d'afficher le contenu des pages détail en fonction de l'id du livre
