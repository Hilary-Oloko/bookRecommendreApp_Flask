from pymongo import MongoClient
import pandas as pd
from nltk.stem import PorterStemmer
import re
import nltk
nltk.download('stopwords')
stemmer = PorterStemmer()
# Fonction de connexion à la base de données

def get_client(uri):
    return MongoClient(uri)

def get_collection(db, coll_name):
    return db[coll_name]


##########################################
# Connexion à la base de données Mongodb #
##########################################
client = get_client("mongodb://localhost:27017")
db = client['Recommendation_system']
livres_collection  = get_collection(db, 'books')
livres = livres_collection.find()

# Créez un DataFrame Pandas à partir des données
df = pd.DataFrame.from_records(livres)


#############################
# Prétraitement des données #
############################# 
# Suppression des colonnes et lignes inutiles

df.drop(columns = ['bookId','series','rating','pages','numRatings','ratingsByStars','isbn','language','publisher',
       'publishDate','firstPublishDate','characters','awards','setting',
        'bbeScore','bbeVotes','price','likedPercent', 'bookFormat','edition'],axis=1,inplace = True) #remove useless cols

df = df.dropna(subset=['title'])

# Créer une fonction pour vérifier si tous les caractères sont en anglais
def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# Appliquer la fonction à la colonne titre et author et filtrer les lignes qui ne sont pas en anglais
df = df[df['title'].apply(lambda x: x.isascii() if type(x) == str else False)]
df = df[df['author'].apply(lambda x: x.isascii() if type(x) == str else False)]

df['resume'] = df["description"]

#Supprimer toutes les lignes avec des resumes null
df = df.dropna(axis=0, subset=['resume'])

#Supprimer les doublons dans les lignes
df = df.drop_duplicates(subset="title", keep='first')

#Remplacer les genres null par unknown dans genres
df['genres'] = df['genres'].fillna('unknown')

#Supprimer les lignes qui n'ont pas d'image
df = df.dropna(axis=0, subset=['coverImg'])

#Mets en minuscule et supprime les
df['resume'] = df['resume'].str.lower()
df['description'] = df['description'].str.lower()
df['description'] = df['description'].str.replace('[^\w\s]', '')
df['genres'] = df['genres'].str.lower()
df['genres'] = df['genres'].str.replace('[^\w\s]', '')
df['author'] = df['author'].str.lower()
df['author'] = df['author'].str.replace('[^\w\s]', '')
df['title'] = df['title'].str.lower()
df['title'] = df['title'].str.replace('[^\w\s]', '')


#remove stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def remove_stopword(text):
    return " ".join(word for word in str(text).split() if word not in stop_words)

df["description"] = df['description'].apply(remove_stopword)

def stem_words(text):
    return " ".join(stemmer.stem(word) for word in text.split())

#Stemming
df['description']=df['description'].apply(stem_words)


###################################################################
# Concaténer le résumé, les tags et l'auteur en une seule colonne #
################################################################### 

df['all_data'] = df['description'] + " " + df['genres'] + " " + df['author']

# Exporter les données en CSV
df.to_csv('books_after_process.csv', index=False)