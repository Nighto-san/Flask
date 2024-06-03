from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [{"name": "STR", "url": "str"},
        {"name": "LIST", "url": "list"},
        {"name": "SET", "url": "set"},
        {"name": "FOR", "url": "for"},
        {"name": "WHILE", "url": "while"},
        {"name": "GRAF", "url": "graf"},
        {"name": "JINJA", "url": "jinja"},
        {"name": "HTLM", "url": "html"},
        {"name": "CSS", "url": "css"},
        {"name": "        ", "url": ""},
        {"name": "FLASK", "url": "flask"},
        {"name": "             ", "url": ""}
        {"name": "Обратная связь", "url": "contact"},]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/contact")
def contact():
    print(url_for('contact'))
    return render_template('contact.html', title="Контакт", menu=menu)




if __name__ == "__main__":
    app.run(debug=True)
