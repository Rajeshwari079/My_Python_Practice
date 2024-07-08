from abc import ABC, abstractmethod

class TimeTable:

    @abstractmethod
    def breakfast(self):
        pass

    @abstractmethod
    def lunch(self):
        pass

    @abstractmethod
    def dinner(self):
        pass

class Raji(TimeTable):
    
   
    def breakfast(self):
        print('South Indian')

    def lunch(self):
        print('North Indian')

    def dinner(self):
        print('sleep')


r=Raji()
r.breakfast
r.lunch
r.dinner
    


