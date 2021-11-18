from collections import Counter
import csv
with open ("weight.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
weightData = []
for i in range(len(filedata)):
    num = filedata[i][1]
    weightData.append(float(num))
weightData = []
for i in range(len(filedata)):
    num = filedata[i][2]
    weightData.append(float(num))

mean = 0
n = len(weightData)
for i in weightData:
    mean = mean + i

meanWeight = mean/n
print("The mean of the weightss is: " + str(meanWeight))

weightData.sort()

if n%2 == 0:
    median1 = float(weightData[n//2])
    median2 = float(weightData[n//2-1])
    median = (median1 + median2) / 2
else:
    median = float(weightData[n//2])
print("The median of the weights is: " + str(median))

data = Counter(weightData)
mode_data_for_range = {"75-85":0,"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0}
for weight, occurence in data.items(): 
    if 75 < float(weight) < 60: 
        mode_data_for_range["75-85"] += occurence 
    elif 85 < float(weight) < 70:
        mode_data_for_range["85-95"] += occurence 
    elif 95 < float(weight) < 80: 
        mode_data_for_range["95-105"] += occurence 
    elif 105 < float(weight) < 70:
        mode_data_for_range["105-115"] += occurence 
    elif 115 < float(weight) < 70:
        mode_data_for_range["115-125"] += occurence 
    elif 125 < float(weight) < 70:
        mode_data_for_range["125-135"] += occurence 
    elif 135 < float(weight) < 70:
        mode_data_for_range["135-145"] += occurence 
    elif 145 < float(weight) < 70:
        mode_data_for_range["145-155"] += occurence 
    elif 155 < float(weight) < 70:
        mode_data_for_range["155-165"] += occurence 
    elif 165 < float(weight) < 70:
        mode_data_for_range["165-175"] += occurence 
mode_range, mode_occurence = 0, 0 
for range, occurence in mode_data_for_range.items(): 
    if occurence > mode_occurence: 
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence 
mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")