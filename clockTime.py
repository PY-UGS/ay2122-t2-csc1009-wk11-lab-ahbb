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

while True:        
    hours = int(input("Enter hours: "))
    while hours<0 or hours>23:
        print("Invalid input for hours.")
        hours = int(input("Enter hours: "))

    minutes = int(input("Enter minutes: "))
    while minutes<0 or minutes>59:
        print("Invalid input for minutes.")
        minutes = int(input("Enter minutes: "))

    seconds = int(input("Enter seconds: "))
    while seconds<0 or seconds>59:
        print("Invalid input for seconds.")
        seconds = int(input("Enter seconds: "))

    c = clockTime()
    c.setTime(hours,minutes,seconds)
    c.showTime()
