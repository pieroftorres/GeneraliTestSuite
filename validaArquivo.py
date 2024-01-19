nome_arquivo = "teste.txt"


with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    
    # Processar linhas intermediárias
    for linha in linhas[1:-1]:
        if linha.startswith('1'):
            cpf = linha[0:10].strip()    # Ler e limpar o campo de CPF
            print(cpf)