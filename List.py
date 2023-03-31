List = [1, 2, 33, 4, 5, 6, 7, 8, 9, 10]
print("Length of list:", len(List))  
print("Accessing item from list:", List[0])  

List.remove(2) 
print("After removing element '2':", List)

List.append(999)  
print("After appending '999'", List)

List.pop() 
print("Popping last element from the list: ", List)

sorted_list = List.copy() 

sorted_list.sort() 
print(sorted_list) 

print("Forward slicing", List[0:3:1]) 
print("Backward Slicing", List[-1::-1])  
print()
#comparsion of list

l1 = input("Enther the list like [a,b,c,d...]")
l2 = input("Enther the list like [a,b,c,d...]")

if l1 == l2:
 print("list are same")
else:
 print ("not same")
