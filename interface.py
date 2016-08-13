import os
import time
import serial

#Constant variable, denotes total number of choices available on menu
CHOICES = 2

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
                liveData = open("live.txt", "a")
                #data = arduino.readline()
                liveData.write(data)
                #print "monitoring!\n"
                liveData.close()

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
