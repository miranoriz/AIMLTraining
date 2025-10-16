#filter condition

#-------------------------------------------

#filter even number in list

# numbers = [1,20,3,40,50]

# even_num = list(filter(lambda x: x%2==0, numbers)) 

# print("Original list: ")
# for n in numbers: 
#    print(n,end=" " )

# print("\nNew list: ")
# for d in even_num: 
#    print(d,end=" " )


#-------------------------------------------

#filter number less than 5 in list

# numbers = [4,2,5,6,7,3,1,10]

# new_num = list(filter(lambda x: x<5, numbers)) 

# print("Original list: ")
# for n in numbers: 
#    print(n,end=" " )

# print("\nNew list: ")
# for d in new_num: 
#    print(d,end=" " )

#-------------------------------------------

#filter mark less than 55 in dictionary

# student_marks = {'mira':22,
#                  'along':23,
#                  'serai':99,
#                  'maya':55}

# pass_student = dict(filter(lambda x : x[1]>40, student_marks.items()))

# print("\nThe student whose pass is: ", pass_student)

# print("\nThe student whose pass is: ")
# for k,v in pass_student.items(): 
#   print(f"Name: {k} & Mark: {v}")


#-------------------------------------------

#sorted by key

student_marks = {'mira':22,
                 'along':23,
                 'serai':99,
                 'maya':55}

# sorted_name = dict(sorted(student_marks.items()))
# print(sorted_name)
    

#-------------------------------------------

#sorted by value (descending)

student_marks = {'mira':22,
                 'along':23,
                 'serai':99,
                 'maya':55}

# sorted_name = dict(sorted(student_marks.items(), key=lambda item:item[1], reverse=True))
# print(sorted_name)

#-------------------------------------------

#sorted by value (ascending)

student_marks = {'mira':22,
                 'along':23,
                 'serai':99,
                 'maya':55}

# sorted_name = dict(sorted(student_marks.items(), key=lambda item:item[1]))
# print(sorted_name)

#-------------------------------------------

#sorted pass student by value (ascending)

student_marks = {'mira':22,
                 'along':23,
                 'serai':99,
                 'maya':55}

pass_student = dict(filter(lambda x: x[1]>40, student_marks.items()))
sorted_name = dict(sorted(pass_student.items(), key=lambda item:item[1]))

for k,v in sorted_name.items():
 print(f"Name: {k} and Mark: {v}")











