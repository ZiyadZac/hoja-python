try:
 number = int (input ("Enter a number: "))
 result = 10 / number
 print(result)
except ValueError:
   print("Enter a valid number")
except ZeroDivisionError:
   print("You cannot divide a number by 0")
else:
  print('bye bye')