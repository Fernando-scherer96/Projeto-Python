# Projeto-Python
 #Calculo da malha-terra de uma subestação elétrica
 '''
Projeto de Malha-Terra
'''
from math import sqrt
s = 0
while True:
    tensão = float(input('Tensão de malha: '))
    Icc_max = float(input('Corrente CC máxima: '))
    Imalha = float(input('Corrente de malha: '))
    h = float(input('Profundidade: '))
    print('Calculo da Área\n.')
    d1 = int(input('D1 [m]: '))
    d2 = int(input('D2 [m]: '))
    dimensão = d1*d2
    print(f'Há Área = {dimensão}')
    tempo = float(input('Tempo de proteção: '))
    tamb = float(input('Temperatura Ambiente (°C): '))
    tmax = float(input('Temperatura de Solda: '))
    print('''
    Solo     Profundidade   Resistividade
    [H1]       0.8             520
    [H2]       1.2             440
    [H3]       1.8             290
    [H4]        -              180
    [Brita]    0.15            3000
    ''')
    l1 = float(input('H1 [m]: '))
    l2 = float(input('H2 [m]: '))
    Brita = 0.15
    p1 = float(input('P1 [ohms/m]: '))
    p2 = float(input('P2 [ohms/m]: '))
    pa = (l1+l2)/((l1/p1)+(l2/p2))
    ps = 3000
    k = (pa-ps)/(pa+ps)
    n = int(input('Para o calculo de Cs(hs,k): '))
    for c in range(1, n):
        s(c) = (k ** n)/(sqrt(1+((2*n*h/0.08) ** 2)))
    cs = (1/0.96)*(1+2*(soma(s)))
    print(cs)
    parar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if parar == 'N':
        break

