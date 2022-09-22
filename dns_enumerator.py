#!/usr/bin/python

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
#   /  /__ /  / / /    \   /  ____/  /          #
#  /________/  /_/      \_/ /_______/    |enum| #
# ______________________________________________#
#                                               #
#           Version: 1.0 | Hav0ck021            # 
# ______________________________________________#
# ----------------------------------------------#
            """

print(Fore.GREEN + text)

print(Fore.LIGHTRED_EX + "LeTs FiNd OuR Ip :)" + "\n")

import socket

dominio = input("enter the domain (ex.:dominio.com or dominio.com.br): ")
nomes = ["ns1", "ns2", "www", "ftp", "intranet"]

for nome in nomes:
    DNS = nome + "." + dominio 
    try:
        print("\n" + "your domain and your Ip is: " + Fore.LIGHTRED_EX + (DNS) + (":") + socket.gethostbyname(DNS) + "\n")
    except socket.gaierror:
        pass

print("pwn them :)")