from flask import Flask, render_template, request
import recommendation as rec
import pandas as pd


app = Flask(__name__)
app.debug = True

###################################################
# Récupérer le csv et le transformer en dataframe #
###################################################
df = pd.read_csv('books_after_process.csv')


###############
# Application #
###############

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Récupérez le terme de recherche envoyé dans le formulaire
        book = request.form.get("book_name")
        num = request.form.get("num")

        # Mettre le livre rentré en minuscule
        book = book.lower()

        #transformer num en int
        num = int(num)

        #Variable no_book
        no_book = "Désolé, Nous n'avons pas ce livre dans notre base"

        # Recommandation pour le livre
        dico = []
        ramdom_dico = []
        
        if book in df["title"].values:
            dico = rec.recommend(book, num)
        else:
            no_book = "Désolé, Nous n'avons pas ce livre dans notre base"
            ramdom_dico = rec.ramdom_recommendation()

        # Affichez les documents dans la vue (template HTML)
        return render_template("index.html", dico=dico, no_book=no_book, num=num, ramdom_dico=ramdom_dico)
    
    # Si aucune recherche n'a été effectuée, affichez la page d'accueil
    return render_template("./index.html")

@app.route("/book_detail/<string:id>")
def book_detail(id):

    # Récupérer les informations sur le livre à partir de l'id
    detail_dico = rec.detail_book(id)

    return render_template("book_detail.html", detail_dico=detail_dico)