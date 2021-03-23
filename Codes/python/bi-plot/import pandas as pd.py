import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("EX1ANALISE.xlsx")
print(df)
plt.plot(df["ID"], df["FREQ.RELATIVO"], "bo-")
plt.xlabel('Numero')
plt.ylabel('Frequência relativa do número')
plt.show()