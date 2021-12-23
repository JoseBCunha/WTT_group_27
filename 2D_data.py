import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math 
Cp_data = np.genfromtxt('cp_test.txt', dtype = float)
"""     Fucked up data 
Data = np.genfromtxt("raw_test.txt", dtype=float,
                     encoding=None)
Data = np.delete(Data,0,0)
Data = np.delete(Data,0,0)
press = np.delete(Data, np.s_[0:39], axis = 1)
# sort data 
Pbar_lst = Data[:,5] * 100 
rho_lst = Data[:,16]
V_lst = Data[:,18]
Qwr_lst = Data[:,35]
alpha_lst = Data[:,2] #okay 
p_dyn_arr = press[:,123:192]
q_inf_lst = Data[:,17]
print("sum is:", Pbar_lst + q_inf_lst)
def Cd_calc (n):
    p_dyn1_lst = p_dyn_arr[n,:]
    p_inf = np.full(len(p_dyn_lst),Pbar_lst[n])
    q_inf = q_inf_lst[n]
    p_st1 = p_inf
p_inf = np.full(len(p_tot[2]),Pbar[2], dtype=float)  #ok
term = p_tot[2,:] - 
##term =np.sqrt(((p_tot[13,:]) - p_inf) / q_inf[13] - (( p_tot[13,:] - p_inf )/ q_inf[13]))\
##       * ( 1 - ( ( (p_tot[13,:] + q_wr[13]) - p_inf ) / q_inf[13] ) )
print("p_tot is:", p_tot[13,:])
print("p_inf is:", p_inf)
print("q_inf is:", q_inf[13])

k = 1 / len(term)
ran = np.arange(0,1,k)
Cd = 2 * np.trapz(term,ran)
#return(Cd)
print("number is:",Cd)
##q_inf = ( 1 / 2 ) * rho_lst[2] * V_lst[2] ** 2
##p_tot = press[:,123:192]
##
##p_inf = np.full(len(p_tot),Pbar[2] * 100, dtype=float)
##print(p_inf)
##print(len(p_tot[2,:] - p_inf))
##
### trying to figure out plots
ys = np.arange(len(press[2,:]))
test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
test = np.array(test)
test = test / 25 
plt.plot(ys,press[2,:])
plt.show()
plt.plot(test,press[33,:])
plt.gca().invert_yaxis()
plt.show()
test = list(np.arange(0,24,1))
extra = list(np.arange(23,-1,-1))
for i in range(len(extra)):
    test.append(extra[i])

print(test)
"""
##### total pressures from 125 tem 191
Cp_data = np.genfromtxt('cp_test.txt', dtype = float)
#print(Cp_data)
drag_data = np.genfromtxt('corr_test (3).txt', dtype = float)
Cd_lst = drag_data[2:,2]
Cm_lst = drag_data[2:,4]
#print("moments are:",Cm_lst)
##################################################################################################

AoA_lst = Cp_data[1,1:]
aoas = AoA_lst / 180 * np.pi
loc_lst = Cp_data[2:,0]
loc_lst = loc_lst / 100

cp_array = Cp_data[2:,1:]
##
##plt.plot(loc_lst,press[2,:])
##plt.show()

def cp_sort (i):
    alpha = AoA_lst[i]
    cplst = cp_array[:,i]
    #cplst= np.flip(cplist)
    return cplst  

# seperate for plotting cp distribution 
cp_aoa_neg2, cp_aoa_neg1, cp_aoa_0, cp_aoa_1, cp_aoa_2 = cp_sort(0), cp_sort(1), cp_sort(2), cp_sort(3), cp_sort(4) 

cp_aoa_3, cp_aoa_3_5, cp_aoa_4, cp_aoa_4_5, cp_aoa_5, cp_aoa_5_5 = cp_sort(5), cp_sort(6), cp_sort(7), cp_sort(8), cp_sort(9), cp_sort(10)

cp_aoa_6, cp_aoa_6_5, cp_aoa_7, cp_aoa_7_5, cp_aoa_8, cp_aoa_8_5 = cp_sort(11), cp_sort(12), cp_sort(13), cp_sort(14), cp_sort(15), cp_sort(16)

cp_aoa_9, cp_aoa_9_5, cp_aoa_10, cp_aoa_10_5, cp_aoa_11 , cp_aoa_11_5 = cp_sort(17), cp_sort(18), cp_sort(19), cp_sort(20), cp_sort(21), cp_sort(22)

