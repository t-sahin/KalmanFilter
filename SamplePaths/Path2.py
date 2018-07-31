import numpy as np
from .PathCalcs import PathCalcs

#TESTING STRAIGHT LINES
x_4 = np.linspace(0, 10, 101) #0.1 intervals
y_4 = [0] * len(x_4)

x_5 = np.linspace(10, 20, 41) #0.25 intervals
y_5 = [0] * len(x_5)

x_6 = np.linspace(20, 30, 26) #0.40 intervals
y_6 = [0] * len(x_6)

#Vertical Lines (and diagonal):
y_7 = np.linspace(0, 5, 26) #0.20 intervals
x_7 = [30] * len(y_7)

x_8 = np.linspace(30, 35, 26) 
y_8 = np.linspace(5, 0, 26)

y_9 = np.linspace(0, 5, 16) #0.333 intervals
x_9 = [35] * len(y_9)

x_10 = np.linspace(35, 40, 16) 
y_10 = np.linspace(5, 0, 16)

x_path2 = np.append(x_4, np.append(x_5, np.append(x_6, np.append(x_7, np.append(x_8, np.append(x_9, x_10))))))
y_path2 = np.append(y_4, np.append(y_5, np.append(y_6, np.append(y_7, np.append(y_8, np.append(y_9, y_10))))))

x_path2_scaled, y_path2_scaled = PathCalcs.scale_to(x_path2, y_path2, 16, 9, 1)
position_measured_path2 = PathCalcs.measurement_noise(x_path2_scaled, y_path2_scaled, 0.2, 0.2)

np.savetxt('KF_Path2.txt', position_measured_path2)
