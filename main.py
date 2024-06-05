from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.secret_key = 'your_secret_key'

menu = [{"name": "STR", "url": "str"},
        {"name": "LIST", "url": "list"},
        {"name": "SET", "url": "set"},
        {"name": "FOR", "url": "for"},
        {"name": "WHILE", "url": "while"},
        {"name": "GRAF", "url": "graf"},
        {"name": "JINJA", "url": "jinja"},
        {"name": "HTLM", "url": "html"},
        {"name": "CSS", "url": "css"},
        {"name": "SQL", "url": "sql"},
        {"name": "FLASK", "url": "flask"},
        {"name": "             ", "url": ""},
        {"name": "Обратная связь", "url": "contact"},]




@app.route("/sql")
def sql():
    print(url_for('sql'))
    return render_template('sql.md', title="SQL", menu=menu)

@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная страница', menu=menu)

@app.errorhandler(404)
def page404(error):
    return render_template('page404.html', title="404 ошибка", menu=menu)

@app.route("/contact",methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('сообщение отправлено успешно',category='success')
        else: flash('Слишком короткое имя',category='error')

    return render_template('contact.html', title="Контакт", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Пользователь: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.form['username'] == "nighto" and request.form['password'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
