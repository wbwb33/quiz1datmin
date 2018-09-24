from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
y_true = [44, 52, 62, 46, 38]
y_pred = [46, 50, 65, 41, 42]
print("mean absolute error = % s" %mean_absolute_error(y_true, y_pred))
print("mean squared error = % s" %mean_squared_error(y_true, y_pred))
