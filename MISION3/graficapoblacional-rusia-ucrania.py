import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("MISION3/poblacion.csv")
x = df["Date"]
y = df["RUS"]
z = df["UKR"]

plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.plot(x, z, color='yellow', linestyle='--', marker='o') 
plt.legend(["Rusia", "Ukrania"], loc="upper left")


plt.xlabel('AÑO')
plt.ylabel('POBLACION')
plt.title('CONFLICTO RUSIA-UCRANIA') 
plt.show() 

