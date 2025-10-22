try:
    firstnum = int(input("Enter first number: "))
    secondnum = int(input("Enter second number: "))
    total = firstnum + secondnum
    div = firstnum/secondnum
    print(f'Result after dividing {firstnum} and {secondnum} is {div}')
    print(f"Sum of {firstnum} and {secondnum} is {total}")

except Exception as e:
    print('Error',e)

finally:
    print('End of program')