def pangram(str):
    alphabet=("abcdefghijklmnopqrstuvwxyz")
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string=input("please enter the sentence")
if(pangram(string)==True):
    print("the given input is a pangram")
else:
    print("the given input is not a pangram")

       
      
