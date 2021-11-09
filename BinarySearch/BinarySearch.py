# -*- coding: utf-8 -*-
import random
from numpy import around

def random_number(L,C):
    random_list = []

    for i in range(L):
        random_number = random.randint(0,C)
        random_list.append(random_number)
    return random_list

def binary_search(numbers,number_to_find,low,high):

    if low > high:
        return False
    mid = int(around((low + high) / 2))

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers,number_to_find,low,mid-1)
    else:
        return binary_search(numbers,number_to_find,mid+1,high)

if __name__ == '__main__':

    number_to_find = int(input('Ingresa Un Numero: '))
    L = int(input('Ingrese La Longitud De La Lista: '))
    C = int(input('Ingrese El Maximo Numero Aleatorio: '))

    numbers = random_number(L,C)
    numbers.sort()
    print(numbers)

    binary_search(numbers,number_to_find,0,len(numbers)-1)

    result = binary_search(numbers,number_to_find,0,len(numbers)-1)

    if result is True:
        print('El Numero SI Esta En La Lista.')
    else:
        print('El Numero NO Esta En La Lista.')
