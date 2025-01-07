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


