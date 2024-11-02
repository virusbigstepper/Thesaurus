from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Home.html')


@app.route("/api/v1/<definition>/<word>")
def define(definition, word):
    df = pd.read_csv("dictionary.csv")
    meaning = df.loc[df["word"] == word]["definition"]
    final = {"definition": meaning, "word": word}
    return final


if __name__ == "__main__":
    app.run(debug=True)