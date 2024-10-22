import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("MISION3/poblacion.csv")
x = df["Date"]
y = df["CHN"]
z = df["IND"]
t = df["USA"]
a = df["IDN"]
b = df["PAK"]
c = df["BRA"]
d = df["NGA"]
e = df["BGD"]
f = df["RUS"]
g = df["MEX"]


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




plt.legend(["China", "India", "Estados Unidos", "Indonesia", "Pakistán", "Brasil", "Nigeria", "Bangladés", "Rusia", "México"], loc="upper left")


plt.xlabel('AÑO')
plt.ylabel('POBLACION')
plt.title('PAISES CON MAYOR POBLACION') 
plt.show() 

