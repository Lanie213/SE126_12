#Jelania Hassell
#Lab4 Demo (List) 

#A list is data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list. 

#Week 4: Introduction to Lists 

#Lists can hold mutiple points of data and store them to "memory" to be used later on in our program

#below is a hand-populated list (not from file) 
#list1 holds a series of names

list1 = ["Sam", "Mary", "Bill", "Adam", "Betty"]

#print full list - looks like print(rec) in data import demo 

print(list1) 

#List: Store multiple data values of the same type!) to RAM (memory) ie our program can remember a group of values, as long as they have a position (index) in the list 
print() #for spacing in console

#print the list each data point at a time 
#) ---> FIRST INDEX!
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

num_records =len(list1) #len() is a length funtion 
#len() returns tthe length of the list/item you pass it
print("\nNUM RECORDS in LIST1: ", num_records)
#the length of a list is always +1 more than the hightest index 
#(position in the list! starts at 0) 

print() #for console sapce 
print() 

#a better way to print (and PROCESS) a full list with contents is using the ...... F O R L O O P!
#For loops were made for lists :]

print("Printing from a FOR LOOP!\n")

for index in range(0, num_records): 
    #the loop starts at index 0 ([0]) and it will run for num-records  # of times (includes 0)
    #IE the loop will run num_records number of times, or for each position help by a list item 

    print("INDEX#" , index, "\t" , list1[index])
    #index MUST be used in combo with list1 (or other list names) in order to find specific value in list at that position 
    #index is the position of the stored values 
    #each index reps a different value position in the list

#-----------------------------------------------------------------------------------------------------------------------------------

#three new list, now with DIFFERENT types of data...
list2 = ["Sam", "18", "32000"]
list3 = ["Mary", "21", "34000"]
list4 = ["Tom", "24", "38000"]
#list above look like a RECORD as opposed to a FIELD when considering a text file

#RECORD --> multiple data values, all different kinds 
#FILED --> multiple data values, all the same kind

#to store a data file's records (which are read as lists) into actual lists (values stored to RAM):

#StEP 1: CREATE EMPTY LISTS
#each FIELD should have its own list 
name = [] #empty list called 'name'
age = [] #empty list called 'age' 
salary = [] #empty list called 'salary' 
#the above liste are EMPTY -- they have no values stored in them 

#STEP 2: ADD ELEMENTS TO THE LIST (POPULATING THE LISTS)
name.append(list2[0]) #adds index0 of list2 to 'name'
name.append(list3[0])
name.append(list4[0])

print()
print("List 'name' contents: " , name) 
print("name[1]: " , name[1]) 

#REMEMBER: it's easier/more efficient to do this in a FOR LOOP 
for index in range(0,3): 
    print("INDEX: " , index, "\t", name[index])

print("Part 1 of demo complete .... \n\n")

#PART 2 -------------FILE IMPORT REVIEW / APPENDING DATA FROM FILES TO LISTS!--------------------------------------
print("-------------------------------------------------------------------------------------------------") 
print("\n\n") 

#BEFORE STARTING: CHECK THE TEXT/CSV FILE!

#STEP 1: imnport csv library
import csv 

#STEP 2: Initialize num_records so it can count the records 
num_records = 0 

#STEP 3: Create empty lists to poplulate with text file data
#MAKE SURE THIS HAPPENS *BEFORE* YOU CONNECT TO THE FILE!
name = []
age = []
salary = [] 
#NOTE: There is one list for each field in the file

#STEP 4: Connect to data file
with open("C:/Users/001283698/Desktop/example.csv") as csvfile:
    

     #STEP 5: allow data to be "read"
     file = csv.reader(csvfile)

    #STEP 6: process data in a for loop
     for rec in file: 
        
    #STEP 7: In
        num_records += 1

    #STEP 8: append (add) values frrom each field of the record to thier corresponding lists

        name.append(rec[0]) #name is hels the 1st field 
        age.append(int(rec[1])) #age is held in the second feild 
        salary.append(float(rec[2])) #salary is held in third field


#process the list to print:
for index in range(0, num_records): 

    print("INDEX: ", index, "\t" , name[index], "\t" , name[index], "\t $" , salary[index]) 

print("Finished processing list for: printing. \n\n") 

#process the lists to find avarage salary
sal_total = 0 
for index in range(0, num_records): 
    sal_total += salary[index] #adds each value of the list to 

avg_sal = sal_total / num_records
print("AVG SALARY IN LIST: ${:.2f}".format(avg_sal))  