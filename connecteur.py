from pymongo import MongoClient
from bson import ObjectId

class Connecteur:
    @classmethod
    def connexion(cls):
        cls.client = MongoClient('mongodb+srv://user:user@promessededon.sw4vx.mongodb.net/<dbname>?retryWrites=true&w=majority')
        cls.db = cls.client.OpenData_ORE
        cls.col = cls.db.conso_annuel

    @classmethod
    def deconnexion(cls):
        cls.client.close()

    @classmethod
    def get_data_fil(cls, filiere):
        cls.connexion()
        result = list(cls.col.find({'fields.filiere': filiere},{'_id':0, 'recordid':1, 'fields.filiere':1, 'fields.libelle_region':1, 'fields.libelle_departement':1, 'fields.libelle_commune':1, 'fields.operateur':1, 'fields.conso':1, 'record_timestamp':1}))
        cls.deconnexion()
        return result[:20]

    @classmethod
    def get_data_region(cls, region):
        cls.connexion()
        result = list(cls.col.find({'fields.libelle_region': region}, {'_id':0, 'recordid':1, 'fields.filiere':1, 'fields.libelle_region':1, 'fields.libelle_departement':1, 'fields.libelle_commune':1, 'fields.operateur':1, 'fields.conso':1, 'record_timestamp':1}))
        cls.deconnexion()
        return result[:20]

    @classmethod
    def get_data_fil_reg(cls, filiere, region):
        cls.connexion()
        result = list(cls.col.find({'$and': [{'fields.filiere': filiere}, {'fields.libelle_region': region}]}, {'_id': 0, 'recordid':1, 'fields.filiere':1, 'fields.libelle_region':1, 'fields.libelle_departement':1, 'fields.libelle_commune':1, 'fields.operateur':1, 'fields.conso':1, 'record_timestamp':1}))
        cls.deconnexion()
        return result[:20]

    @classmethod
    def get_conso_fil(cls, filiere):
        cls.connexion()
        result = list(cls.col.aggregate([{'$match':{'fields.filiere': filiere}}, {'$group': {'_id': {'filiere': '$fields.filiere'}, 'consommation': {'$sum': '$fields.conso'}}}]))
        cls.deconnexion()
        return result

    @classmethod
    def get_conso_reg(cls, region):
        cls.connexion()
        result = list(cls.col.aggregate([{'$match':{'fields.libelle_region': region}}, {'$group': {'_id': {'region': '$fields.libelle_region'}, 'consommation': {'$sum': '$fields.conso'}}}]))
        cls.deconnexion()
        return result

    @classmethod
    def get_doc(cls, recordid):
        cls.connexion()
        result = cls.col.find_one({'recordid':recordid}, {'_id': 0})
        cls.deconnexion()
        return result

    @classmethod
    def delete_doc(cls, recordid):
        cls.connexion()
        cls.col.delete_one({'recordid': recordid})
        cls.deconnexion()
        result = {'alert': 'Elément supprimé !'}
        return result

    @classmethod
    def update_doc(cls, recordid, conso):
        cls.connexion()
        cls.col.update({'recordid': recordid}, {'$set': {'fields.conso': float(conso)}})
        cls.deconnexion()
        result = {'alert': 'Elément modifié !'}
        return result

    @classmethod
    def get_conso_filiere_region(cls, filiere, region):
        cls.connexion()
        result = list(cls.col.aggregate([{'$match': {'$and': [{'fields.filiere': filiere}, {'fields.libelle_region': region}]}}, {'$group': {'_id': {'filiere': '$fields.filiere', 'region': '$fields.libelle_region'}, 'consommation': {'$sum': '$fields.conso'}}}]))
        cls.deconnexion()
        return result

    @classmethod
    def get_conso_regs_fils_for_charts(cls):
        cls.connexion()
        result = list(cls.col.aggregate([{'$group': {'_id':{'region': '$fields.libelle_region', 'filiere': '$fields.filiere'}, 'consommation': {'$sum': '$fields.conso'}}}]))
        cls.deconnexion()
        return result

    @classmethod
    def get_regions(cls):
        cls.connexion()
        result = list(cls.col.distinct('fields.libelle_region'))
        cls.deconnexion()
        return result