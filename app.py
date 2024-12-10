from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def hash_text(text, algo='sha256'):
    """Hash le texte en utilisant l'algorithme spécifié (par défaut SHA-256)."""
    hash_obj = hashlib.new(algo)
    hash_obj.update(text.encode('utf-8'))
    return hash_obj.hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    hashed_text = None
    if request.method == 'POST':
        text = request.form['text']
        algorithm = request.form['algorithm']
        hashed_text = hash_text(text, algorithm)
    return render_template('index.html', hashed_text=hashed_text)

if __name__ == '__main__':
    app.run(debug=True)