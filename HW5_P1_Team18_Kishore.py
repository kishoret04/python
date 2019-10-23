# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:44:54 2019

@author: kisho
"""
import numpy as np
import os
import matplotlib.pyplot as plt


#change directory to required drectory
os.chdir(r"F:\Programming\Python") 

#print current directory path
print(os.getcwd())

#read from file 'insurance.txt'

#age	sex	bmi	children	smoker	region	expenses
#19	female	27.9	0	yes	southwest	16884.92
#dtype ={'names': ('gender', 'age', 'weight'), 
#                                  'formats': ('S1', 'i4', 'f4')}
datatype = {'names':('age','sex','bmi','children','smoker','region','expenses'),
         'formats':('i4','S10','f4','i4','S5','S20','f4')}

filename='insurance.txt'

insurance_data = np.loadtxt(filename,datatype,skiprows=1)

#histograms
plt.hist(insurance_data['age'])
plt.hist(insurance_data['bmi'])

#function to calculate mean,sd,median for numpy 1D array
def descriptive_stats(data):
    mean_data = np.mean(data)
    sd_data = np.std(data)
    median_data = np.median(data)
    return np.round(np.array([mean_data,sd_data,median_data]),4)

#function to calculate mode
def calc_mode(data):
    #extract unique values in data    
    unique_set = np.unique(data)
    freq_list = list()
    #calculate frequency of each unique element in the data
    for i in range(len(unique_set)):
        freq_list.append(sum(data == unique_set[i]))
    
    #value with max frequency in the data
    mode = unique_set[freq_list.index(max(freq_list))]
    return mode
      
#Q1 Mean, standard deviation and median of age
dstats_age = descriptive_stats(insurance_data['age'])
#mean_age = round(np.mean(insurance_data['age']),4)
#sd_age = round(np.std(insurance_data['age']),4)
#median_age = round(np.median(insurance_data['age']),4)

#2.	Mean, standard deviation and median of BMI. [5 points]
dstats_bmi = descriptive_stats(insurance_data['bmi'])
#mean_bmi = round(np.mean(insurance_data['bmi']),4)
#sd_bmi = round(np.std(insurance_data['bmi']),4)
#median_bmi = round(np.median(insurance_data['bmi']),4)

#3.	Mean, standard deviation and median of BMI grouped by sex. [5 points]
#descriptive stastistics of males bmi
male_index = insurance_data['sex'] == b'male'
dstats_malebmi = descriptive_stats(insurance_data['bmi'][male_index])
#mean_malebmi = round(np.mean(insurance_data['bmi'][male_index]),4)
#sd_malebmi   = round(np.std(insurance_data['bmi'][male_index]),4)
#median_malebmi=round(np.median(insurance_data['bmi'][male_index]),4)

#descriptive stastistics of females bmi
female_index = insurance_data['sex'] == b'female'
dstats_femalebmi = descriptive_stats(insurance_data['bmi'][female_index])
#mean_femalebmi = round(np.mean(insurance_data['bmi'][female_index]),4)
#sd_femalebmi   = round(np.std(insurance_data['bmi'][female_index]),4)
#median_femalebmi=round(np.median(insurance_data['bmi'][female_index]),4)

#4.	Mean, standard deviation and median of BMI for smokers and non-smokers. [5 points]
#descriptive stastistics of smokers' bmi
smokers_index = insurance_data['smoker'] == b'yes'
dstats_smokerbmi = descriptive_stats(insurance_data['bmi'][smokers_index])
#mean_smokerbmi = round(np.mean(insurance_data['bmi'][smokers_index]),4)
#sd_smokerbmi   = round(np.std(insurance_data['bmi'][smokers_index]),4)
#median_smokerbmi=round(np.median(insurance_data['bmi'][smokers_index]),4)

#descriptive stastistics of nonsmokers' bmi
nonsmokers_index = insurance_data['smoker'] == b'no'
dstats_nonsmokerbmi = descriptive_stats(insurance_data['bmi'][nonsmokers_index])

#mean_nonsmokerbmi = round(np.mean(insurance_data['bmi'][nonsmokers_index]),4)
#sd_nonsmokerbmi   = round(np.std(insurance_data['bmi'][nonsmokers_index]),4)
#median_nonsmokerbmi=round(np.median(insurance_data['bmi'][nonsmokers_index]),4)


#5.	Mean, standard deviation and median of BMI grouped by region. [5 points]
#extracting unique set of region values
region_arr = np.unique(insurance_data['region'])

#creating dictionary with region as index and descriptive stats as values
dstats_region = dict()
for i in range(len(region_arr)):
    region_index = insurance_data['region'] == region_arr[i]
    dstats_region[region_arr[i]] = descriptive_stats(insurance_data['bmi'][region_index])
    

#6.	Mean, standard deviation and median of BMI of those who have more than 2 children. [5 points]
above2child_arr = insurance_data['children'] > 2
dstats_above2child = descriptive_stats(insurance_data['bmi'][above2child_arr])

max2child_arr = insurance_data['children'] <= 2
dstats_max2child = descriptive_stats(insurance_data['bmi'][max2child_arr])



#partC What are the primary reasons for the top 20% of the expenses? 
#In particular, sort the data by expense, and 
#compute the mean, and standard deviation of BMI and the mode of smoker and region.
#How do these values differ from the rest 80% of the population? [10 points]     

#sorting insurance data in descending order of expenses
sortindices_expenses = insurance_data['expenses'].argsort()[::-1]
insurance_data = insurance_data[sortindices_expenses]

#copying top 20% and bottom 80% data into deparate arrays
insurance_top20exp = insurance_data[:int(len(insurance_data)//5)].copy()
insurance_bot80exp = insurance_data[int((len(insurance_data)//5)+1):].copy() 

#calculating descriptive stats of bmi of top 20% insurance data
dstats_top20exp = descriptive_stats(insurance_top20exp['bmi'])

#calculating mode of region and smoker columns of top 20% insurance data
moderegion_top20exp = calc_mode(insurance_top20exp['region'])
modesmoker_top20exp = calc_mode(insurance_top20exp['smoker'])

#calculating descriptive stats of bmi of bottom 80% insurance data
dstats_bot80exp = descriptive_stats(insurance_bot80exp['bmi'])

#calculating mode of region and smoker columns of bottom 80% insurance data
moderegion_bot80exp = calc_mode(insurance_bot80exp['region'])
modesmoker_bot80exp = calc_mode(insurance_bot80exp['smoker'])


        
    

#saving results - INCOMPLETE--------

output_file = 'HW5_output.txt'
np.savetxt(output_file ,np.array2string(dstats_age,separator = '\t'),
           header = 'Mean\tSD\tMedian\n')
dstats_age.tofile(output_file,sep = '\t', format = '%s')


np.array2string(dstats_age,separator = '\t')










