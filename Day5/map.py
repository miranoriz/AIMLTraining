
#map()= apply a function to all items in an iterable

numbers = [10,20,30,40,50]
double_num = list(map(lambda x: 2*x, numbers)) 

print("Original list: ")
for n in numbers: 
   print(n,end=" " )

print("\nNew list: ")
for d in double_num: 
   print(d,end=" " )
