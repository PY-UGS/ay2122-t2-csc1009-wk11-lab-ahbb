class clockTime:
    
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    
    def setHours(self,hours):
        self.hours = hours

    def setMinutes(self,minutes):
        self.minutes = minutes

    def setSeconds(self,seconds):
        self.seconds = seconds

    def setTime(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def showTime(self):
        print("Time is {}:{}:{}".format(self.hours,self.minutes,self.seconds))

hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")

c = clockTime()
c.setTime(hours,minutes,seconds)
c.showTime()