# -*- coding: utf-8 -*-
"""Cupom.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DT9Zk3hjmTBsWfrWTQQat8axqo9f66fW
"""

from time import sleep
print('-'*50)
print('Vamos calcular o preço de sua passagem com base na tabela abaixo:')
print('\nViagens  de até 200KM --------------- R$0.50 por Km.\n'
      'Viagens acima de 200Km --------------- R$0.45 por Km.')
print('-'*50)
sleep(2)
dis = float(input('\nQual a distância de sua viagem em km? '))
print('CALCULANDO...')
sleep(2)
if dis <= 200:
    print('O preço da passagem é R$', dis * 0.50)
if dis > 200:
    print('O preço da passagem é R$', dis * 0.45)
print('-'*25, 'BOA VIAGEM!', '-'*25)