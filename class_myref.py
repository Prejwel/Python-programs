
class Job:
    job1="iOS dev"
    job2="System eng"
    def work(self):
        print("%s and %s are the jobs done so far"%(self.job1,self.job2))

# use self /object  while trying to access the class variable/method

obj=Job()
obj.work()
print(obj.job2)
print(obj.job1)
