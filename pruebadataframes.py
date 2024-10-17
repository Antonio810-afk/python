import pandas as pd
#crear un DataFrame
nombre = ['Ana','Luis','Carlos']
edad = [23, 34, 29]
telefono = [374884,3847673,3745766]
data = {'Nombre': ['Ana','Luis', 'Carlos'],'edad':['25','34','29']}
df = pd.DataFrame(data)
print(df)
data2=pd.DataFrame[nombre,edad,telefono]
print(data2)
df.to_CSV("salida.csv", index=False)

