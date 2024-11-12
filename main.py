from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Home.html')


@app.route("/api/v1/<word>")
def define(word):
    df = pd.read_csv("dictionary.csv")
    meaning = df.loc[df["word"] == word]["definition"].squeeze()
    final = {"word": word, "definition": meaning}
    return final


if __name__ == "__main__":
    app.run(debug=True)