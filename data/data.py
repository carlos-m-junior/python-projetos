def obter_data():
    while True:
        data = input("Digite a data no formato DD/MM/AAAA: ")
        if validar_data(data):
            return data
        else:
            print("Data inválida. Certifique-se de que a data está no formato correto e tente novamente.")


def validar_data(data):
    if len(data) != 8:
        return False
    try:
        dia = int(data[:2])
        mes = int(data[2:4])
        ano = int(data[4:])
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2099:
            return True
        return False
    except ValueError:
        return False


def converter_data_para_extenso(data):
    dias = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]

    dia = data[:2]
    mes = int(data[2:4]) - 1
    ano = data[4:]

    return f"{dias[int(dia) - 1]} de {meses[mes]} de {ano}"


def listar_dados():
    datas = []
    while True:
        print("\nMenu:")
        print("1. Adicionar uma data")
        print("2. Listar datas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = obter_data()
            datas.append(converter_data_para_extenso(data))
            print("Data adicionada com sucesso.")
        elif opcao == "2":
            if datas:
                print("\nDatas cadastradas:")
                for data in datas:
                    print(f"- {data}")
            else:
                print("Nenhuma data cadastrada.")
        elif opcao == "3":
            print("Saindo da aplicação...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def main():
    listar_dados()


if __name__ == "__main__":
    main()
