#Renomear todos os arquivos numeral continuos independente da extensão
import os

path = os.chdir("C:\\me")

i = 0
for file in os.listdir(path):

    if (file.endswith('.jpg')):
        new_file_jpg = '{}.jpg'.format(i)
        os.rename(file, new_file_jpg)

        i = i + 1
    elif file.endswith('.jpeg'):
        new_file_jpeg = '{}.jpeg'.format(i)
        os.rename(file, new_file_jpeg)

        i = i + 1
    elif file.endswith('.png'):
        new_file_png = '{}.png'.format(i)
        os.rename(file, new_file_png)

        i = i + 1
		elif file.endswith('.jfif'):
        new_file_jfif = '{}.jfif'.format(i)
        os.rename(file, new_file_jfif)

        i = i + 1

#Renomear todos os arquivos numeral diferenciando por extensão
import os

path = os.chdir("C:\\me")

i = 0
j = 0
k = 0
l = 0

for file in os.listdir(path):
    if file.endswith('.jpg'):
        new_file_jpg = '{}.jpg'.format(i)
        os.rename(file, new_file_jpg)

        i = i + 1
    elif file.endswith('.jpeg'):
        new_file_jpeg = '{}.jpeg'.format(j)
        os.rename(file, new_file_jpeg)

        j = j + 1
    elif file.endswith('.png'):
        new_file_png = '{}.png'.format(k)
        os.rename(file, new_file_png)

        k = k + 1
    elif file.endswith('.jfif'):
        new_file_jfif = '{}.jfif'.format(l)
        os.rename(file, new_file_jfif)

        l = l + 1