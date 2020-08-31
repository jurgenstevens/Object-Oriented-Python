# Inheritance
class User:
    def log(self):
        print(self)  # => AttributeError: 'Customer' object has no attribute 'log'
                    # you'll get an error unless you pass User as a parameter for the Custoer class

# Polymorphism 
class Teacher(User):
    def log(self):
        print("I'm a teacher")

class Customer(User): # initialize the parameters below
    # Initialize method
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    # we're going to make name a property with two methods
    @property
    def name(self):
        return self._name #this is private

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter # this deletes the name attribute from the customer class
    def name(self):
        del self._name

    def update_membership(self, new_membership):
        print("Calculating costs")
        self.membership = new_membership

    # printing all the customers method with NO SELF
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    #  this method will converst a customer to a string
    def __str__(self):
        return self.name + " " + self.membership

    # Equals method
    def __eq__(self, other):
        if self.name == other.name and self.membership == other.membership:
            return True
        
        return False

    __hash__ = None

    __repr__ = __str__


# # create the customer like this
# jurgen = Customer("Jurgen", "Premium")
# print(jurgen.name, jurgen.membership)
# # another example of creating a customer
# caleb = Customer("Caleb", "Bronze")
# print(caleb.name, caleb.membership)


#  you can create a list of objects created with the class. They're arguments
customers = [Customer("Jurgen", "Premium"), 
            Customer("Caleb", "Bronze"),
            Teacher()]

print(customers[1].name) # => Caleb

# Custom Methods
# customers[1].verified = False
# print(customers[1].verified) # => False

# Use Custom Method to update the membership
# print(customers[1].membership) # => Bronze
# customers[1].update_membership("Gold")
# print(customers[1].membership) # => Gold  

# convert customer to string
print(customers[1]) # Caleb Bronze
customers[1].update_membership("Gold")
print(customers[1]) # => Caleb Gold

#Print all of the customers
Customer.print_all_customers(customers)
# => Jurgen Premium
#    Caleb Bronze

# Equals
print(customers[0] == customers[1]) # False

print(customers)  # => [Jurgen Premium, Caleb Gold]

# Encapsulation - The whole idea behind it is you can hide the inner details of a class or certain data.
# and you only need to share or expose what is needed for the user of the class to use this class

# Inheritance - Allows us to have certain attributes for objects because they're defined in a base class

# Polymorphism - It's the same thing as inheritance except special abilities/methods can be added to each individual object

customers[0].log() # => Jurgen Premium

customers[2].log()

users = [Customer("Jurgen", "Premium"),
             Customer("Caleb", "Bronze"),
             Teacher()]

#  loop the log for each user in the array of users
for user in users:
    user.log()