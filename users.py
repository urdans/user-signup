import re


class Users:
    user_list = []
    _userdata = {}

    def __init__(self):
        super()
        self.add_user("urdans", "12345678", "urdans@gmail.com")
        self.add_user("coffecup", "12345678", "coffecup@hotmail.com")
        self.add_user("theknight", "12345678", "theknight@yahoo.com")

    def add_user(self, username, password, email):
        self._userdata.clear()
        self._userdata.update(self.checkusername(username))
        self._userdata.update(self.checkpassword(password))
        self._userdata.update(self.checkemail(email))

        if ("UserError" in self._userdata) or ("PasswordError" in self._userdata) or ("EmailError" in self._userdata):
            return False

        for user in self.user_list:
            un = self._userdata["user_name"]
            if user["user_name"] == un:
                self._userdata.clear()
                self._userdata["UserError"] = "User '{}' already exist!".format(
                    un)
                return False

        self.user_list.append(dict(self._userdata))
        return True

    def checkusername(self, username):
        # rules for username goes here
        un = username.strip()
        if len(un) < 3 or len(un) > 20:
            return {"UserError": "User name must be between 3 and 20 characters long!"}
        elif ' ' in un:
            return {"UserError": "User name cannot contain middle spaces!"}
        else:
            return {"user_name": un}

    def checkpassword(self, password):
        # rules for passwords goes here
        if len(password) < 3 or len(password) > 20:
            return {"PasswordError": "Password must be between 3 and 20 characters long!"}
        elif ' ' in password:
            return {"PasswordError": "Passwords cannot contain spaces!"}
        else:
            return {"password": password}

    def checkemail(self, email):
        em = email.strip()
        if em == "":
            return {"email": ""}
        # using reg exp
        match = re.search(
            r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', em, re.I)
        if match:
            return {"email": match.group()}
        else:
            return {"EmailError": "Invalid email address!"}

        # if (len(em) < 3) or (len(em) > 20) or (em.count("@") != 1) or (em.count(".") != 1) or (" " in em):
        #     return {"EmailError": "Invalid email address!"}
        # else:
        #     return {"email": em}

    def get_username_error(self):
        if "UserError" in self._userdata:
            return self._userdata["UserError"]
        else:
            return ""

    def get_password_error(self):
        if "PasswordError" in self._userdata:
            return self._userdata["PasswordError"]
        else:
            return ""

    def get_email_error(self):
        if "EmailError" in self._userdata:
            return self._userdata["EmailError"]
        else:
            return ""

    def count(self):
        return len(self.user_list)


if __name__ == '__main__':
    user_list = Users()

    print(user_list.user_list)
    r = user_list.add_user("misterwho", "1234567", "misterwho@aol.com")
    if not r:
        print(user_list.get_username_error())
        print(user_list.get_password_error())
        print(user_list.get_email_error())

    print("There are {} registered users".format(user_list.count()))

    # s = '   manogna@a.com'  # .neelam@tutorialspoint.com'
    # match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', s, re.I)
    # if match:
    #     print(match.group())
    # else:
    #     print("bad email address")
