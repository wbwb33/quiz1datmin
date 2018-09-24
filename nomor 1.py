import statistics
import numpy as np
from scipy import stats
from scipy.stats import iqr
data1=np.array([10, 3, 7, 5, 4, 9, 10, 1, 2, 7])

#nomor 1a
print("Mean of data-set is : % s " % (statistics.mean(data1))) 
print("Median of data-set is : % s " % (statistics.median(data1))) 
print(stats.mode(data1))

#nomor 1b
print("Variance : % s" % np.var(data1))
print("Standard Deviation : % s" % np.std(data1))
print("Range : % s" % np.ptp(data1,axis=0))
print("IQR : % s" % iqr(data1))

#nomor 1c
from sklearn.preprocessing import MinMaxScaler
data2=data1.reshape(-1,1)
scaler = MinMaxScaler()
scaler.fit(data2)
print("Min-max Normalization")
print(scaler.transform(data2))

print("z normalization")
stats.zscore(data1)
