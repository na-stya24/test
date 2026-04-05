import hashlib
import itertools
import threading

"""
עליך לכתוב קוד אשר מבצע מתקפת 
bruteforce לפענוח סיסמה אשר הוצפנה באמצעות MD5
על הקוד לנסות את כל האפשרויות הקיימות אחת אחרי השנייה עבור סיסמה באורך 6 בעלת מספרים בלבדו
"""
# -----------------------------------------------------------------------------------------------------#

"""
BRUTEFORCE:
    Password cracking: A common example is a brute force attack, where a program tries all possible password combinations
      to gain access to an account. 
    Brute force algorithms: This is a type of algorithm that solves a problem by exhaustively checking every possibility,
      which can be a valid approach when a more intelligent, efficient algorithm is not feasible. 
"""
#-------------------------------------------------------------------------------------------------------#
"""
MD5:
    a hash function that generates a 128-bit "fingerprint" for any given data
מתקפת MD5:
     This happens when a malicious file is created to have the same MD5 hash value as a legitimate file
"""

# First function  gives as random password with 6 digits
def generete_password():
    words = "" # instructions such as those that may be in a random password
    password = itertools.product(words, repeat=6)
    return password

# we need to turn password into hashed password
def calculate_md5(text):
    # ENCODE - the process of converting text into a numerical format
    return hashlib.md5(text.encode("utf-8")).hexdigest() 

def copy_to_list(iter_list):
    new_list = []
    for item in iter_list:
        new_list.append(" ".join(item))
    return new_list

# function that includes two functions in one(generete_password + calculate_md5)
def decode_md5(hashed_password, possible_password):
    possible_passwords = generete_password()
    for password in possible_passwords:
        password = "".join(password)
        print("Trying: {}".format(password))
        if calculate_md5(password) == hashed_password:
            print("The password: {}".format(password))
            return password
    print("No password found")
    return None

if __name__ == "__main__":
    hashed_password =" "
    # from password to the list
    possible_passwords = generete_password()
    possible_passwords =  copy_to_list(possible_passwords)
    # the creation of the lists
    middle_index = int(len(possible_passwords) / 2) 
    start_to_middle = possible_passwords[:middle_index]
    middle_to_end = possible_passwords[middle_index + 1:]
    # the divaded work for two threads for each thread one half of the ist
    first_half_list_trd = threading.Thread(target=decode_md5, args=(hashed_password, start_to_middle))
    second_half_list_trd =threading.Thread(target=decode_md5, args=(hashed_password, middle_to_end))

    first_half_list_trd.start()
    second_half_list_trd.start()
    # the function that says that the main need to wait until the threds will finish their work
    first_half_list_trd.join()
    second_half_list_trd.join()
    

