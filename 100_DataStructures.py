# -*- coding: utf-8 -*-
"""
Created on 23-11-2020
Created by Kedar Badrinath Pathade

@author: DELL
"""

print("hello world")
print("hello world")
#Numbers
#a=3 , b=5  #a and b are number objects 

#String
str1 = 'hello javatpoint' #string str1
str1 = 'hello javatpoint'
str2 = ' how are you' #string str2  
str2 = 'how are you'
print (str1)

print (str1[1:5]) #printing first five character using slice operator  
print (str1[4]) #printing 4th character of the string  
print (str1*2,end='kedar') #printing the string twice  
print (str1 + str2) #printing the concatenation of str1 and str2

#Lists
l = ['1','h', "python", '2'] 
l
print(l)
print (l[3:])  
print (l[0:2])
print (l)  
print (l + l);  
print (l * 3);
print(type(l))
#Lets try mutation 
l[1] = "Bye"
print (l)
print(l,'kedar')

#Tuple
t  = ("hi", "python", 2, 4)  
print (t[1:]); 
print(t[1:]) 
print (t[0:2]);  
print(t[0:2])
print (t);  
print(t)
print (t + t)
print(t +t)
print (t * 3)  
print(t*3)
print (type(t))
print(type(t)) 
print("kedar "+t[0])
print('kedar'+t)
p=('k','e','d','a','r')
print(p+t)
print(p)
#Lets try mutation 
t[1] = "Bye"
print (t)

#Dictionary
d = {1:"Jimmy", 2:'Alex', 3:'john', 4:'mike'};
#now we will create a dictionary. the concept of dictionary is like that-
#we have every element and every element has its index
#we denote the lists by [], and we denote tuples by (), and now denote the dictionary with{}
d={1:"Jimmy", 2:"Kedar",3:'pathade'}
print("1st name is "+d[1]); 
print(d)
print("1st name is"+d[1])
print("1st name is "+d[1]) 
print("2nd name is "+ d[4]); 
print("2nd name is "+d[2]) 
print (d); 
print (d.keys());  
print(d.keys())
print(d.values())
print (d.values());

#----ADVANCED----
#list
#ordered collection of items; sequence of items in a list
shoplist =['apple','carrot','mango', 'banana']
shoplist =['apple','ball','carrot','dog']
shoplist
len(shoplist)
len(shoplist)
print(shoplist)
print(shoplist)

#run next 2 lines together
for i in shoplist:
    print(i,end='    ')
    
for i in shoplist:
    print(i,end='    ')

#add item to list
shoplist.append('rice')
shoplist.append("kedar")
shoplist
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist.sort()
shoplist

#index/select
shoplist[0]
shoplist[0:2]
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

#Tuple
#Used to hold multiple object; similar to lists; less functionality than list
#immutable - cannot modify- fast ; ( )
zoo = ('python','lion','elephant','bird')
zoo
len(zoo)
languages = 'c', 'java', 'php'  #better to put (), this also works
languages

#Dictionary - like an addressbook. use of associate keys with values
#key-value pairs { 'key1':value1, 'key2':value2} ; { } bracket, :colon

student = {'A101': ('Abhinav','Kedar'), 'A102': 'Rohit', 'A103':'Rahul', 'A104': 'Karan'}
student
student['A103']
print('Name of rollno A103 is ' +student['A103'])
del student['A104']
student
len(student)

for roll, name in student.items():
    print('name of {} is {} '.format(roll, name) )

#Lets test Mutation: 
#adding a value
student['A104'] = 'Hitesh'
student

#Set
#Sets are unordered collections of objects; ( [ , ])
teamA = set(['india','england','australia','sri lanka','ireland'])
teamA
teamB = set(['pakistan', 'south africa','bangladesh','ireland'])
teamB

#Checking whether a data value exists in a set or not.
'india' in teamA
'india' in teamB

#Adding values in a set
teamA.add('china')
teamA  #puts in order
teamA.add('india')
teamA  #no duplicates
teamA.remove('australia')
teamA

#Create dataframe :
import pandas as pd
 
#Create a DataFrame
d = {'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
            'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                    'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
                    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
                               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
                               'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
 
df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

#View a column of the dataframe in pandas:
df['Name']

#View two columns of the dataframe in pandas:
df[['Name','Score']]

#View first two rows of the dataframe in pandas:
df[:2]
