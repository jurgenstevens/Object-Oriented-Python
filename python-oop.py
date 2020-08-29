class Customer: # initialize the parameters below
    # INIT method
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    def update_membership(self, new_membership):
        self.membership = new_membership



# # create the customer like this
# jurgen = Customer("Jurgen", "Premium")
# print(jurgen.name, jurgen.membership)
# # another example of creating a customer
# caleb = Customer("Caleb", "Bronze")
# print(caleb.name, caleb.membership)


#  you can create a list of objects created with the class. They're arguments
customers = [Customer("Jurgen", "Premium"), 
            Customer("Caleb", "Bronze")]

print(customers[1].name) # => Caleb

# Custom Methods
# customers[1].verified = False
# print(customers[1].verified) # => False

# Use Custom Method to update the membership
print(customers[1].membership) # => Bronze
customers[1].update_membership("Gold")
print(customers[1].membership) # => Gold  
