import pandas
import numpy
import matplotlib.pyplot as plt

#this was done once for dataset manipulation to achive redable data

#Data = pandas.read_csv("Iraq_dataset.csv")
#Data['Gender'] = Data['Gender'].replace({'F': 0, 'M': 1})
#Data['CLASS'] = Data['CLASS'].replace({'N': 0, 'P': 1, 'Y': 2})
#print(Data['CLASS'])
#Data.to_csv('Modified_Iraq_dataset.csv',index = False)

#all data types are alright, this dataset is fine:

Data = pandas.read_csv("Modified_Iraq_dataset.csv")
Data.drop(['ID','No_Pation'], axis = 1, inplace = True)

#since 1 is the smallest group now we randomly choose 52 samples from 'CLASS' groups 0, ,2 so we have equal samples for all states:

Data_0 = Data[Data['CLASS'] == 0].sample(n=53, ignore_index= False)
#Data_0.info()
#print(Data_0)
Data_1 = Data[Data['CLASS'] == 1]
#print(Data_1)
Data_2 = Data[Data['CLASS'] == 2].sample(n=53, ignore_index= False)
#print(Data_2)
#print(Data_0.size,Data_1.size,Data_2.size)
#print(Data_0,Data_1,Data_2)

# now we plot histograms for chosen data groups to see corelations and so on

# plt.hist(Data_0['BMI'], label= 'Healthy', bins= 12, alpha= 0.7)
# plt.hist(Data_1['BMI'], label= 'Maybe', bins= 12, alpha= 0.7)
# plt.hist(Data_2['BMI'], label= 'Diabetes', bins= 12, alpha= 0.7)

# plt.xlabel("BMI")
# plt.ylabel("Patient")

# plt.legend()
# plt.show()

# Create a figure and axes
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot histograms
axes[0, 0].hist(Data_0['BMI'], label= 'Healthy', bins= 12, alpha= 0.7)
axes[0, 0].hist(Data_1['BMI'], label= 'Maybe', bins= 12, alpha= 0.7)
axes[0, 0].hist(Data_2['BMI'], label= 'Diabetes', bins= 12, alpha= 0.7)
axes[0, 0].legend()
axes[0, 0].set_xlabel("BMI")
axes[0, 0].set_ylabel("Patient")
axes[0, 0].set_title("BMI Histogram")

axes[0, 1].hist(Data_0['AGE'], label= 'Healthy', bins= 12, alpha= 0.7)
axes[0, 1].hist(Data_1['AGE'], label= 'Maybe', bins= 12, alpha= 0.7)
axes[0, 1].hist(Data_2['AGE'], label= 'Diabetes', bins= 12, alpha= 0.7)
axes[0, 1].legend()
axes[0, 1].set_xlabel("AGE")
axes[0, 1].set_ylabel("Patient")
axes[0, 1].set_title("AGE Histogram")

axes[1, 0].hist(Data_0['Chol'], label= 'Healthy', bins= 12, alpha= 0.7)
axes[1, 0].hist(Data_1['Chol'], label= 'Maybe', bins= 12, alpha= 0.7)
axes[1, 0].hist(Data_2['Chol'], label= 'Diabetes', bins= 12, alpha= 0.7)
axes[1, 0].legend()
axes[1, 0].set_xlabel("Chol")
axes[1, 0].set_ylabel("Patient")
axes[1, 0].set_title("Chol Histogram")

axes[1, 1].hist(Data_0['HDL'], label= 'Healthy', bins= 12, alpha= 0.7)
axes[1, 1].hist(Data_1['HDL'], label= 'Maybe', bins= 12, alpha= 0.7)
axes[1, 1].hist(Data_2['HDL'], label= 'Diabetes', bins= 12, alpha= 0.7)
axes[1, 1].legend()
axes[1, 1].set_xlabel("HDL")
axes[1, 1].set_ylabel("Patient")
axes[1, 1].set_title("HDL Histogram")

# Adjust layout for better appearance
plt.tight_layout()
plt.show()
