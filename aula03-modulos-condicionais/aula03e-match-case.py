escolha_usuario = 1
# 0 -> Sair do programa
# 1 -> Entrar no programa
# >>>> Erro!!


match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("erro!!")