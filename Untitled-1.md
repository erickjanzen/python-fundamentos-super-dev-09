PARTE 1 - Classe Autor
==================================================

Classe:
Autor

Objetivo:
Criar uma classe para representar o autor de um livro.

O construtor deve receber os seguintes parâmetros:
- nome
- nacionalidade
- ano_nascimento

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Nome do autor
- Nacionalidade do autor
- Ano de nascimento do autor

Criar uma função chamada obter_descricao.

A função obter_descricao deve:
- Retornar uma string contendo o nome e a nacionalidade do autor

Exemplo de informação que poderá ser retornada:

Machado de Assis - Brasileiro

==================================================
PARTE 2 - Classe Livro
==================================================

Classe:
Livro

Objetivo:
Criar uma classe para representar um livro.

O construtor deve receber os seguintes parâmetros:
- titulo
- quantidade_paginas
- ano_publicacao
- autor

O parâmetro autor deverá receber um objeto da classe Autor.

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Título do livro
- Quantidade de páginas
- Ano de publicação
- Descrição do autor

Para apresentar a descrição do autor, a classe Livro deverá chamar a função obter_descricao do objeto autor.

Depois:

1. Instanciar 2 objetos da classe Autor
2. Instanciar 2 objetos da classe Livro
3. Passar um objeto Autor para cada objeto Livro
4. Chamar a função apresentar_dados de cada autor
5. Chamar a função apresentar_dados de cada livro

Importante:

Não preencher o autor do livro utilizando somente uma string.

Errado:

autor = "Machado de Assis"

O atributo autor da classe Livro deverá receber um objeto da classe Autor.