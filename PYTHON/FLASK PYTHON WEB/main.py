from flask import Flask , render_template

app=Flask(__name__)


url="https://api.npoint.io/5feef6879ed0a3895201"
import requests


@app.route("/")
def homePage():
    received=requests.get(url)
    received_json=received.json()
    return render_template("index.html",posts=received_json)
@app.route("/index.html")
def IndexPage():
        received=requests.get(url)
        received_json=received.json()
        return render_template("index.html",posts=received_json)


@app.route("/about.html")
def aboutPage():
    return render_template("about.html")
@app.route("/contact.html")
def contactPage():
    return render_template("contact.html")

@app.route("/post.html/<id>")
def postPage(id):
    received=requests.get(url)
    received_json=received.json()
    return render_template("post.html",post=received_json[int(id)])






if __name__=="__main__":
    app.run(debug=True)
