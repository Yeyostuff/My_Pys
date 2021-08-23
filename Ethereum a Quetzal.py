from time import sleep
from requests_html import HTMLSession
import os

link = ("https://www.google.com/search?q=ethereum+a+quetzal&btnK=Buscar+con+Google&safe=off&source=hp&ei=PSmxYLeVJ-2XwbkPwLeooAo&iflsig=AINFCbYAAAAAYLE3Ta9MQHD8gGy2HbMQko6vWJiP-yNR&oq=AMD+Epyc&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgYIABAWEB46CAgAEBYQChAeULcOWKErYLktaAFwAHgAgAGfA4gBtASSAQcwLjEuNC0xmAEAoAECoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwj3p6Oc9OzwAhXtSzABHcAbCqQQ4dUDCAc&uact=5")

session = HTMLSession()
r = session.get(link)
tiempo = 4
busqueda = ""

#os.system("cls")
eth = float(input("Cuanto ethereum quieres convertir a Quetzales?  "))
busqueda = r.html.find(".b1hJbf") #b1hJbf esta es la clase que contiene el tipo de cambio
print(busqueda)
cambio = float(busqueda[0]._attrs['data-exchange-rate'])
#os.system("cls")

print("          CUANTO VALE MI ETHEREUM HOY:\n")
print(" El tipo de cambio actual es {} QUETZALES por cada Ethereum".format(cambio))



print("\n Tus {} ETH equivalen a: ".format(eth))

sleep(0.3)
print("\n.-.-.-.-.-.-.-.-.-    {} QUETZALES HOY.-.-.-.-.-.-.-.-.-".format(cambio * eth))
