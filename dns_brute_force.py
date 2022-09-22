#!/usr/bin/python

import socket
import colorama 
from colorama import Fore, Back, Style
colorama.init()

text = """\n
#-----------------------------------------------#
#                                               #
#        _____      __       __    _______      #
#      /  __  \    /  \     / /  /   ____/      #
#     /  /  \  |  / /\ \   / /   \  \           #
#    /  /   |  | / /  \ \ / /     \  \          #
#   /  /__ /  / / /    \   /  ____/  /  |brute| #
#  /________/  /_/      \_/ /_______/   |force| #
# ______________________________________________#
#                                               #
#           Version: 1.0 | Hav0ck021            # 
# ______________________________________________#
# ----------------------------------------------#
            """

print(Fore.GREEN + text)

print(Fore.LIGHTRED_EX + "LeTs FiNd OuR DoMaInS :)" + "\n")

dominio = input ("enter the domain (ex.:dominio.com or dominio.com.br): ")

with open("bruteforce.txt") as arquivo:
    nomes = arquivo.readlines()

for nome in nomes:
    DNS = (nome.strip("\n") + "." + dominio)
    try:
        print ("\n" + (DNS) + "." + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass

print("pwn them :)")