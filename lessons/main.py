exemplo_string = f'Sítio do pica-pau amarelo \n 2023'

def separandoStringEmCaracteres(palavra):
    retorno = [caractere for caractere in palavra if caractere != ' ']
    print(retorno)

separandoStringEmCaracteres(exemplo_string)
