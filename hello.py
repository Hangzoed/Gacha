from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/BlueArchive')
def blue():
    return render_template("BlueArchive.html")

@app.route('/FateGrandOrder')
def FGO():
    return render_template("FateGrandOrder.html")

@app.route('/LeagueOfLegends')
def League():
    return render_template("LeagueofLegends.html")
@app.route('/Arknights')
def Ark():
    return render_template("Arknights.html")

@app.route('/Genshin')
def Genshin():
    return render_template("Genshin.html")


@app.route('/HSR')
def HSR():
    return render_template("HSR.html")


if __name__ == '__main__':
    app.run(debug=True)