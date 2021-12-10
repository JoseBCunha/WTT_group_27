# Program to graph the XFOIL polars

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

polar = np.array(pd.read_csv('polar_data.csv', skiprows=1, sep=','))

AoA = polar[:,0]
Cl = polar[:,1]
Cd = polar[:,2]
Cm = polar[:,4]


plt.scatter(AoA,Cl, s=10, c="r")
plt.plot(AoA,Cl, color="black", linewidth=1)
plt.title("Cl - alpha Curve")
plt.ylabel("Cl")
plt.grid()
plt.savefig("Cl_AoA.png", dpi="figure", transparent=True)

plt.scatter(AoA,Cm, s=10, c="r")
plt.plot(AoA,Cm, color="black", linewidth=1)
plt.title("Cm - alpha Curve")
plt.xlabel("alpha [deg]")
plt.ylabel("Cm")
plt.grid()
plt.savefig("Cm_AoA.png", dpi="figure", transparent=True)

plt.scatter(Cd,Cl, s=10, c="r")
plt.plot(Cd,Cl,color="black", linewidth=1)
plt.title("Cl - Cd Curve")
plt.xlabel("Cd")
plt.ylabel("Cl")
plt.grid()
plt.savefig("Cl_Cd.png", dpi="figure", transparent=True)


# plt.show()


