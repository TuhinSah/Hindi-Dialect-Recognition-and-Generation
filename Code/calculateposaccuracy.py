import sys

predictions = []
answers = []

total_words = 0
correct_words = 0

with open(sys.argv[1], "r") as prediction_file:
    for line in prediction_file:
    	predictions.extend(line.strip().split(" "))

with open(sys.argv[2], "r") as answer_file:
    for line in answer_file:
    	answers.extend(line.strip().split(" "))

for prediction in predictions:
	total_words += (len(prediction))

print len(predictions)
print len(answers)

for i in xrange(len(predictions)):
	print i, predictions[i], answers[i]
	if predictions[i].split("/")[1] == answers[i].split("/")[1]:
		correct_words += 1

accuracy = float(correct_words) / float(total_words) * 100.0
print "Accuracy = " + str(accuracy)
