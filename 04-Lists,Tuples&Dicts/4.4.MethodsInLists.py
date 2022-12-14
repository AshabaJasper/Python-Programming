#Firstly understand Augmented Assignment Operators
#+=, -=, /=, *=

word="hello"
word+=" world"
word+=" the next is now"

print(word)

#finding a value with the index() method

list=[21,23,34,56,78,98]
print(list.index(34))

list1=['james','peter','jane']
print(list1.index("james"))

#adding values to lists is called appending or inserting
#how append works:
list2=['cats','dogs','mice']
list2.append('birds')
print(list2)
#will add birds to the list

#how insert works
list2.insert(2,'birds')
print(list2)

#removing values to lists is called remove()
list2.remove('birds')
print(list2)
#will remove the first instance of birds
list2.remove('birds')
print(list2)
#remove the second instance
#can also use the del function

#removes the item at the first index
del list2[1]
print(list2)

#using the sort() method
list_of_numbers=[1,2,4,6,8,7,56,34,67,89,23,56,47,90]
print(list_of_numbers)
list_of_numbers.sort()
print(list_of_numbers)

list_of_alphabets=['a','b','c','A','B','C']
print(list_of_alphabets)
list_of_alphabets.sort()
print(list_of_alphabets)
#if you intend to start with small letters
list_of_alphabets.sort(key=str.lower)
print(list_of_alphabets)
#cannot sort numbers and strings together

#using reverse() in python
names=["hately",'lovely','fondly']
print(names)
names.reverse()
print(names)
