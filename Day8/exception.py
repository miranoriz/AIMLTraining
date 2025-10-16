try:
    fnum = float(input("Enter first number: "))
    snum = float(input("Enter second number: "))

    result = fnum/snum

    print(f'Result after dividing {fnum} and {snum} is {round(result,4)}')

except Exception as e:
    print('Error',e)

finally:
    print('good bye')
