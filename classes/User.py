class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = ""
        self.number = 0
        self.login_attempts = 0

    def discribe_user(self):
        print("user's name: " +self.last_name+"\n user's Gmail: "+self.email+"\n user's number: " +str(self.number) )

    def greet_user(self):
        print("Hi "+self.first_name+" good day to you")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
         self.login_attempts = 0
      

user = User('jhon', 'bloodborn')

user.discribe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

