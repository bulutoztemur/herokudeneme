from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/toplam", methods=['GET', 'POST'])
def toplam():
    if request.data == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        return render_template("number.html", total=int(a) + int(b))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

