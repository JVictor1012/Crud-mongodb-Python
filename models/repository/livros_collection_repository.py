from typing import Dict, List
from bson.objectid import ObjectId
from datetime import timedelta

class LivrosRepository:
    def __init__(self, db_connection) -> None:
        self. __collection_name = "livros"
        self. __db_connection = db_connection
        
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents
    
    def busca_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.find_one(document)
        return document
    
    def busca_varios(self, filtro ) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filtro, 
        {"_id": 0}      #opções de retorno                 
        )
        
        response = []
        for elem in data:
            response.append(elem)
        
        return response
    
    def busca_if_exists(self, filtro) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ filtro: { "$exists": True } })
        for elem in data: print(elem)
        
    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            { "name": "Lhama" }, # Filtro
            { "endereco": 0, "_id": 0 } # Opcoes de retorno
        ).sort([("pedidos.pizza", 1)]) #1 crescente e -1 decrescente

        for elem in data: print(elem)
        
    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "$or": [{ "tittle": "Sherlock" }, { "ano": { "$exists": True } }] }, {"_id": 0})
        for elem in data:
            print(elem)
            print()
            
    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "_id": ObjectId("64e69a14b48db9698894f8ca") })
        for elem in data: print(elem)
        
    def edit_registry(self, id, propriedade) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one(
            { "_id": ObjectId(id) }, #Filtro
            { "$set": { "tittle": propriedade } } # Campo de edição
        )
        print(data.modified_count)
        
    def edit_many_registries(self, filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            filtro, #Filtro
            { "$set": propriedades }
        )
        print(data.modified_count)
        
    def delete_many_registries(self, filtro) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(filtro)
        print(data.deleted_count)
    
    def delete_registry(self, filtro) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one(filtro)
        print(data.deleted_count)
        
    def create_index_ttl(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        tempo_de_vida = timedelta(seconds=10)
        collection.create_index("data_de_criacao", expireAfterSeconds=tempo_de_vida.seconds)