from flask import Flask, render_template, request

from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tuemaildeprueba@gmail.com'
app.config['MAIL_PASSWORD'] = 'tupassworddeprueba'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/send_message', methods=["GET", "POST"])
def send_message():
    if request.method == "POST":
        addressee = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        message = Message(
            subject, sender="tuemaildeprueba@gmail.com", recipients=[addressee])

        message.body = message

        mail.send(message)

        success = "Message sent"

        return render_template("result.html", success=success)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
