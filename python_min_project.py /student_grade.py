
def get_marks():
    eng = float(input('Mark In English (out of hundred): '))
    ss = float(input('Mark In Social Science: '))               
    math = float(input('Mark In Math: '))
    comp = float(input('Mark In Computer: '))
    s = float(input('Mark In Science: '))
    return [eng, ss, math, comp, s]

def calculate_total(marks):
  z=sum(marks)
  print('Total mark:',z)
  return z 

def calculate_average(f):
  avg=f/5
  print("Average mark:",avg)
  return avg

def find_grade(f):
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

def display_result(grade):
  if grade == "fail":
    print("Result:Fail")
  else:
    print("Result:Pass")

marks=get_marks()
total=calculate_total(marks)
avg=calculate_average(total)
grade=find_grade(avg)
display_result(grade)