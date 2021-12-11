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

# airfoil data
airfoil = np.array(pd.read_csv("Airfoil.csv", skiprows=0, sep=","))
x_c = airfoil[:,0]
y_c = airfoil[:,1]

def LiftPolar():
    plt.scatter(AoA,Cl, s=10, c="r", label="XFOIL")
    plt.plot(AoA,Cl, color="black", linewidth=1)
    plt.xlabel("\u03B1 [deg]")
    plt.ylabel(r"$C_{l}$")
    plt.grid()
    plt.legend()
    plt.savefig("Cl_AoA.png", dpi="figure", transparent=True)
    return plt.show()

def MomentPolar():
    plt.scatter(AoA,Cm, s=10, c="r", label="XFOIL")
    plt.plot(AoA,Cm, color="black", linewidth=1)
    plt.xlabel("\u03B1 [deg]")
    plt.ylabel(r"$C_{m}$")
    plt.grid()
    plt.legend()
    plt.savefig("Cm_AoA.png", dpi="figure", transparent=True)
    return plt.show()

def DragPolar1():
    plt.scatter(Cd,Cl, s=10, c="r", label="XFOIL")
    plt.plot(Cd,Cl,color="black", linewidth=1)
    plt.xlabel(r"$C_{d}$")
    plt.ylabel(r"$C_{l}$")
    plt.grid()
    plt.legend()
    plt.savefig("Cl_Cd.png", dpi="figure", transparent=True)
    return plt.show()

def DragPolar2():
    plt.scatter(AoA,Cd, s=10, c="r", label="XFOIL")
    plt.plot(AoA,Cd,color="black", linewidth=1)
    plt.xlabel("\u03B1 [deg]")
    plt.ylabel(r"$C_{d}$")
    plt.grid()
    plt.legend()
    plt.savefig("Cl_Cd.png", dpi="figure", transparent=True)
    return plt.show()

def CpGraph(n):
    name = index(n)
    file_name = "Cp__a=%sº.png" % name
    plt.scatter(x[n], Cp[n], s=10, c="r", label=f"XFOIL for alpha = {index(n)}º")
    plt.plot(x[n], Cp[n], color="black", linewidth=1)
    plt.xlabel("x/c")
    plt.ylabel(r"$C_{p}$")
    plt.grid()
    plt.legend()
    plt.savefig(file_name, dpi="figure", transparent=True)
    return plt.show()

def Airfoil():
    plt.figure(figsize=(16, 3))
    plt.scatter(x_c,y_c, s=10, c="r")
    plt.plot(x_c,y_c, color="black", linewidth=1)
    plt.xlabel("x/c")
    plt.ylabel("y/c")
    plt.savefig("airfoil_plot.png", dpi="figure", transparent=True)
    return plt.show()

# print(CpGraph(0), CpGraph(1), CpGraph(2), CpGraph(3), CpGraph(4),LiftPolar(),MomentPolar(),DragPolar(),DragPolar2(),Airfoil())

