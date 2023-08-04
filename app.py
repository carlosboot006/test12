from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abrir_pasta_download')
def abrir_pasta_download():
    diretorio_download = '/sdcard/Download'  # substitua pelo diretório correto da pasta de download do Android
    os.system(f'xdg-open {diretorio_download}')
    return ''

if __name__ == '__main__':
    app.run()
