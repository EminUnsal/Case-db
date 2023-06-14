from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('den.csv', delimiter=';')

@app.route('/betriebsstelle/<abkuerzung>')
def get_betriebsstelle(abkuerzung):
    betriebsstelle = data[data['Abk'] == abkuerzung]

    if betriebsstelle.empty:
        return jsonify({'error': 'Betriebsstelle nicht gefunden'})
    
    return jsonify({
        'Name': betriebsstelle['Name'].values[0],
        'Kurzname': betriebsstelle['Kurzname'].values[0],
        'Typ': betriebsstelle['Typ'].values[0]
        })

if __name__ == '__main__':
    app.run(debug=True)