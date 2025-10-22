#take user marks from user with in 0 to 50
#if user enter outside 0-50 raise Error InvalidMark using Custom Exception
#Give chance to the user till user entered valid marks

# class Invalidmark(Exception):
#     pass

# def mark(mark):
#     if (mark<0 or mark>50):
#         raise Invalidmark("Invalid Mark. Please try again") 
#     else:
#         print (f"Mark {mark} is a  valid mark") 

# while True:
#   try: 
#     marks = int(input("Enter mark between 0-50: "))
#     if (marks<0 or marks>50):
#        mark(marks)
#     else:
#        mark(marks)
#        break
#   except Invalidmark as e:
#    print("Invalid Mark", e)
#   except Exception as er:
#    print("Error", er)

#-----------------------------------
class Invalidmark(Exception):
    pass

def mark(mark):
    if (mark<0 or mark>50):
        raise Invalidmark("Please try again") 
    else:
        print (f"Mark {mark} is a  valid mark") 

while True:
  try: 
    marks = int(input("Enter mark between 0-50: "))
    mark(marks)
  except Invalidmark as e:
   print("Invalid Mark", e)
  except Exception as er:
   print("Error", er)
  else:
    print("Recorded")
    break
  choice = input("If you want to re-enter the mark, press y \t").lower()
  if(choice != 'y'):
     print("Bye")
     break