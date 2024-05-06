# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:38:58 2024

@author: Dell
"""

noticia = open("notcia.txt","rt")
datos_noticia = noticia.read()
print(datos_noticia)

noticia = open("notcia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)
