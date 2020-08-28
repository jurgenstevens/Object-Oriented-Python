class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

# # create the customer like this
# jurgen = Customer("Jurgen", "Premium")
# print(jurgen.name, jurgen.membership)
# # another example of creating a customer
# caleb = Customer("Caleb", "Bronze")
# print(caleb.name, caleb.membership)


#  you can create a list of objects created with the class
customers = [Customer("Jurgen", "Premium"), 
            Customer("Caleb", "Bronze")]

print(customers[1].name) # => Caleb