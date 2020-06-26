# Class ,Object, default constructor, class method, class variable, self

class Phone:
    phone_version="SE"
    brand_name="iPhone"
    username=""
# when we create an object from class, by default constructor will be created
    def __init__(self,user):
        self.username=user
    def bootlogo(self):     #by default,  the methods will have arg as self
        print("Apple",self.phone_version) # inside a class method , call the class variable using self

prej=Phone("Prejwel")   #object creation ( here we have an arg bcz default constructor have an arg)
prej.bootlogo()     #call class method using object
