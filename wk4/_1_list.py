#Author John Russelle Domingo
from random import randint


first_names = ['John','Krish', 'James', 'Mathew', 'Dong Dong', 'Rich Hard','JoNathan']
second_names = ['Russelle','Marie','Jacob', 'Doe','Kel-vin','Ben','Max', 'Johnson']
last_names = ['Domingo','Sy','Labuntog','Dela Torre','Rimorin', 'Tenison','Eleven','Crawford', 'Joestar']
#print(len(first_names)-1)
#print(randint(0,len(first_names)-1))
def nameGenerator(numberOfNames):
    f_name = (first_names[randint(0,len(first_names)-1)])
    s_name = (second_names[randint(0,len(first_names)-1)])
    l_name = (last_names[randint(0,len(first_names)-1)])
    random_names = [f_name,s_name,l_name]
    if(numberOfNames==1):
        return f"{random_names[randint(0,len(random_names)-1)]}"
    elif(numberOfNames==2):
        return f"{random_names[randint(0,len(random_names)-1)]} {random_names[randint(0,len(random_names)-1)]}"
    else:
        return f"{random_names[randint(0,len(random_names)-1)]} {random_names[randint(0,len(random_names)-1)]} {random_names[randint(0,len(random_names)-1)]}"
    

for i in range(1,randint(1,20)):
    print(f"{i} {nameGenerator(randint(0,3))}")