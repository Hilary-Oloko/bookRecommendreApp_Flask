import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

###################################################
# Récupérer le csv et le transformer en dataframe #
###################################################

df = pd.read_csv('books_after_process.csv')

#################
# Vectorization #
#################

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['all_data'])


##############################
# Fonction de recommandation #
##############################

def recommend(title, num):    
    dict = []

    # Trouver l'index du livre spécifié
    idx = df[df['title'] == title].index[0]

    # Calculer la similarité cosine entre le livre spécifié et tous les autres livres
    sim_scores = cosine_similarity(X[idx], X).flatten()

    # Trier les livres par ordre de similarité décroissante
    sim_scores = sim_scores.argsort()[::-1]
    
    for i in sim_scores[1:num+1]:
        data = {
            'title' : df.iloc[i]['title'],
            'cover' : df.iloc[i]['coverImg'],
            'author' : df.iloc[i]['author'],
            'id' : df.iloc[i]['_id'],
            'genres' : df.iloc[i]["genres"],
        }
        dict.append(data)
    
    return dict


random_seed = random.randint(1, 100000)
ramdom_df = df.sample(n=10, axis=0, random_state=42)
def ramdom_recommendation():
    random_seed = random.randint(1, 100000)
    ramdom_df = df.sample(n=10, axis=0, random_state=random_seed)
    ramdom_dico = []
    for i in range(10):
        data = {
                    'title' : ramdom_df.iloc[i]['title'],
                    'cover' : ramdom_df.iloc[i]['coverImg'],
                    'author' : df.iloc[i]['author'],
                    'id' : df.iloc[i]['_id'],
                }
        ramdom_dico.append(data)
    return ramdom_dico

def detail_book(id):
    # Trouver l'index du livre spécifié
    book = df[df["_id"] == id]
    # extraire les informations souhaitées
    data = {
        'title' : book["title"].iloc[0],
        'resume' : book["resume"].iloc[0],
        'author' : book["author"].iloc[0],
        'cover' : book["coverImg"].iloc[0],
        'genres' : book["genres"].iloc[0],
    }
    return(data)