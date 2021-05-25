import random
import string
import time

class password_check:
    """Program to check password & release voucher."""

    def __init__(self, business):
        self.business = business.lower()
        self.count = 0
        self.voucher = ''
        self.usr = ''
        self.passwords = []
        self.unlocked = False

    # not needed in final version
    # def describe_business(self):
    #     return f"The business type is: {self.business}."

    def input_password(self):
        self.usr = input("Type password: ").lower()
        self.passwords = ['columbo', 'poirot', 'marple']
        return p1.check_password()

    def check_password(self):
        if self.usr in self.passwords:
            self.unlocked = True
            return p1.release_voucher()
        else:
            self.unlocked = False
            self.count += 1
            print("I'm sorry, that's not a winner! Please try again.")
            if self.count > 5:
                print("Too many incorrect entries: wait 10 seconds.")
                time.sleep(10)
                return p1.input_password()
            else:
                return p1.input_password()

    def release_voucher(self):
            return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

p1 = password_check('cinema') # create instance of class
# print(p1.describe_business()) # print to show that functions are returning
print(p1.input_password()) # functions within functions, so this is only necessary command
