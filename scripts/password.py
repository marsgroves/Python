secret_password = "pazzw0rd!"

def apasswordcheker(password_checkers):
    if password == "pazzw0rd!":
        print("Congrats! You figured out the secret password!")

def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val
        
def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val

def password_chek(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 


groves = "jigowatt"
check = "FALSE"

while check == "FALSE":
 user_password = input("Hi Mr. Groves,  What is your password (lowercase only) ? ")
 if user_password == groves:
    check = "TRUE"    
    print("Hello Detective Groves, the last file you accessed is: topsecret.txt")
 elif user_password == "pazzw0rd!":
     print("Please dont look at the code to figure out the password")

 else:
    print("That is incorrect, please try again")

def passord_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 