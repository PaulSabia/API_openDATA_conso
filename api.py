from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import uvicorn
from connecteur import Connecteur

app = FastAPI()

#Recupère les données d'une filière 
@app.get('/api/filiere/<string:filiere>')
async def get_data_fil(filiere):
    result = Connecteur().get_data_fil(filiere)
    return jsonable_encoder(result)

#Recupère les données d'une région
@app.get('/api/region/<string:region>')
async def get_data_region(region):
    result = Connecteur().get_data_region(region)
    return jsonable_encoder(result)

#Recupère les données d'une région et d'une filière
@app.get('/api/filiere_region/<string:filiere>/<string:region>')
async def get_data_fil_reg(filiere, region):
    result = Connecteur().get_data_fil_reg(filiere, region)
    return jsonable_encoder(result)

#Recupère la consommation d'une fillière
@app.get('/api/conso_filière/<string:filiere>')
async def get_conso_fil(filiere):
    result = Connecteur().get_conso_fil(filiere)
    return jsonable_encoder(result)

#Recupère la consommation d'une région
@app.get('/api/conso_reg/<string:region>')
async def get_conso_reg(region):
    result = Connecteur().get_conso_reg(region)
    return jsonable_encoder(result)

#Obtenir un doc selon son recordid
@app.get('/api/get_doc/<string:recordid>')
async def get_doc(recordid):
    result = Connecteur().get_doc(recordid)
    return jsonable_encoder(result)

#Supprime un document selon son recordid
@app.delete('/api/delete_doc/<string:recordid>')
async def delete_doc(recordid):
    result = Connecteur().delete_doc(recordid)
    return jsonable_encoder(result)

#Update un document selon son recordid
@app.put('/api/update_doc/<string:recordid>/<float:conso>')
async def update_doc(recordid, conso):
    result = Connecteur().update_doc(recordid, conso)
    return jsonable_encoder(result)

#Recupère la consommation d'une filière et d'un département
@app.get('/api/get_conso_filiere_region/<string:filiere>/<int:code>')
async def get_conso_filiere_region(filiere, code):
    result = Connecteur().get_conso_filiere_region(filiere, code)
    return jsonable_encoder(result)

#Récupère le consommation par filière pour chaque région
@app.get('/api/conso_filieres_regions')
async def get_conso_regs_fils_for_charts():
    result = Connecteur().get_conso_regs_fils_for_charts()
    return jsonable_encoder(result)

#Récupère les regions distincts
@app.get('/api/regions')
async def get_regions():
    result = Connecteur.get_regions()
    return jsonable_encoder(result)

if __name__ == '__main__':
    uvicorn.run("api:app", host="127.0.0.1", port=5000, reload=True)