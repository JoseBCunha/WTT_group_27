# Program to graph the XFOIL polars

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# polar data
polar = np.array(pd.read_csv('polar_data.csv', skiprows=1, sep=','))
AoA = polar[:,0]
Cl = polar[:,1]
Cd = polar[:,2]
Cm = polar[:,4]

# Cp data
Cps = np.array(pd.read_csv('CP_data.csv', skiprows=1, sep=','))  # for alpha = -2 0 5 10 15
def index(n):
    if n == 0:
        a = -2
    elif n == 1:
        a = 0
    elif n == 2:
        a = 5
    elif n == 3:
        a = 10
    elif n == 4:
        a= 15
    return a

Cp = []
x = []
for i in range(0, 5):
    Cp.append(Cps[:,3*i +2])
for i in range(0, 5):
    x.append(Cps[:, 3 * i])



def LiftPolar():
    plt.scatter(AoA,Cl, s=10, c="r", label="XFOIL")
    plt.plot(AoA,Cl, color="black", linewidth=1)
    plt.title("Cl - alpha Curve")
    plt.xlabel("Alpha [deg]")
    plt.ylabel("Cl")
    plt.grid()
    plt.legend()
    plt.savefig("Cl_AoA.png", dpi="figure", transparent=True)
    return plt.show()

def MomentPolar():
    plt.scatter(AoA,Cm, s=10, c="r", label="XFOIL")
    plt.plot(AoA,Cm, color="black", linewidth=1)
    plt.title("Cm - alpha Curve")
    plt.xlabel("alpha [deg]")
    plt.ylabel("Cm")
    plt.grid()
    plt.legend()
    plt.savefig("Cm_AoA.png", dpi="figure", transparent=True)
    return plt.show()

def DragPolar():
    plt.scatter(Cd,Cl, s=10, c="r", label="XFOIL")
    plt.plot(Cd,Cl,color="black", linewidth=1)
    plt.title("Cl - Cd Curve")
    plt.xlabel("Cd")
    plt.ylabel("Cl")
    plt.grid()
    plt.legend()
    plt.savefig("Cl_Cd.png", dpi="figure", transparent=True)
    return plt.show()

def CpGraph(n):
    name = index(n)
    file_name = "Cp__a=%sº.png" % name
    label_name = index(n)
    plt.scatter(x[n], Cp[n], s=10, c="r", label=f"XFOIL for alpha = {index(n)}º")
    plt.plot(x[n], Cp[n], color="black", linewidth=1)
    plt.title("Cp Curve")
    plt.xlabel("x / c")
    plt.ylabel("Cp")
    plt.grid()
    plt.legend()
    plt.savefig(file_name, dpi="figure", transparent=True)
    return plt.show()

print(CpGraph(0), CpGraph(1), CpGraph(2), CpGraph(3), CpGraph(4),LiftPolar(),MomentPolar(),DragPolar())

