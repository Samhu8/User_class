
# Create a file with the User class, including the __init__ with all the attributes,
# parameters and default values.

class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Add the display_info(self) method to the User class
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Hello {self.first_name}, it is {self.is_rewards_member} that you are now a member. You have {self.gold_card_points} points!")

    # have this method decrease the user's points by the amount specified
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points < 0:
            print("Sorry, you don't have enough points. Cannot process request")
        else:
            print(f"Hello {self.first_name}, you now have {self.gold_card_points} points.")




# In the outer scope, create a user instance and call the display_info method to test.
user_1 = User("Don","Draper","madmen01@codingdojo.com", 45)
user_1.display_info()

# Add the enroll method to the User class, implement and test by calling the method
# on the user in the outer scope.
user_1.enroll()

user_2 = User("Ted", "Lasso", "richmond01@codingdojo.com", 40)
user_3 = User("Michael","Scott", "dunder01@codingdojo.com", 42)


# Have the user spend 50 points
user_1.spend_points(50)

# Have the second user enroll
user_2.enroll()

# Have the second user spend 80 points
user_2.spend_points(80)

# Call the display method on all users.

user_1.display_info()
user_2.display_info()
user_3.display_info()

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
user_1.enroll()

# BONUS: Implement the logic to prevent over-spending and call the spend_points
# method with 40 points on the 3rd user.
user_3.spend_points(40)
