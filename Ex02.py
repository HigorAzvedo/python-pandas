import pandas as pd

anos = []
nacionalidades = []
nome_pilotos = []
equipes = []

def leArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    tamanho = arquivo.readlines()
    
    cont = 0
    while(len(tamanho) > cont):
        linha = tamanho[cont]
        dados = linha.split(";")
        anos.append(int(dados[0]))
        nacionalidades.append(dados[1])
        nome_pilotos.append(dados[2].replace("1","").strip())
        equipes.append(dados[3].strip())
        cont += 1  
    arquivo.close()

leArquivo("./assets/formula1.txt")

df = pd.DataFrame({'Anos' : anos,
                   'Nacionalidade' : nacionalidades,
                   'Nome Piloto' : nome_pilotos,
                   'Equipes': equipes})

contagem_vitorias = df['Nome Piloto'].value_counts()
df['Títulos na Carreira'] = df['Nome Piloto'].map(contagem_vitorias)

print(df)
file_name = 'Formula1.xlsx'
df.to_excel(file_name)
file_name = 'Formula1.json'
df.to_json(file_name)