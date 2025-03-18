import csv
import pandas
import matplotlib.pyplot as plt

# with open("diabetes.csv", 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print(line)

data = pandas.read_csv("diabetes.csv").to_numpy()

#data.drop(['SkinThickness', 'Insulin'], axis = 1, inplace = True)

#data.plot(x= 'Insulin', y= 'BMI', kind = "scatter")
#plt.show()




#plt.scatter(matrix1,matrix2)
#plt.show()

#bail = pandas.plotting.scatter_matrix(data, figsize=(9, 9), grid= True)
#plt.show()

# matrix1 = numpy.array(data[:,0])
# matrix2 = numpy.array(data[:,1])
# matrix3 = numpy.array(data[:,2])
# matrix4 = numpy.array(data[:,3])
# matrix5 = numpy.array(data[:,4])
# matrix6 = numpy.array(data[:,5])
# matrix7 = numpy.array(data[:,6])
# matrix8 = numpy.array(data[:,7])

# fig, axs = plt.subplots(2, 2)
# axs[0, 0].scatter(matrix1, matrix2)
# axs[0, 0].set_title('Axis [0, 0]')
# axs[0, 1].scatter(matrix1, matrix3)
# axs[0, 1].set_title('Axis [0, 1]')
# axs[1, 0].scatter(matrix1, matrix4)
# axs[1, 0].set_title('Axis [1, 0]')
# axs[1, 1].scatter(matrix1, matrix5)
# axs[1, 1].set_title('Axis [1, 1]')


data.plot(x= 'Insulin', y= 'BMI', kind = "scatter")
plt.show()