# This script serves to purpose of plotting the 3D experimental data

import numpy as np
import matplotlib.pyplot as plt

corr_data = np.genfromtxt('corr_test.txt')  # Generating array
corr_data = corr_data[2:]  # Removing parameters and units

unc_data = np.genfromtxt('unc_test.txt', usecols=np.arange(0,33))
unc_data = unc_data[2:]

# Defining columns
Run_nr, Alpha, Beta, CL, CD, Cyaw, Cm_p_qc, Ct, Cn, Cside, Cm_roll, Cm_pitch, Cm_yaw, V, Re, M = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

# plot lift curve
plt.title('Lift curve')
plt.xlabel('Alpha')
plt.ylabel('CL')
plt.plot(corr_data[:, Alpha], corr_data[:, CL], label='Corrected')
plt.plot(unc_data[:, Alpha], unc_data[:, CL], label='Uncorrected')
plt.legend()
plt.grid()
plt.show()
# plot CD against Alpha
plt.title('Drag coefficient against angle of attack')
plt.xlabel('Alpha')
plt.ylabel('CD')
plt.plot(corr_data[:, Alpha], corr_data[:, CD], label='Corrected')
plt.plot(unc_data[:, Alpha], unc_data[:, CD], label='Uncorrected')
plt.legend()
plt.grid()
plt.show()
# plot drag polar
plt.title('Drag polar')
plt.xlabel('CD')
plt.ylabel('CL')
plt.plot(corr_data[:, CD], corr_data[:, CL], label='Corrected')
plt.plot(unc_data[:, CD], unc_data[:, CL], label='Uncorrected')
plt.legend()
plt.grid()
plt.show()

# Plot moment coefficients
# Roll moment coefficient
plt.title('Roll moment coefficient against angle of attack')
plt.xlabel('Alpha')
plt.ylabel('C_m')
plt.plot(corr_data[:, Alpha], corr_data[:, Cm_roll], label='Corrected')
plt.plot(unc_data[:, Alpha], unc_data[:, Cm_roll], label='Uncorrected')
plt.legend()
plt.grid()
plt.show()

# pitch moment coefficient
plt.title('Pitch moment coefficient against angle of attack')
plt.xlabel('Alpha')
plt.ylabel('C_m')
plt.plot(corr_data[:, Alpha], corr_data[:, Cm_pitch], label='Corrected')
plt.plot(unc_data[:, Alpha], unc_data[:, Cm_pitch], label='Uncorrected')
plt.legend()
plt.grid()
plt.show()
