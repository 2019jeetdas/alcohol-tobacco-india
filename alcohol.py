# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/alcohol.csv",encoding="utf-8")

print("\n----------------------- output data :---------------------\n")
print("Project - 15 : Tobacco Use and Alcohol Consumption in India (using Python ) ");
print("\n------------------------------------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question - C : print available states/UT

df1 = df['India-States-Union Territories']

print('---------------------------------------------')
print('Available data for following State and UT  : ')
print('---------------------------------------------')
print(df1)
print('---------------------------------------------')

# Question - D : Women Use Tobacco

df1 = df['Women who use any kind of Tobacco (%) - NFHS-4 - Total']
df2 = df['Women who use any kind of Tobacco (%) - NFHS-4 - Rural']
df3 = df['Women who use any kind of Tobacco (%) - NFHS-4 - Urban']
df4 = df['Women who use any kind of Tobacco (%) - NFHS-3']

plt.title('Question - D : Women Use Tobacco')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df1,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] Women who use any kind of Tobacco (%) - NFHS-4 - Total")

plt.plot(df2,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] Women who use any kind of Tobacco (%) - NFHS-4 - Rural")

plt.plot(df3,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Women who use any kind of Tobacco (%) - NFHS-4 - Urban")
            
plt.plot(df4,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4] Women who use any kind of Tobacco (%) - NFHS-3")
            
            
plt.legend()
plt.show()


# Question - E : Men use Tobacco

df5 = df['Men who use any kind of Tobacco (%) - NFHS-4 - Total']
df6 = df['Men who use any kind of Tobacco (%) - NFHS-4 - Rural']
df7 = df['Men who use any kind of Tobacco (%) - NFHS-4 - Urban']
df8 = df['Men who use any kind of Tobacco (%) - NFHS-3']

plt.title('Question - E : Men use Tobacco')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df5,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] Men who use any kind of Tobacco (%) - NFHS-4 - Total")

plt.plot(df6,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] Men who use any kind of Tobacco (%) - NFHS-4 - Rural")

plt.plot(df7,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Men who use any kind of Tobacco (%) - NFHS-4 - Urban")
            
plt.plot(df8,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4] Men who use any kind of Tobacco (%) - NFHS-3")
            
            
plt.legend()
plt.show()


# Question - F : Women consume Alcohol

df9 = df['Women who consume Alcohol (%) - NFHS-4 - Total']
df10 = df['Women who consume Alcohol (%) - NFHS-4 - Rural']
df11 = df['Women who consume Alcohol (%) - NFHS-4 - Urban']
df12 = df['Women who consume Alcohol (%) - NFHS-3']

plt.title('Question - F : Women consume Alcohol')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df9,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] Women who consume Alcohol (%) - NFHS-4 - Total")

plt.plot(df10,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] Women who consume Alcohol (%) - NFHS-4 - Rural")

plt.plot(df11,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Women who consume Alcohol (%) - NFHS-4 - Urban")
            
plt.plot(df12,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4] Women who consume Alcohol (%) - NFHS-3")
            
            
plt.legend()
plt.show()

# Question - G : Men consume Alcohol

df13 = df['Men who consume Alcohol (%) - NFHS-4 - Total']
df14 = df['Men who consume Alcohol (%) - NFHS-4 - Rural']
df15 = df['Men who consume Alcohol (%) - NFHS-4 - Urban']
df16 = df['Men who consume Alcohol (%) - NFHS-3']

plt.title('Question - G : Men consume Alcohol')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df13,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] Men who consume Alcohol (%) - NFHS-4 - Total")

plt.plot(df14,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] Men who consume Alcohol (%) - NFHS-4 - Rural")

plt.plot(df15,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Men who consume Alcohol (%) - NFHS-4 - Urban")
            
plt.plot(df16,
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[4] Men who consume Alcohol (%) - NFHS-3")
            
            
plt.legend()
plt.show()

# Question - H : Women tried to stop Tobacco

df17 = df['Women who Tried to Stop Smoking or using Tobacco in any other form during the Past 12 months (%) - Total']
df18 = df['Women who Tried to Stop Smoking or using Tobacco in any other form during the Past 12 months (%) - Rural']
df19 = df['Women who Tried to Stop Smoking or using Tobacco in any other form during the Past 12 months (%) - Urban']

plt.title('Question - H : Women tried to stop Tobacco')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df17,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] Women who Tried to Stop Smoking or using Tobacco in any other form during the Past 12 months (%) - Total")

plt.plot(df18,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] Women who Tried to Stop Smoking or using Tobacco in any other form during the Past 12 months (%) - Rural")

plt.plot(df19,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Women who Tried to Stop Smoking or using Tobacco in any other form during the Past 12 months (%) - Urban")
            
plt.legend()
plt.show()

# Question - I : Men tried to stop Tobacco

df20 = df['Men who Tried to Stop Smoking or using Tobacco in any other form (during the Past 12 months)* % - Total']
df21 = df['Men who Tried to Stop Smoking or using Tobacco in any other form (during the Past 12 months)* % - Rural']
df22 = df['Men who Tried to Stop Smoking or using Tobacco in any other form (during the Past 12 months)* % - Urban']

plt.title('Question - I : Men tried to stop Tobacco')
plt.xlabel("State sl. no. --- >")
plt.ylabel("Numbers --- >")
    
plt.plot(df20,
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[1] Men who Tried to Stop Smoking or using Tobacco in any other form (during the Past 12 months)* % - Total")

plt.plot(df21,
            marker=5,
            markersize=10,
            linestyle='dashed',
            label="[2] Men who Tried to Stop Smoking or using Tobacco in any other form (during the Past 12 months)* % - Rural")

plt.plot(df22,
            marker=6,
            markersize=10,
            linestyle='dashed',
            label="[3] Men who Tried to Stop Smoking or using Tobacco in any other form (during the Past 12 months)* % - Urban")
            
plt.legend()
plt.show()
