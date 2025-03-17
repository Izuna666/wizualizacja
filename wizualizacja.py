import csv
import pandas
import matplotlib.pyplot as plt

# with open("diabetes.csv", 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

data = pandas.read_csv("diabetes.csv")

data.plot(x= 'Insulin', y= 'BMI', kind = "scatter")
plt.show()