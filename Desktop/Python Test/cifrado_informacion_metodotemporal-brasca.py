"""__author__ = "Ignacio Brasca"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "warkanlock@gmail.com"
__status__ = "In development"

Copyright (C) <year>  <name of author>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import time
import random 
import matplotlib.pyplot as plt
import timeit

start = time.time()

#TESTING SEED
import time
year, month, day, hour, minute, secunde = time.strftime("%Y,%m,%d,%I,%M,%S").split(',')

#GENERAR LA SEED Y LA KEY
#localtime = time.asctime( time.localtime(time.time()) )
#print "seed form: ", localtime
#seed = input("Enter the seed: ")

seed = (int(year)/int(month)) + (int(month) + int(day) + int(hour) + int(minute)) ** int(secunde)
peso = 60 #peso
print "Semilla Generada por tiempo / Seed generate by time: ", seed

#INGRESA EL CODIGO DE ENTRADA
code = input("Ingresar el codigo a cifrar / Input the code to encode: ")

random.seed(seed);

key = random.random() #llave primaria
key_constelacion = ((random.uniform(peso, seed))/(seed/key)) #llave_constelacion

def generate_random_key_list(key, key_constelacion):
	secret_key = []
	for i in range(0,10):
		#data = (i)/(key)*((i-1)**key**time.time()) + peso 
		data = (i)/(key)*((key-1)**key_constelacion**time.time()) + peso 
		if(data>128):
			data = data/4
		secret_key.append(data)
		#secret_key[i-1] = secret_key.append(data)
		#print secret_key[i]
	return secret_key

def generate_word(code):
	word_complete = ""
	for i in range(0,len(code)):
		word_complete = word_complete + (code[i] + '.')
	return word_complete.split('.')

def encode(word, list_keys):
	for i in range(0, len(word)-1):
		word[i] = repr(list_keys[random.randint(0,9)])

	word_encode = word

	return word_encode #es una lista, no un string

def decode(word_encode):
	output_word = []
	for i in range(0, len(word_encode)-1):
		output_word.append(str(unichr(int(float(word_encode[i])))))
		#letra_convertida.append(str(unichr(int(word_encode[i]))))
	return output_word
