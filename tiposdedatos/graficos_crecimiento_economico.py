import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("crecimiento_economico.csv")
x = df["Año"]
y = df["Argentina"]
z = df["Brasil"]
t = df["Chile"]
a = df["Colombia"]
b = df["México"]
c = df["Perú"]

plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.plot(x, z, color='yellow', linestyle='--', marker='o') 
plt.plot(x, t, color='black', linestyle='--', marker='o') 
plt.plot(x, a, color='red', linestyle='--', marker='o') 
plt.plot(x, b, color='blue', linestyle='--', marker='o') 
plt.plot(x, c, color='violet', linestyle='--', marker='o') 
plt.legend(["Argentina", "Brasil", "Chile", "Colombia", "México", "Perú"], loc="lower center")

plt.xlabel('año')
plt.ylabel('PIB')
plt.title('Grafico sobre el crecimiento economico en america latina') 
plt.show() 

