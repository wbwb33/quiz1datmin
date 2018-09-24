a = [[70, 20],[30, 80]]

TP = a[0][0]
FN = a[0][1]
FP = a[1][0]
TN = a[1][1]

sensitivity=TP/(TP+FN)
print("Sensitivity (Recall) = % s" % (sensitivity))

specificity=TN/(TN+FP)
print("Specificity = % s" % (specificity))

pred_pos=TP/(TP+FP)
print("Positive predictate value (Precision) = % s" % (pred_pos))

pred_neg=TN/(TN+FN)
print("Negative predictate value = % s" % (pred_neg))

f_score = 2 * pred_pos * sensitivity / (pred_pos + sensitivity)
print("f-score = % s" % (f_score))
