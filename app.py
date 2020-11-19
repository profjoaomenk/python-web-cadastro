from flask import Flask, render_template, redirect
from forms import CadastroForm
from db import db_query, db_insert
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)

app.config['SECRET_KEY'] = "ABC123"
csrf.init_app(app)


@csrf.exempt
@app.route('/', methods=('GET', 'POST'))
def index():
    form = CadastroForm()
    if form.validate_on_submit():
        db_insert(
            "INSERT INTO [dbo].[Cadastro] (nome, sobrenome, email) VALUES ('" + form.nome.data + "','" + form.sobrenome.data + "','" + form.email.data + "');")
        return redirect("/consulta")
    return render_template('index.html', form=form)


@app.route('/consulta')
def consulta():
    query = db_query("SELECT * FROM [dbo].[Cadastro];")
    return render_template('consulta.html', query=query)


if __name__ == '__main__':
    app.run()
