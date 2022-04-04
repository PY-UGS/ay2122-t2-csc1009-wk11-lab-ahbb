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

hours = -1
minutes = -1
seconds = -1

while hours<0 or hours>23:
    hours = int(input("Enter hours: "))
    if hours<0 or hours>23:
        print("Invalid input for hours.")

while minutes<0 or minutes>59:
    minutes = int(input("Enter minutes: "))
    if minutes<0 or minutes>59:
        print("Invalid input for minutes.")

while seconds<0 or seconds>59:
    seconds = int(input("Enter seconds: "))
    if seconds<0 or seconds>59:
        print("Invalid input for seconds.")


c = clockTime()
c.setTime(hours,minutes,seconds)
c.showTime()
