from typing import Dict, Any

livro: Dict[str, Any] = {
    "Titulo": "Game of thrones",
    "Autor": "Estagiario",
    "Ano": 2005
}
print(livro["Ano"])

lista_completa = livro.items()

for chaves in lista_completa:
    print(chaves)

    



    #python aula4.py