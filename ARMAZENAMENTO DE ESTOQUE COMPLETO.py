import datetime
try:
    with open("estoque.txt","r") as arquivo:
        estoque_atual = int(arquivo.read())
except:
    estoque_atual = 0

limite_maximo = 500
alerta_proximo = 450

print("--- SISTEMA DE FLUXO DE PATIO INICIADO---")

while True:
    print(f"\nEstoque agora: {estoque_atual} paletes")
    
    try:
        entrada = input("movimentacao ou digite 999 para sair: ")
        movimentacao = int(entrada)

        if movimentacao == 999:
            print("Encerrando sistema... Bom descanso!")
            break

        estoque_atual = estoque_atual + movimentacao

        with open("estoque.txt", "w") as arquivo:
            arquivo.write(str(estoque_atual))
        agora=    datetime.datetime.now().strftime("%D/%M/%Y, %H:%M:%S")
        relatorio= f"[{agora}]:{movimentacao} |EstoqueFinal:{estoque_atual}\n"
        with open ("historico.txt","a")as arquivo_hist:
            arquivo_hist.write(relatorio)    
        if estoque_atual >= limite_maximo:
            print("❌ STATUS: SETOR LOTADO! PARE O DESCARREGAMENTO.")
        elif estoque_atual >= alerta_proximo:
            print("⚠ STATUS: ATENCAO! ESTOQUE QUASE CHEIO!")
        else:
            print("✅ STATUS: LIBERADO. PODE CONTINUAR.")
    except ValueError:
        print("⚠ ERRO: Por favor, digite apenas NUMEROS inteiros!")