agenda = []  # Variável para armazenar os contatos
# Variável para marcar uma alteração na agenda
alterada = False


def pede_nome(padrao=""):
    """Solicita ao usuário um nome e retorna o valor, ou um padrão se não for fornecido."""
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
    return nome


def pede_telefone(padrao=""):
    """Solicita ao usuário um telefone e retorna o valor, ou um padrão se não for fornecido."""
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
    return telefone


def pede_endereco(padrao=""):
    """Solicita ao usuário um endereço e retorna o valor, ou um padrão se não for fornecido."""
    endereco = input("Endereço: ")
    if endereco == "":
        endereco = padrao
    return endereco


def pede_cidade(padrao=""):
    """Solicita ao usuário uma cidade e retorna o valor, ou um padrão se não for fornecido."""
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrao
    return cidade


def pede_uf(padrao=""):
    """Solicita ao usuário uma UF e retorna o valor, ou um padrão se não for fornecido."""
    uf = input("UF: ")
    if uf == "":
        uf = padrao
    return uf


def mostra_dados(nome, telefone, endereco, cidade, uf):
    """Exibe os dados do contato formatados."""
    print(f"Nome: {nome} | Telefone: {telefone} | Endereço: {endereco} | Cidade: {cidade} | UF: {uf}")


def pede_nome_arquivo():
    """Solicita ao usuário o nome do arquivo para salvar ou carregar a agenda."""
    return input("Nome do arquivo: ")


def pesquisa(nome):
    """Pesquisa um contato pelo nome e retorna a posição na lista, se encontrado."""
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def verifica_nome_existente(nome):
    """Verifica se o nome já existe na agenda."""
    if pesquisa(nome) is not None:
        print("Erro: Nome já existe na agenda.")
        return True
    return False


def novo():
    """Adiciona um novo contato à agenda."""
    global agenda, alterada
    nome = pede_nome()

    # Verifica se o nome já existe
    if verifica_nome_existente(nome):
        return  # Retorna se o nome já existir

    telefone = pede_telefone()
    endereco = pede_endereco()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, endereco, cidade, uf])
    alterada = True


def confirma(operacao):
    """Solicita a confirmação do usuário para uma operação (S/N)."""
    while True:
        opcao = input(f"Confirma {operacao} (S/N)? ").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")


def apaga():
    """Remove um contato da agenda."""
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")


def altera():
    """Altera os dados de um contato existente."""
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        endereco = agenda[p][2]
        cidade = agenda[p][3]
        uf = agenda[p][4]
        print("Encontrado:")
        mostra_dados(nome, telefone, endereco, cidade, uf)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor

        # Verifica se o novo nome já existe na agenda
        if verifica_nome_existente(nome) and nome.lower() != agenda[p][0].lower():
            return  # Retorna se o nome já existir e não for o mesmo

        telefone = pede_telefone(telefone)
        endereco = pede_endereco(endereco)
        cidade = pede_cidade(cidade)
        uf = pede_uf(uf)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, endereco, cidade, uf]
            alterada = True
    else:
        print("Nome não encontrado.")


def lista():
    """Lista todos os contatos na agenda."""
    print("\nAgenda\n\n------")
    for posicao, e in enumerate(agenda):
        print(f"Posição: {posicao} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")


def lê_última_agenda_gravada():
    """Lê a última agenda gravada e a carrega, se existir."""
    ultima = ultima_agenda()
    if ultima is not None:
        leia_arquivo(ultima)


def ultima_agenda():
    """Retorna o nome do último arquivo de agenda gravado."""
    try:
        arquivo = open("ultima_agenda.dat", "r", encoding="utf-8")
        ultima = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        return None
    return ultima


def atualiza_última(nome):
    """Atualiza o nome do último arquivo gravado."""
    arquivo = open("ultima_agenda.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")
    arquivo.close()


def leia_arquivo(nome_arquivo):
    """Lê os contatos de um arquivo e os adiciona à agenda."""
    global agenda, alterada
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone, endereco, cidade, uf = l.strip().split("#")
        agenda.append([nome, telefone, endereco, cidade, uf])
    arquivo.close()
    alterada = False


def lê():
    """Lê a agenda de um arquivo e atualiza a última agenda gravada."""
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)


def ordena():
    """Ordena a agenda por nome."""
    global alterada
    agenda.sort(key=lambda e: e[0])  # Ordena usando o nome (primeiro elemento da lista)
    alterada = True


def grava():
    """Grava a agenda em um arquivo."""
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")  # Salva todos os dados
    arquivo.close()
    atualiza_última(nome_arquivo)
    alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    """Valida se a entrada do usuário está dentro de um intervalo especificado."""
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


def menu():
    """Exibe o menu de opções para o usuário e retorna a escolha."""
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)


# Lê a última agenda gravada ao iniciar o programa
lê_última_agenda_gravada()

# Loop principal do programa
while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        lê()
    elif opcao == 7:
        ordena()