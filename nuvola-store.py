from flask import Flask, request, jsonify

app = Flask(__name__)

def trova_articolo(articolo):
    articoli = {
        "caricatori per cellulare": "I caricatori per cellulare si trovano nel reparto elettronica, sugli scaffali a sinistra.",
        "caricatori": "I caricatori si trovano nel reparto elettronica, sugli scaffali a sinistra.",
        "cavo-c": "I cavi di ricarica si trovano nel reparto elettronica, sugli scaffali a sinistra.",
        "caricatori iphone": "I caricatori per iPhone si trovano nel reparto elettronica, sugli scaffali a sinistra.",
        "caricatori android": "I caricatori per Android si trovano nel reparto elettronica, sugli scaffali a sinistra.",
        # Aggiungi altre categorie di articoli e relative posizioni qui
    }

    for key, value in articoli.items():
        if key in articolo.lower():
            return value

    return "Mi dispiace, l'articolo che stai cercando è esaurito."

@app.route('/cerca', methods=['POST'])
def cerca():
    query = request.json['query']
    risultato_ricerca = trova_articolo(query)
    return jsonify({'result': risultato_ricerca})

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)