def verificador_media (media: int|float) -> str:
    """Esta função retorna se o aluno passou ano"""


    
    if isinstance(media, int):
        raise TypeError("Tipo invalido, a entrada deve ser numerica")
    



    if media >= 7:
        return "Aprovado"
    
    elif media < 4:
        return "Reprovado"
    
    else:
        raise ValueError("Entrada Invalida")
    


    






if __name__ == "__main__":
    print(verificador_media(7))
    