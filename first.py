from traceback import print_tb

print("welcome to my first python program")
a=10
print(type(a))
str='shraddha'
#finding length of string
print('length of string is: ',len(str))
#print the element at specific index from string
print(str[2])
#concatenate two strings
print(str+' sadavarte')
#some string methods
print(str.upper())
print(str.lower())
print(str.isalpha())
print(str.startswith('sadavarte'))
print(str.endswith('a'))
print(str.find('a')) #returns the index of first occurence of 'a'
s='good morning'
print(s.replace('morning','night'))
print(s.split())

#string slicing
str1='hello'
print(str1[1:4])
print(str1[:3])
print(str1[2:])
print(str1[-1]) #last character of string
print(str1[:-3])
print(str1[-2:-4])
 #list in python
list1=[1,"hi",1.2,[2,4,6]]
print(type(list1))
print(list1)
#list slicing
print(list1[1:3])
print(list1[:2])
#list concatenation
print(list1+list1)
#list repetition using * operator
print(list1*3)

#tuples in python
tup=(2,1,4,3) #tuple can also allow heterogeneous elements
print(type(tup)) #print type of tuple
print(tup) #print the tuple values
#tuple slicing
print(tup[1:2])
print(tup[2:])
#tuple concatenation
print(tup+tup)
#tuple repetition using + operator
print(tup*3)

#dictionary in python
d={1:'Jimmy',2:'Alex',3:'John',4:'Mike'}
#printing dictionary
print(d)
#accessing values using keys
print("1st name is: ",d[1])
print("2nd name is: ",d[4])

print(d.keys())
print(d.values())
#The data type's unordered collection is Python Set. It is iterable, mutable(can change after creation), and has remarkable components. The elements of a set have no set order; It might return the element's altered sequence. Either a sequence of elements is passed through the curly braces and separated by a comma to create the set or the built-in function set() is used to create the set.
# It can contain different kinds of values.
set1=set() #empty set
set2={'james',2,'python',3,2,4} #set does not allow duplicate values
print(set2)
#adding element to the set
set2.add('shraddha')
print(set2)
#removing element from set
set2.remove(2)
print(set2)

