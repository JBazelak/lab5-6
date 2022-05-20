import numpy as np
#zad1
#a = np.array([2, 5, 3])
#b = np.array([3, 0, 8])
# print(a * b)
#zad 2
# c = np.array([4, 6, 12, 65, 54, 90, 4, 11, 31]).reshape(3, 3)
# d = np.arange(16).reshape((4, 4))
#
# print(c.min(axis=0))
# print(c.min(axis=1))
# print(d.min(axis=0))
# print(d.min(axis=1))

#zad 3
#print(a.dot(b))

#zad4
# calkowite = np.array([2, 4, 6])
# rzeeczywiste = np.array([np.e, np.sqrt(2), 1.618])
# print(calkowite * rzeeczywiste)

#zad5
# arr = np.arange(6).reshape(2, 3)
# a = np.sin(arr)
# a = np.around(a, 2)
# print('macierz z zad 5: \n',a)
#
# #zad 6
# arc = np.arange(6).reshape(2, 3)
# b = np.cos(arc)
# b = np.around(b, 2)
# print('macierz z zad 6: \n', b)
#
# #zad 7
#
# def funkcja(arr5, arr6):
#     print('macierz z zad 7: \n', arr5 + arr6)
#
# funkcja(a, b)

#zad 8

# s = np.arange(9).reshape(3, 3)
# for i in s:
#     print(i)
#     print("")
# for j in s.T:
#         print(j)
#         print("")

#zad 9

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# for i in a.flat:
#     print(i)

#zad 10
# b = []
# a = np.arange(81).reshape(9, 9)
#
# print(a)
# print("")
# for i in range(1, 82):
#     if 81 % i == 0:
#         for x in range(1,82):
#             if x * i == 81 and x * x != 81:
#                 b.append(x)
#
# print("mamy ", len(b), " możliwości")
#
# for i in b:
#     for j in reversed(b):
#         if i * j == 81:
#             print(i, 'x', j)
# print("")
# print(a.reshape(27,3))

#macierz 9x9 ma 81 elementów więc przekszatałcone macierze tez muszą tyle elementów zawierać
#pętla nr 1 wyrzuca 4 wartosci: 1,3,27,81 (z wyłączeniem 9 bo macierz 9x9 juz mamy)
# które po przemnorzeniu przez siebie dają wynik 81 zatem mamy 4 kombinacje które wyświetla petla nr 2

#zad11

# a = np.arange(12).reshape(3, 4)
# b = a.reshape(4,3)
# c = a.reshape(2, 6)
#
# print(a.flat)
# print(b.flat)
# print(c.flat)

#wartosci identyczne


#####PANDAS######
import pandas as pd

#zad 1

xls = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xls)
# print(df)

###zad 2

#pkt1
# print(df[df['Liczba'] > 1000])

#pkt2
# print(df[df['Imie'] == 'JAKUB'])

#pkt3
# print(sum(df['Liczba']))

#pkt4

#PKT5
# m = len(df[df['Plec'] == 'M'])
# print('Urodzonych chlopcow: ', m)
# k = len(df[df['Plec'] == 'K'])
# print('Urodzonych dziewczynek: ',k)

#pkt 6
#pkt 7

###Zad3

data = pd.read_csv('zamowienia.csv',header=0, sep=';',decimal=',')
print(data)

#pkt 1
print(data.Sprzedawca.is_unique)
#pkt 2
# print(data.sort_values(by='Utarg', ascending=True,  na_position='last').head(5))
