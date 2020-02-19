from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = MySQL(app)

# usuario1 = Usuario('luan', 'Luan Marques', '1234')
# usuario2 = Usuario('Nico', 'Nico Steppat', '7a1')
# usuario3 = Usuario('flavio', 'flavio Almeida', 'javascript')

# usuarios = {usuario1.id: usuario1,
#             usuario2.id: usuario2,
#             usuario3.id: usuario3}

# jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
# jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
# lista = [jogo1, jogo2]
from views import *
if __name__ == '__main__':
    app.run(debug=True)