cp_aoa_12, cp_aoa_12_5, cp_aoa_13, cp_aoa_13_5, cp_aoa_14, cp_aoa_14_5 = cp_sort(23), cp_sort(24), cp_sort(25), cp_sort(26), cp_sort(27), cp_sort(28)

cp_aoa_15, cp_aoa_15_5, cp_aoa_16, cp_aoa_16_5, cp_aoa_17, cp_aoa_16_5b = cp_sort(29), cp_sort(30), cp_sort(31), cp_sort(32), cp_sort(33), cp_sort(34)

cp_aoa_16b, cp_aoa_15_5b, cp_aoa_15b, cp_aoa_14_5_b, cp_aoa_14b, cp_aoa_13_5b = cp_sort(35), cp_sort(36), cp_sort(37), cp_sort(38), cp_sort(39), cp_sort(40)

cp_aoa_13b = cp_sort(41)


# split upper and lower cp

cp_upper = cp_array[:24,:] #ok
points_upper = loc_lst[0:24] #ok


points_lower = loc_lst[24:]
cp_lower = cp_array[24:,:]


##Cna = np.trapz( cp_upper[:,2], points_upper) - np.trapz(cp_lower[:,2], points_lower) ==>> probably wrong method 

Cnb = np.trapz(cp_array[:,2], loc_lst)

Cn_lst = []
Cms = []


for i in range(len(AoA_lst)):
    Cn = np.trapz(cp_array[:,i], loc_lst)
    Cn_lst.append(Cn)


Cl_lst = Cn_lst * ( np.cos(aoas) + ((np.sin(aoas)) ** 2 / np.cos(aoas))) \
         - np.tan(aoas) * Cd_lst


print(Cl_lst[28])

plt.plot(AoA_lst,Cl_lst)
plt.title("Cl-alpha curve")
plt.xlabel("Alpha [degrees]")
plt.ylabel("Cl")
plt.grid()
plt.show()

##plt.plot(AoA_lst, Cd_lst)
##plt.title('Cd-alpha curve')
##plt.xlabel("Alpha [degrees]")
##plt.ylabel("Cd")
##plt.grid()
##plt.show()

##plt.plot(Cd_lst, Cl_lst)
##plt.title('Cl-Cd curve')
##plt.xlabel("Cd")
##plt.ylabel("Cl")
##plt.grid()
##plt.show()

##plt.plot(AoA_lst, Cm_lst)
##plt.title('alpha-cm curve')
##plt.xlabel("alpha [degrees]")
##plt.ylabel("Cm")
##plt.grid()
##plt.show()
    

##print(Cn_lst)
##print()
##print(Cm_lst)
##
##print("Cn together is:", Cnb)

##plt.plot(AoA_lst, Cn_lst)
##plt.title("normal coefficients")
##plt.show()
##plt.plot(AoA_lst, Cm_lst)
##plt.title("moment coefficients")
##plt.show()


plt.plot(loc_lst, cp_aoa_17)
plt.gca().invert_yaxis()
plt.grid()
plt.title("Pressure distribution for 17 degree AoA")
plt.xlabel("Position along chord")
plt.ylabel("Pressure coefficient")
plt.show()
##
##plt.plot(loc_lst, cp_aoa_5)
##plt.gca().invert_yaxis()
##plt.title("Pressure distribution for 5 degree AoA")
##plt.xlabel("Spanwise position")
##plt.ylabel("Pressure coefficient")
##plt.show()
##
##plt.plot(loc_lst, cp_aoa_7)
##plt.gca().invert_yaxis()
##plt.title("Pressure distribution for 7 degree AoA")
##plt.xlabel("Spanwise position")
##plt.ylabel("Pressure coefficient")
##plt.show()
##
##plt.plot(loc_lst, cp_aoa_15)
##plt.gca().invert_yaxis()
##plt.title("Pressure distribution for 15 degree AoA")
##plt.xlabel("Spanwise position")
##plt.ylabel("Pressure coefficient")
##plt.show()
##
##plt.plot(loc_lst, cp_aoa_17)
##plt.gca().invert_yaxis()
##plt.title("Pressure distribution for 17 degree AoA")
##plt.xlabel("Spanwise position")
##plt.ylabel("Pressure coefficient")
##plt.show()









