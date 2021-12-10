import numpy as np
import matplotlib.pyplot as plt

Cp_data = np.genfromtxt('cp_test.txt', dtype = float)


AoA_lst = Cp_data[1,1:]
loc_lst = Cp_data[2:,0]
cp_array = Cp_data[2:,1:]

def cp_sort (i):
    alpha = AoA_lst[i]
    cplst = cp_array[:,i]
    #cplst= np.flip(cplist)
    return cplst  

cp_aoa_neg2, cp_aoa_neg1, cp_aoa_0, cp_aoa_1, cp_aoa_2 = cp_sort(0), cp_sort(1), cp_sort(2), cp_sort(3), cp_sort(4) 

cp_aoa_3, cp_aoa_3_5, cp_aoa_4, cp_aoa_4_5, cp_aoa_5, cp_aoa_5_5 = cp_sort(5), cp_sort(6), cp_sort(7), cp_sort(8), cp_sort(9), cp_sort(10)

cp_aoa_6, cp_aoa_6_5, cp_aoa_7, cp_aoa_7_5, cp_aoa_8, cp_aoa_8_5 = cp_sort(11), cp_sort(12), cp_sort(13), cp_sort(14), cp_sort(15), cp_sort(16)

cp_aoa_9, cp_aoa_9_5, cp_aoa_10, cp_aoa_10_5, cp_aoa_11 , cp_aoa_11_5 = cp_sort(17), cp_sort(18), cp_sort(19), cp_sort(20), cp_sort(21), cp_sort(22)

cp_aoa_12, cp_aoa_12_5, cp_aoa_13, cp_aoa_13_5, cp_aoa_14, cp_aoa_14_5 = cp_sort(23), cp_sort(24), cp_sort(25), cp_sort(26), cp_sort(27), cp_sort(28)

cp_aoa_15, cp_aoa_15_5, cp_aoa_16, cp_aoa_16_5, cp_aoa_17, cp_aoa_16_5b = cp_sort(29), cp_sort(30), cp_sort(31), cp_sort(32), cp_sort(33), cp_sort(34)

cp_aoa_16b, cp_aoa_15_5b, cp_aoa_15b, cp_aoa_14_5_b, cp_aoa_14b, cp_aoa_13_5b = cp_sort(35), cp_sort(36), cp_sort(37), cp_sort(38), cp_sort(39), cp_sort(40)

cp_aoa_13b = cp_sort(41)







plt.plot(loc_lst, cp_aoa_13b)
plt.gca().invert_yaxis()
plt.show()








