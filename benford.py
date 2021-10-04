import csv
import numpy as np
import json
import os
import matplotlib.pyplot as plt


file_name = input("Enter csv/json file name: ")

filename, file_extension = os.path.splitext(file_name)

if file_extension == ".csv":
    print("csv not ready yet")
else:
    with open(file_name) as json_file:
        counts = {"0":0, "1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0,"8": 0,"9": 0}
        for line in json_file:
            views = str(json.loads(line)['views'])
            first_number = views[:1]
            counts[first_number] += 1
            # print(first_number+" : "+str(counts[first_number]))

names = list(counts.keys())
values = list(counts.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(counts)),values,tick_label=names)
plt.savefig('bar.png')
plt.show()
