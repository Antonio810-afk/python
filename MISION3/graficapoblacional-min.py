import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("MISION3/poblacion.csv")
x = df["Date"]
y = df["NRU"]
z = df["TUV"]
t = df["PLW"]
a = df["KNA"]
b = df["MCO"]
c = df["LIE"]
d = df["MDV"]
e = df["WSM"]
f = df["DMA"]
g = df["BRB"]


plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.plot(x, z, color='yellow', linestyle='--', marker='o') 
plt.plot(x, t, color='black', linestyle='--', marker='o') 
plt.plot(x, a, color='red', linestyle='--', marker='o') 
plt.plot(x, b, color='blue', linestyle='--', marker='o') 
plt.plot(x, c, color='violet', linestyle='--', marker='o') 
plt.plot(x, d, color='Orange', linestyle='--', marker='o') 
plt.plot(x, e, color='Purple', linestyle='--', marker='o') 
plt.plot(x, f, color='Brown', linestyle='--', marker='o') 
plt.plot(x, g, color='Pink', linestyle='--', marker='o') 




plt.legend(["Nauru", "Tuvalu", "Palaos", "San Cristóbal y Nieves", "Mónaco", "Liechtenstein", "Maldivas", "Samoa", "Dominica", "Barbados"], loc="upper left")


plt.xlabel('AÑO')
plt.ylabel('POBLACION')
plt.title('PAISES CON MENOR POBLACION') 
plt.show() 

