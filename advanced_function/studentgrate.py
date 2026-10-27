eng=float(input('Mark In English:(out of hundred) '))
ss=float(input('Mark In Social Science: '))               
math=float(input('Mark In Math: '))
comp=float(input('Mark In Computer: '))
s=float(input('Mark In Science: '))
print()

def calculate_total():
  global z
  z=eng+ss+math+comp+s
  print('Total mark:',z)

calculate_total()

def calculate_avg():
  global f
  f=z/5
  print("Average mark:",f)

calculate_avg()

def grade():
  if f>=90:
    print("Grade A+")
  elif f>=80:
    print("Grade A")
  elif f>=70:
    print("Grade B")
  elif f>=60:
    print("Grade C")
  elif f>=50:
    print("Grade D")
  else:
    print("Grade:Fail")
    return "fail"

if grade()=="fail":
  print("Result:Fail")
else:
  print("Result:Pass")