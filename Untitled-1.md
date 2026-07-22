==================================================
PARTE 2 - Classe Pessoa
==================================================

Classe:
Pessoa

Objetivo:
Criar uma classe para representar uma pessoa.

O construtor deve receber os seguintes parâmetros:
- nome
- idade
- telefone
- endereco

O parâmetro endereco deverá receber um objeto da classe Endereco.

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Nome da pessoa
- Idade da pessoa
- Telefone da pessoa
- Endereço completo da pessoa

Para apresentar o endereço, a classe Pessoa deverá chamar a função obter_endereco_completo do objeto endereco.

Criar uma função chamada verificar_maioridade.

A função verificar_maioridade deve:
- Verificar se a pessoa possui 18 anos ou mais
- Apresentar uma mensagem informando o resultado

Mensagens possíveis:

Pessoa maior de idade
Pessoa menor de idade

Depois:

1. Instanciar 2 objetos da classe Endereco
2. Instanciar 2 objetos da classe Pessoa
3. Passar um objeto Endereco para cada objeto Pessoa
4. Chamar a função apresentar_dados de cada endereço
5. Chamar a função apresentar_dados de cada pessoa
6. Chamar a função verificar_maioridade de cada pessoa



--------------------------------------------------
Ex.3 - Classes Cliente e Pedido
--------------------------------------------------

Objetivo:
Criar as classes Cliente e Pedido.

A classe Pedido deverá possuir um objeto da classe Cliente.

Relacionamento:

Um pedido tem um cliente.



==================================================
PARTE 1 - Classe Cliente
==================================================

Classe:
Cliente

Objetivo:
Criar uma classe para representar um cliente.

O construtor deve receber os seguintes parâmetros:
- nome
- cpf
- email

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Nome do cliente
- CPF do cliente
- E-mail do cliente

Criar uma função chamada obter_identificacao.

A função obter_identificacao deve:
- Retornar uma string contendo o nome e o CPF do cliente

Exemplo de informação que poderá ser retornada:

Mariana Silva - CPF: 000.000.000-00



==================================================
PARTE 2 - Classe Pedido
==================================================

Classe:
Pedido

Objetivo:
Criar uma classe para representar um pedido.

O construtor deve receber os seguintes parâmetros:
- numero
- produto
- quantidade
- valor_unitario
- cliente

O parâmetro cliente deverá receber um objeto da classe Cliente.

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Número do pedido
- Nome do produto
- Quantidade
- Valor unitário
- Identificação do cliente

Para apresentar a identificação do cliente, a classe Pedido deverá chamar a função obter_identificacao do objeto cliente.

Criar uma função chamada calcular_total.

A função calcular_total deve:
- Multiplicar a quantidade pelo valor unitário
- Retornar o valor total do pedido

Criar uma função chamada apresentar_total.

A função apresentar_total deve:
- Chamar a função calcular_total
- Apresentar o valor total do pedido

Depois:

1. Instanciar 2 objetos da classe Cliente
2. Instanciar 2 objetos da classe Pedido
3. Passar um objeto Cliente para cada objeto Pedido
4. Chamar a função apresentar_dados de cada cliente
5. Chamar a função apresentar_dados de cada pedido
6. Chamar a função apresentar_total de cada pedido

Importante:

Neste exercício, cada pedido terá somente um produto.

Não utilizar listas de produtos.



--------------------------------------------------
Ex.4 - Classes Professor e Curso
--------------------------------------------------

Objetivo:
Criar as classes Professor e Curso.

A classe Curso deverá possuir um objeto da classe Professor.

Relacionamento:

Um curso tem um professor.



==================================================
PARTE 1 - Classe Professor
==================================================

Classe:
Professor

Objetivo:
Criar uma classe para representar um professor.

O construtor deve receber os seguintes parâmetros:
- nome
- especialidade
- tempo_experiencia

O tempo de experiência deverá ser informado em anos.

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Nome do professor
- Especialidade
- Tempo de experiência

Criar uma função chamada obter_apresentacao.

A função obter_apresentacao deve:
- Retornar uma string contendo o nome e a especialidade do professor

Exemplo de informação que poderá ser retornada:

Francisco - Especialista em Python



==================================================
PARTE 2 - Classe Curso
==================================================

Classe:
Curso

Objetivo:
Criar uma classe para representar um curso.

O construtor deve receber os seguintes parâmetros:
- nome
- carga_horaria
- quantidade_alunos
- professor

O parâmetro professor deverá receber um objeto da classe Professor.

Criar uma função chamada apresentar_dados.

A função apresentar_dados deve apresentar:
- Nome do curso
- Carga horária
- Quantidade de alunos
- Apresentação do professor

Para apresentar o professor, a classe Curso deverá chamar a função obter_apresentacao do objeto professor.

Criar uma função chamada verificar_duracao.

A função verificar_duracao deve:
- Verificar a carga horária do curso
- Apresentar uma mensagem de acordo com a carga horária

Regras:

- Curso com menos de 40 horas: curso de curta duração
- Curso com 40 horas ou mais: curso de longa duração

Mensagens possíveis:

Curso de curta duração
Curso de longa duração

Depois:

1. Instanciar 2 objetos da classe Professor
2. Instanciar 2 objetos da classe Curso
3. Passar um objeto Professor para cada objeto Curso
4. Chamar a função apresentar_dados de cada professor
5. Chamar a função apresentar_dados de cada curso
6. Chamar a função verificar_duracao de cada curso





==================================================
REGRAS GERAIS
==================================================

- Criar uma classe separada para cada elemento
- Utilizar o construtor __init__ em todas as classes
- Utilizar self para acessar os atributos
- Criar funções dentro das classes
- Criar métodos com retorno
- Criar métodos sem retorno
- Instanciar os objetos diretamente no código
- Passar objetos como parâmetros dos construtores
- Não substituir os objetos por strings
- Não utilizar listas
- Não utilizar for
- Não utilizar while
- Não utilizar input
- Os dados devem ser preenchidos diretamente no código
- Testar um exercício por vez
- Utilizar nomes de objetos diferentes e fáceis de identificar
- Não copiar os dados apresentados nos exemplos
- Criar seus próprios autores, livros, pessoas, endereços, clientes, pedidos, professores e cursos
"""