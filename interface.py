import os
import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#Constant variable, denotes total number of choices available on menu
CHOICES = 2
arduino = serial.Serial('COM5', 115200, timeout =.1)
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    liveData = arduino.readline()
    lines = arduino.split('\n')
    xs = []
    ys = []
    for line in lines:
	if len(line) > 1:
	    x, y = line.split(',')
	    xs.append(x)
	    ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)
    print liveData

try:
    #Main Menu
    valid = False
    os.system('cls' if os.name == 'nt' else 'clear')
    while not valid:
        print "Welcome!"
        print "Please make a selection: (Type 1,2,3...)"
        print "   1. Monitor"
        print "   2. Record"
        menuinput = input("Selection: ")
        if menuinput > CHOICES:
            os.system('cls' if os.name == 'nt' else 'clear')
            print "Please make another selection!"
        else:
            valid = True

    #Monitor
    if menuinput == 1:
        #Open .txt for real-time graph
            liveData = open("live.txt", "w+")
            #Initialize variable to accept characters
            data = "o"

        #Open Arduino serial port
            #arduino = serial.Serial('/dev/tty.usbserial', 15200, timeout=.1)

            print "Now monitoring. Press ctrl+c to stop program. "
            #Do all the monitoring things
            while True:
		ani = animation.FuncAnimation(fig,animate, interval = 1000)
		plt.show()
                
    #Record
    elif menuinput == 2:
    #Open .csv for data storage
        temp = raw_input("New Filename: (Date will be appended) ")
        #Get current date and time
        currDate = time.strftime("%d/%m/%Y")
        currTime =time.strftime("%I:%M:%S")
        #Concatenate temp, date and time
        dirName = temp + "-" + currDate + "-" + currTime
        #Replace "/" in file name to avoid directory problems
        dirName = dirName.replace("/",":")
        #Add file extension to filename
        fileName = dirName + ".csv"
        #Create directory
        os.mkdir(dirName)
        #Open File
        print "Opening: " + fileName
        excelData = open(dirName + "/" + fileName, "w+")

    #Open .txt for real-time graph
        liveData = open("live.txt", "w+")
        #Initialize variable to accept characters
        data = "o"

        print "Ready to Record. Press enter to begin. "
        raw_input()

    #Open Arduino serial port
        #arduino = serial.Serial('/dev/tty.usbserial', 15200, timeout=.1)

        print "Now recording. Press ctrl+c to stop program and end recording. "
        #Do all the recording things
        while True:
            liveData = open("live.txt", "a")
            excelData = open(dirName + "/" + fileName, "a")
            #data = arduino.readline()
            liveData.write(data)
            excelData.write(data)
            #print "recording!\n"
            liveData.close()
            excelData.close()


except KeyboardInterrupt:
    print "\nExiting!"
