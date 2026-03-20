def verificador_media(media:int|float) -> str:

    # Testando para ver se a média é um número
    if not isinstance(media,(int,float)):
        raise TypeError("Tipo inválido, a entrada deve ser numérica")
    # Varificar se é menor que 0
    elif media < 0:
        raise ValueError ("O valor deve ser maior ou igual a 0 e menor ou igual a 10")
    # Varifica se é maior que 10
    elif media > 10:
        raise ValueError ("O valor deve ser maior ou igual a 0, e menor ou igual a 10")
    # Varifica se a média é maior ou igual a 7 para ser "Aprovado"
    elif media >= 7:
        return("Aprovado")
    # Verifica se a média é menor ou igual a 4 para ser "Reprovado"
    elif media <= 4:
        return("Reprovado")
    # Verifica se a média é maior ou igual a 5 e menor ou igual a 6 para ficar de "Recuperação"
    else:
        return("Recuperação")
    
    
    
if __name__ == "__main__":
    print(verificador_media(6))
