from models.connection_options.connection import DBConnectionHandler
from models.repository.livros_collection_repository import LivrosRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

livrosRepository = LivrosRepository(db_connection)

#collection.insert_one({
#    "tittle": "O Guia do Mochileiro das Galaxias",
#    "author": "Douglas Adams",
#    "Editora": "Arqueiro"
#})

livro = {
    "tittle":"Herobrine a lenda",
    "author":"Pac e Mike",
    "Editora":"Editora Jovem"
}

list_of_livros = [
    {
    "tittle":"Sertoes veredas",
    "author":"muito bom",
    "Editora":"Essa Mesmo"
    },
    {
    "tittle":"Sherlock",
    "author":"Arthur",
    "Editora":"Watson"
    }
]

#livrosRepository.insert_list_of_documents(list_of_livros)
#livrosRepository.insert_list_of_documents(list_of_livros)

livrosRepository.busca_varios(livro)



print(livrosRepository.edit_registry("64e69a14b48db9698894f8ca", "Sherlock Holmes"))