import numpy as np
from .PathCalcs import PathCalcs

#TESTING MOTION WITH ERRATIC BEHAVIOR:

def func_circle(radius, center, step_num, top_only, bottom_only):
    x_top = np.linspace(-radius+center[0], radius+center[0], step_num)
    x_bottom = np.linspace(radius+center[0], -radius+center[0], step_num)
    
    func_top = np.sqrt(radius**2 - (x_top-center[0])**2) + center[1]
    func_bottom = -1*np.sqrt(radius**2 - (x_bottom-center[0])**2) + center[1]
    
    x_tot = np.append(x_top, x_bottom)
    func_tot = np.append(func_top, func_bottom)
    
    if top_only:
        return (x_top, func_top)
    elif bottom_only:
        return (x_bottom, func_bottom)
    else:
        return (x_tot, func_tot)

x_29 = np.linspace(3,7,41)
y_29 = [10]*41

x_30 = [7]*22
y_30 = [10]*22

x_31 = np.linspace(7,10,31)
y_31 = [10]*31

y_32 = np.linspace(0,3,41)+10 
x_32 = np.exp(y_32-10)+10-1 #function in terms of y

y_33 = np.linspace(3,0,31)+10
x_33 = np.exp(y_33-10)+10-1 #function in terms of y

y_34 = np.linspace(10, 8, 41)
x_34 = 2*y_34 - 10 #function in terms of y

x_35, y_35 = func_circle(1, (6+1,8), 30, False, False)

y_36 = np.linspace(8, 5, 31)
x_36 = 2*y_36 - 10 #function in terms of y

x_37 = np.linspace(0, 20, 30)
y_37 = -1*3*np.sqrt(1 - (x_37-10)**2/10**2) + 5

x_38 = np.linspace(20, 12, 20)
y_38 = (1/5)*x_38 + 2

x_39 = [12]*20
y_39 = [4.4]*20

x_40 = np.linspace(12, 45, 30)
y_40 = -(1/8)*x_40 + 2*2.9

x_41 = np.linspace(45, 35, 10)
y_41 = -(1/8)*x_41 + 2*2.9

x_42 = np.linspace(35, 45, 8)
y_42 = -(1/8)*x_42 + 2*2.9

x_43 = [45]*30
y_43 = np.linspace(0.2, 5, 30)

y_44 = np.linspace(5, 5.8, 20)
x_44 = 5*np.sin(5*y_44-3) + 45 #function in terms of y

y_45 = np.linspace(5.8, 7.5, 20)
x_45 = 9*np.sin(2*y_45+1) + 49.5 #function in terms of y

x_46 = [46]*30
y_46 = [7.55]*30

y_47 = np.linspace(7.6, 11.6, 30)
x_47 = 15*np.sin(1.1*y_47+0.5) + 37 #function in terms of y

x_48 = [48, 48.8, 49.5, 49.8, 49.9, 49.4, 48.5, 47.3, 46.2, 45.2, 44.8, 44.6, 44.7, 44.85, 45.4, 45.8, 46.4, 47.2, 47.9]
y_48 = [11.7, 11.8, 11.95, 12.15, 12.4, 12.6, 12.75, 12.78, 12.7, 12.5, 12.3, 12.1, 11.9, 11.7, 11.5, 11.3, 11.2, 11.1, 11.05]

x_49 = [48.8]*10
y_49 = [11.0]*10

x_path5 = np.append(x_29, np.append(x_30, np.append(x_31, np.append(x_32, np.append(x_33, np.append(x_34, np.append(x_35, np.append(x_36, np.append(x_37, np.append(x_38, np.append(x_39, np.append(x_40, np.append(x_41, np.append(x_42, np.append(x_43, np.append(x_44, np.append(x_45, np.append(x_46, np.append(x_47, np.append(x_48, x_49))))))))))))))))))))
y_path5 = np.append(y_29, np.append(y_30, np.append(y_31, np.append(y_32, np.append(y_33, np.append(y_34, np.append(y_35, np.append(y_36, np.append(y_37, np.append(y_38, np.append(y_39, np.append(y_40, np.append(y_41, np.append(y_42, np.append(y_43, np.append(y_44, np.append(y_45, np.append(y_46, np.append(y_47, np.append(y_48, y_49))))))))))))))))))))

x_path5_scaled, y_path5_scaled = PathCalcs.scale_to(x_path5, y_path5, 16, 9, 1)
position_measured_path5 = PathCalcs.measurement_noise(x_path5_scaled, y_path5_scaled, 0.2, 0.2)

np.savetxt('KF_Path5.txt', position_measured_path5)
