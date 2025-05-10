#x = input('digite a estrutura: ')

#if x == 'mt':
#    print('estrutura primaria')
#elif x == 'bt':
#    print('estr sec')
#elif x == 'btmt':
#    print('estr sec e primaria')
#else:
#    print('nao reconheço a estrutura')

#python aula3.py
#quantidade = 2
#preço = -4

#if quantidade <0:
#    print('ta abaixo do valor')
#elif preço <0:
#    print('abaixo do preço tambem')
#elif quantidade and preço >0:
#    print('ta no preço')

#lista_frutas = ['cereja' , 'laranja' , 'banana']
#lista_vendedores = ['fabio' , 'rafael' , 'nassau']

# python aula3.py
#for frutas in lista_frutas:
#    print(frutas)
#for vendedores in lista_vendedores:
#    print(vendedores)

#brasil = []
#estado1 = {'estado':'São Paulo' , 'cidade': 'Franca'}
#estado2 = {'estado': 'Rio de Janeiro' , 'cidade': 'Cabo frio'}

#brasil.append(estado1)
#brasil.append(estado2)

#print(f'como melhor estado do Brasil temos' , brasil[0]["estado"] , 'e segundo melhor' , brasil[1]["estado"])
#python aula3.py

#estado = dict()
#brasil = list()
#for tabela in range(0, 2):

 #   estado['uf'] = str(input('unidade federativa: '))
  #  estado['sigla'] = str(input('sigla: '))
   # brasil.append(estado.copy())
#for e in brasil:
#    print(e)

#nome = str(input('digite o nome:'))
#media = int(input('qual sua média: '))

#if media <=5:
#    print('reprovado')
#elif media >5:
#    print('aprovado,parabens!')
#python aula3.py

####exercicios


### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.


#quantidade =int(input("insira um valor: "))
#preço =int(input("insira um preço: "))

#if quantidade < 0:
#    print("valores negativos na tabela quantidade")
#elif preço <0:
#    print("valores negativos na tabela preço")
#else:
#    print("valores positivios na tabela")

#python aula3.py
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

tp1 = int(input("insira uma temperatura: "))
tp2 = int(input("insira uma temperatura:"))

if tp1 >=30:
    print("temperatura alta")
elif tp1 <30 >20:
    print("temperatura dentro do normal")
elif tp1 <20:
    print("temperatura abeixo do normal")
elif tp2 >=30:
    print("temperatura alta")
elif tp2 <30 >20:
    print("temperatura dentro do normal")
elif tp3 <20:
    print("temperatura abeixo do normal")



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
