from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_password(password):
    result = zxcvbn(password)
    score = result['score']
    if score  == 3 or score == 4:
        response = f"Strong enough Password: score of {score}"
    else:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = f"Weak Password: Score of {score}"
        response += "\nSuggestions: "
        
        for suggestion in suggestions:
            response += ' ' + suggestion
    return response

def hash_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(pw_attempt, hashed):
    if bcrypt.checkpw(pw_attempt.encode(), hashed):
        return "Password is correct. Access Granted!"
    else:
        return "Password is incorrect. Access Denied!"
    
if __name__ == "__main__":
    while True:
        password1 =getpass("Enter a Password to check strength: ")
        print(check_password(password1))
        if check_password(password1).startswith("Weak"):
            print("Please choose a stronger password")
        else:
            break 
        
    hashed_pw = hash_pw(password1)
    print(f"Hashed Password: {hashed_pw}")
    pw_attempt = getpass("Re-enter your password for verification: ")
    print(verify_password(pw_attempt, hashed_pw))
    