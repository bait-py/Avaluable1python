#REQUISITOS
# input()
# print()
# a = 1
# 1+1
# "Hola" + "el nil te un 6"
# b = int(12)
# c = float(b)

# -PLANTEJAMENT EXERCICI-
#Quants cops han posat la sesion de quevedo depenent de la hora.
#Com bé sabem la sessió de Quevedo es un absolut banger, aixo vol dir que quanta mes estona passi de la nit més vegades sonara aquesta cançó.
#Podem intentar deduir que la cancó sonara un cop cada dues hores es a dir si passen 4 hores, sonara 2 cops, si passen 6 hores sonarà 3 cops, etc.
#Cal recalcar que el DJ es una mica tiquismiquis i només li agrada posar la cançó en hores parelles.

#ENTRADA
#Demana una entrada que ens digui les hores que han passat de festa.
#Després calcula la quantitat de vegades que sonara la canó depenent de les hores que hagin passat.
#Recorda que si el numero és imparell haurem d'arrodonir el numero a la baixa ja que la canço no pot sonar a la meitat, la gent no pot permetres aguantar aquesta tortura a mitjes. 
#Pista: Llibreria math.

#SORTIDA
#Un cop calculem les vegades que ha sonat la canço farem que surti per pantalla el missatge "LA SESSIO DE QUEVEDO HA SONAT X COPS", X significant el numero de cops que ha sonat.

#RESOLUCIÓ
import math
HoresFesta = int(input("Quantes hores han passat de festa? "))
NumVegades = math.floor(HoresFesta/2) #També podem utilitzar // (Divisió entera)
print(f"la sessió de quevedo ha sonat {NumVegades} cops".upper)


#ENTRADES
input()

#SORTIDES
print("Hello World")

#CÀLCULS NUMÈRICS
a = 1+1

#CÀLCULS DE STRINGS
string1 = "Hola"
string2 = "Mon"
resultat = string1 + string2

#TRANSFORMACIONS
int()
float()
str()
bool()