from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

def kelime_goster(txt_dosyasi):
    with open(txt_dosyasi, 'r', encoding='utf-8') as dosya:
        metin = dosya.read().split()

    return metin

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kelimeler')
def kelimeler():
    dosya_adi = "b.txt"  # Metin dosyasının adı
    kelimeler = kelime_goster(dosya_adi)
    return jsonify(kelimeler=kelimeler)

if __name__ == '__main__':
    app.run(debug=True)
