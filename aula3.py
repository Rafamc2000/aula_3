#x = input('digite a estrutura: ')

#if x == 'mt':
#    print('estrutura primaria')
#elif x == 'bt':
#    print('estr sec')
#elif x == 'btmt':
#   print('estr sec e primaria')
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

#tp1 = int(input("insira uma temperatura: "))
    
#if tp1 >=30:
#    print("temperatura 1 alta")
#elif tp1 <30 and tp1 >20:
#    print("temperatura 1 dentro do normal")
#elif tp1 <20:
#    print("temperatura 1 abaixo do normal")
#else:
#    print("insira novamente um valor")
    
#tp2 = int(input("insira uma temperatura: "))
    
#if tp2 >=30:
#    print("temperatura 2 alta")
#elif tp2 <30 and tp2 >20:
#    print("temperatura 2 dentro do normal")
#elif tp2 <20:
#    print("temperatura 2 abaixo do normal")
#else:
#    print("insira novamente um valor")


#python aula3.py


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

#lista = {'Rafael':5000 , 'Adriano': 9000}
#print(f'O salario de Rafael é ', lista['Rafael'] , 'e o de Adriano é' , lista['Adriano'])

#adicionar = lista.insert(0 , 0)
#print(lista)




### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
#import re

#def validar_email(email):
    
 #   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  #  if re.fullmatch(regex, email):
   #     return True
    #else:
   #     return False
#email = input("Digite seu e-mail: ")
#if validar_email(email):
 #   print(f"O e-mail {email} é válido.")
#else:
#    print(f"O e-mail {email} não é válido.")

#idade = int(input("digite sua idade: "))

#if idade <18:
#    print("pela sua idade voce nao participara")
#elif idade >65:
#    print("pela sua idade voce nao participara")
#else:
#    print("Usuario cadastrado,idade:" , idade)

 #   print("email cadastrado: ", email)



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

#transacao = {'valor': 9000, 'hora': 11}

#if transacao['valor'] >10000 or transacao['hora'] <9 or transacao['hora'] >18:
#    print("transação suspeita!!!")
#else :
#    print("transação aceita")



### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

#from collections import Counter

#texto = "Aqui temos muitas palavras e muitas mesmo!"
#palavras = texto.lower().split()  # Converte para minúsculas e divide por espaços
#contagem_palavras = Counter(palavras)
#print(contagem_palavras)




### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

##numeros = [10, 20, 30, 40, 50]
#minimo = min(numeros)
##maximo = max(numeros)
#normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

#print(normalizados)





### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

#usuarios = [
 #   {"nome": "Alice", "email": "alice@example.com"},
 #   {"nome": "Bob", "email": ""},
 #   {"nome": "Carol", "email": "carol@example.com"}
#]

#usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

#print(usuarios_validos)




### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

#numeros = [2,3,4,5,6,7,8,9,8,12,213,134,234,234,3453,2000]

#pares = [numero for numero in numeros if numero % 2 == 0]

#print(pares)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria. @@@DUVIDA NO TOTAL_POR_CATEGORIA = {}

#vendas = [
 #   {"categoria": "eletrônicos", "valor": 1200},
  #  {"categoria": "livros", "valor": 200},
   # {"categoria": "eletrônicos", "valor": 800}
#]

#total_por_categoria = {}
#for venda in vendas:
 #   categoria = venda["categoria"]
 #   valor = venda["valor"]
 #  if categoria in total_por_categoria:
 #       total_por_categoria[categoria] += valor
 #   else:
 #      total_por_categoria[categoria] = valor

#print(total_por_categoria)



### Exercícios com WHILE

#import time

#while True:
    #print("Verificando novos dados...")
    # Aqui você pode adicionar o código para verificar novos dados,
    # por exemplo, checar a existência de novos arquivos em um diretório,
    # fazer uma consulta a um banco de dados ou API, etc.
    
 #   time.sleep(10)  # Pausa o loop por 10 segundos




### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#entrada = str(input("digite: "))

#while entrada != ("sair"):
# entrada=input("digite 'sair' para fechar: ")
#if entrada == ("sair"):
#    exit()



### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

#numero = float(input("insira numero entre 20 e 50:"))

#while numero <20:
#    print("numero fora do limite,insira outro numero")
#    numero = float(input("insira numero entre 20 e 50:"))
#    if numero >50:
#       print("numero fora do limite,insira outro numero")
#    numero = float(input("insira numero entre 20 e 50:")) 
#else: 
#    print("parabens,seu numero é:",numero)




### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

#pagina_atual = 1
#paginas_totais = 5  # Simulação, na prática, isso viria da API

#while pagina_atual <= paginas_totais:
#    print(f"Processando página {pagina_atual} de {paginas_totais}")
#    # Aqui iria o código para processar os dados da página
#    pagina_atual += 1

#print("Todas as páginas foram processadas.")





### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

#tentativas_maximas = 5
#tentativa = 1

#while tentativa <= tentativas_maximas:
#    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
#    if True:  # Suponha que a conexão foi bem-sucedida
 #       print("Conexão bem-sucedida!")
  #      break
   # tentativa += 1
#else:
 #   print("Falha ao conectar após várias tentativas.")
    




### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.


itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1

 