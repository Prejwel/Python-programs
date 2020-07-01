class Job:
    name="Prejwel"
    job1="iOS dev"
    job2="System eng"
    interest = "sports"
    def get_interest(self):
        return self.interest
    def set_interest(self,val):
        self.interest="Sports,"+val

    def work(self):
        print("Name is %s ,%s and %s are the jobs done so far"%(self.name,self.job1,self.job2))


    def __init__(self,name):
        self.name=name

obj=Job("Harindran")
obj.work()
print(obj.job2)
print(obj.job1)

obj.set_interest("Studies")
print(obj.get_interest())
