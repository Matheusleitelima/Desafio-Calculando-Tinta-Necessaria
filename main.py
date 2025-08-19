import math
def calcular(litro_lata, altura, largura):

    area = altura * largura
    quantidade_certa = area / litro_lata
    latas_certa = math.ceil(quantidade_certa) #arrendoda para numero inteiro

    return print(f'Você necessita de {latas_certa} latas de tinta')



rendimento_tinta = float(input('Digite o redimento da lata: '))
altura_parede = float(input('Digite a altura da parede: '))
largura_parede = float(input('Digite a largura da parede: '))

calcular(rendimento_tinta, altura_parede, largura_parede)
