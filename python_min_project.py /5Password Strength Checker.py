def get_password():
    pas=input("Enter the password")
    return pas

def check_length(pas):
    if len(pas)>=8:
        return True
    else:
        return False

def check_special_character(pas):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '?', '/']
    for i in pas:
        if i in symbols:
            return True
    
    return False

def check_numbers(pas):
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in pas:
        if i in numbers:
            return True
    return False

def display_strength():
    pas=get_password()
    #print(check_length(pas))#print(check_special_character(pas))#print(check_numbers(pas))
    i=0
    if check_length(pas)==True:
        i+=10
    if check_special_character(pas)==True:
        i+=10
    if check_numbers(pas)==True:
        i+=10
    if i==30:
        print("STRONG PASSWORD")
    elif i==20:
         print("MEDIUM PASSWORD")
    elif i==10:
        print("WEAK PASSWORD")
    else:
        print("VERY WEAK PASSWORD")




display_strength()