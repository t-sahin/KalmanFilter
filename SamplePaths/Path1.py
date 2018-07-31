import numpy as np
import matplotlib.pyplot as plt
from .PathCalcs import PathCalcs

#TESTING DIFFERENT CONSTANT VELOCITIES WITH SAME FUNCTION:
def func_sin(x):
    return 20*np.sin(x)

x_1 = np.linspace(0, 20, 201) 
y_1 = func_sin(x_1)

x_2 = np.linspace(20, 40, 81) 
y_2 = func_sin(x_2)

x_3 = np.linspace(40, 60, 51) 
y_3 = func_sin(x_3)

x_path1 = np.append(x_1, np.append(x_2, x_3)) 
y_path1 = np.append(y_1, np.append(y_2, y_3))

x_path1_scaled, y_path2_scaled = PathCalcs.scale_to(x_path1, y_path1, 16, 9, 1)
position_measured_path1 = PathCalcs.measurement_noise(x_path1_scaled, y_path1_scaled, 0.2, 0.2)

np.savetxt('KF_Path1.txt', position_measured_path1)
