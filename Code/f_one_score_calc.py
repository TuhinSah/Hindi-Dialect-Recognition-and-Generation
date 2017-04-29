import sys

predictions = []
answers = []

with open(sys.argv[1], "r") as prediction_file:
    for line in prediction_file:
        (_, dialect) = line.strip().split(" | ")
        predictions.append(dialect)

with open(sys.argv[2], "r") as answer_file:
    for line in answer_file:
        (_, dialect) = line.strip().split(" | ")
        answers.append(dialect)

total_lines = len(predictions)

std_true_positive = 0
std_false_positive = 0
std_false_negative = 0

hum_true_positive = 0
hum_false_positive = 0
hum_false_negative = 0

bom_true_positive = 0
bom_false_positive = 0
bom_false_negative = 0

wup_true_positive = 0
wup_false_positive = 0
wup_false_negative = 0

eup_true_positive = 0
eup_false_positive = 0
eup_false_negative = 0

del_true_positive = 0
del_false_positive = 0
del_false_negative = 0

for i in range(total_lines):
    if(predictions[i] == "STD" and answers[i] == "STD"):
        std_true_positive += 1
    elif(predictions[i] == "STD" and answers[i] != "STD"):
        std_false_positive += 1
    elif(predictions[i] != "STD" and answers[i] == "STD"):
        std_false_negative += 1
    elif(predictions[i] == "HUM" and answers[i] == "HUM"):
        hum_true_positive += 1
    elif(predictions[i] == "HUM" and answers[i] != "HUM"):
        hum_false_positive += 1
    elif(predictions[i] != "HUM" and answers[i] == "HUM"):
        hum_false_negative += 1
    elif(predictions[i] == "BOM" and answers[i] == "BOM"):
        bom_true_positive += 1
    elif(predictions[i] == "BOM" and answers[i] != "BOM"):
        bom_false_positive += 1
    elif(predictions[i] != "BOM" and answers[i] == "BOM"):
        bom_false_negative += 1
    elif(predictions[i] == "WUP" and answers[i] == "WUP"):
        wup_true_positive +=1
    elif(predictions[i] == "WUP" and answers[i] != "WUP"):
        wup_false_positive += 1
    elif(predictions[i] != "WUP" and answers[i] == "WUP"):
        wup_false_negative += 1
    elif(predictions[i] == "EUP" and answers[i] == "EUP"):
        eup_true_positive += 1
    elif(predictions[i] == "EUP" and answers[i] != "EUP"):
        eup_false_positive += 1
    elif(predictions[i] != "EUP" and answers[i] == "EUP"):
        eup_false_negative += 1
    elif(predictions[i] == "DEL" and answers[i] == "DEL"):
        del_true_positive +=1
    elif(predictions[i] == "DEL" and answers[i] != "DEL"):
        del_false_positive +=1
    elif(predictions[i] != "DEL" and answers[i] == "DEL"):
        del_false_negative += 1

print "STD True Positive: " + str(std_true_positive)
print "STD False Positive: " + str(std_false_positive)
print "STD False Negative: " + str(std_false_negative)

std_precision = std_true_positive / float(std_true_positive + std_false_positive)
std_recall = std_true_positive / float(std_true_positive + std_false_negative)
std_f1 = 2 * std_precision * std_recall / (std_precision + std_recall)

print "STD Precision: " + str(std_precision)
print "STD Precision: " + str(std_recall)
print "STD F1: " + str(std_f1)

print "HUM True Positive: " + str(hum_true_positive)
print "HUM False Positive: " + str(hum_false_positive)
print "HUM False Negative: " + str(hum_false_negative)

hum_precision = hum_true_positive / float(hum_true_positive + hum_false_positive)
hum_recall = hum_true_positive / float(hum_true_positive + hum_false_negative)
hum_f1 = 2 * hum_precision * hum_recall / (hum_precision + hum_recall)

print "HUM Precision: " + str(hum_precision)
print "HUM Precision: " + str(hum_recall)
print "HUM F1: " + str(hum_f1)

print "BOM True Positive: " + str(bom_true_positive)
print "BOM False Positive: " + str(bom_false_positive)
print "BOM False Negative: " + str(bom_false_negative)

bom_precision = bom_true_positive / float(bom_true_positive + bom_false_positive)
bom_recall = bom_true_positive / float(bom_true_positive + bom_false_negative)
bom_f1 = 2 * bom_precision * bom_recall / (bom_precision + bom_recall)

print "BOM Precision: " + str(bom_precision)
print "BOM Precision: " + str(bom_recall)
print "BOM F1: " + str(bom_f1)

print "WUP True Positive: " + str(wup_true_positive)
print "WUP False Positive: " + str(wup_false_positive)
print "WUP False Negative: " + str(wup_false_negative)

wup_precision = wup_true_positive / float(wup_true_positive + wup_false_positive)
wup_recall = wup_true_positive / float(wup_true_positive + wup_false_negative)
wup_f1 = 2 * wup_precision * wup_recall / (wup_precision + wup_recall)

print "WUP Precision: " + str(wup_precision)
print "WUP Precision: " + str(wup_recall)
print "WUP F1: " + str(wup_f1)

print "EUP True Positive: " + str(eup_true_positive)
print "EUP False Positive: " + str(eup_false_positive)
print "EUP False Negative: " + str(eup_false_negative)

eup_precision = eup_true_positive / float(eup_true_positive + eup_false_positive)
eup_recall = eup_true_positive / float(eup_true_positive + eup_false_negative)
eup_f1 = 2 * eup_precision * eup_recall / (eup_precision + eup_recall)

print "EUP Precision: " + str(eup_precision)
print "EUP Precision: " + str(eup_recall)
print "EUP F1: " + str(eup_f1)

print "DEL True Positive: " + str(del_true_positive)
print "DEL False Positive: " + str(del_false_positive)
print "DEL False Negative: " + str(del_false_negative)

del_precision = del_true_positive / float(del_false_positive + del_true_positive)
del_recall = del_true_positive / float(del_true_positive + del_false_negative)
del_f1 = 2 * del_precision * del_recall / (del_precision + del_recall)

print "DEL Precision: " + str(del_precision)
print "DEL Precision: " + str(del_recall)
print "DEL F1: " + str(del_f1)
