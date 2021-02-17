from flask import Flask, render_template, url_for, request, jsonify, redirect, flash
import requests
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recherche', methods=['GET', 'POST'])
def recherche():
    if request.method == 'POST':
        if request.form['choix'] == 'filiere':
            filiere = request.form['filiere']
            url = f"http://127.0.0.1:5000/api/filiere/<string:filiere>?filiere={filiere}"
            response = requests.get(url).json()
            return render_template('data_response.html', response=response)

        if request.form['choix'] == 'region':
            region = request.form['regions']
            url = f"http://127.0.0.1:5000/api/region/<string:region>?region={region}"
            response = requests.get(url).json()
            return render_template('data_response.html', response=response)

        if request.form['choix'] == 'both':
            filiere = request.form['filiere2']
            region = request.form['regions2']
            url = f"http://127.0.0.1:5000/api/filiere_region/<string:filiere>/<string:region>?filiere={filiere}&region={region}"
            response = requests.get(url).json()
            return render_template('data_response.html', response=response)

    url = "http://127.0.0.1:5000/api/regions"
    regions = requests.get(url).json()
    return render_template('recherche.html', listeRegions=regions)


@app.route('/recherche/<string:recordid>/update', methods=['GET','POST'])
def update(recordid):
    url = f"http://127.0.0.1:5000/api/get_doc/<string:recordid>?recordid={recordid}"
    response = requests.get(url).json()
    if request.method == 'POST':
        conso = request.form['conso']
        url = f"http://127.0.0.1:5000/api/update_doc/<string:recordid>/<float:conso>?recordid={recordid}&conso={conso}"
        response = requests.put(url).json()
        flash(f"{response['alert']}")
        return redirect(url_for('recherche'))
    return render_template('update.html', response=response)

@app.route('/recherche/<string:recordid>/delete', methods=['GET','DELETE'])
def delete(recordid):
    url = f"http://127.0.0.1:5000/api/delete_doc/<string:recordid>?recordid={recordid}"
    response = requests.delete(url).json()
    flash(f"{response['alert']}")
    return redirect(url_for('recherche'))


@app.route('/consommation', methods=['GET','POST'])
def consommation():
    if request.method == 'POST':
        if request.form['choix'] == 'filiere':
            filiere = request.form['filiere']
            url = f"http://127.0.0.1:5000/api/conso_filière/<string:filiere>?filiere={filiere}"
            response = requests.get(url).json()
            response[0]['consommation'] = round(response[0]['consommation'], 2)
            return render_template('conso_response.html', response_conso=response)

        if request.form['choix'] == 'region':
            region = request.form['regions']
            url = f"http://127.0.0.1:5000/api/conso_reg/<string:region>?region={region}"
            response = requests.get(url).json()
            response[0]['consommation'] = round(response[0]['consommation'], 2)
            return render_template('conso_response.html', response_conso=response)

        if request.form['choix'] == 'both':
            filiere = request.form['filiere2']
            region = request.form['regions2']
            url = f"http://127.0.0.1:5000/api/get_conso_filiere_region/<string:filiere>/<int:code>?filiere={filiere}&code={region}"
            response = requests.get(url).json()
            response[0]['consommation'] = round(response[0]['consommation'], 2)
            return render_template('conso_response.html', response_conso=response)
    
    url = 'http://127.0.0.1:5000/api/conso_filieres_regions'
    response = requests.get(url).json()

    conso_gaz = []
    conso_elec = []

    for dics in response:
        if dics['_id']['filiere'] == 'Gaz':
            conso_gaz.append([dics['_id']['region'], round(dics['consommation'], 2)])
        else:
            conso_elec.append([dics['_id']['region'], round(dics['consommation'], 2)])

    conso_gaz.sort(key= lambda elem: elem[0])
    conso_elec.sort(key= lambda elem: elem[0])

    no_gaz = ['Martinique', 'Guadeloupe', 'Guyane', 'Mayotte', 'La Réunion', 'Corse']
    sort_conso_elec = []
    for elec in conso_elec:
        if elec[0] not in no_gaz:
            sort_conso_elec.append(elec)
    for elec in conso_elec:
        if elec[0] in no_gaz:
            sort_conso_elec.append(elec)

    gaz = [elem[1] for elem in conso_gaz]
    elec = [elem[1] for elem in sort_conso_elec]
    categories = [elem[0] for elem in sort_conso_elec]

    url = "http://127.0.0.1:5000/api/regions"
    regions = requests.get(url).json()

    return render_template('consommation.html', gaz=gaz, elec=elec, region=categories, listeRegions=regions)


if __name__ == '__main__':
    app.run(port=5001, debug=True)