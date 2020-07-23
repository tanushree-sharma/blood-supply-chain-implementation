import numpy as np


# prameter generation
# columns - donors, RBC, plasma, platelets
# rows - days of the week starting with sunday
data = [[0 for x in range(4)] for y in range(7)] 

#np.random.lognormal(90.725, 45.635) is giving veryy high values, need to fix
data[0] = [np.random.lognormal(90.725, 45.635),np.random.gamma(3.6582, 19.145),  0.5493 * float(np.random.weibull(1.571)) * 43.243, float(np.random.weibull(2.6342)) * 44.874]
data[1] = [np.random.triangular(0,116,172.01), np.random.triangular(0,132,250.37), 1.0864 * float(np.random.weibull(1.571)) * 43.243, np.random.gamma(4.9766,9.2618)]
data[2] = [np.random.gamma(14.908,7.4096), np.random.gamma(10.466,12.198), 1.0327 * float(np.random.weibull(1.571)) * 43.243, np.random.gamma(6.9138,8.1944)]
data[3] = [np.random.gamma(12.853,9.96), float(np.random.weibull(3.457)) * 132.19, 1.2364 * float(np.random.weibull(1.571)) * 43.243, np.random.gamma(4.7146,9.317)] 
data[4] = [float(np.random.weibull(3.3489)) * 145.3, np.random.gamma(10.277,11.586), 1.1006 * float(np.random.weibull(1.571)) * 43.243, np.random.gamma(5.7338,8.06)]
data[5] = [np.random.gamma(10.47,9.8342), np.random.gamma(13.781,11.601), 1.3835 * float(np.random.weibull(1.571)) * 43.243, np.random.gamma(4.8136,8.7179)]
data[6] = [float(np.random.weibull(1.8248)) * 57.18, np.random.gamma(6.6579,10.279), 0.6111 * float(np.random.weibull(1.571)) * 43.243, float(np.random.beta(1.5186, 1.2625))* 68.669]

# convert number of patients to int, not sure if this needs to be done for other columns
for i in range (0,7):
    data[i][0] = int(data[i][0])

print (data)
