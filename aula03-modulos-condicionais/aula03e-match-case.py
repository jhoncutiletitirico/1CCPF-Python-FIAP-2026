escolha_usuario = 1
# 0 -> Sair do programa
# 1 -> Entrar no programa
# >>>> Erro!!


match escolha_usuario:
    case 0:
        status = "Sair do programa"
    case 1:
        status = "Entrar no programa"
    case _:
        status = "Error"