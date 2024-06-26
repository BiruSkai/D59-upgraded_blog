from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager
app = Flask(__name__)

url = "https://api.npoint.io/0b05e13fc68b93b1aa29"
url_data = requests.get(url).json()
notification_manager = NotificationManager()

@app.route("/")
def home():
    return render_template("index.html", datas=url_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = (data["name"])
        email = (data["email"])
        phone = (data["phone"])
        message = (data["message"])
        if data:
            print(message)
            notification_manager.send_email(name, email, phone, message)

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def post_detail(index):
    for data in url_data:
        if data["id"] == index:
            return render_template("post.html", data=data)




@app.route("/no_page")
def no_page():
    return render_template("no_page.html")


if __name__ == "__main__":
    app.run(debug=True)