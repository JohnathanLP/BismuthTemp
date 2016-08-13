import serial
import time

#opening our text and CSV files for Write so we get a clean slate each time.
#You SHOULD rename the .txt and .csv file if you want to keep a copy of the
#code you ran last time before you run the code again.
liveData = open("temp.txt", "w")
excelData = open("temp.csv","w")

#opening the Serial port, COM will change depending on what is plugged into
#your computer at the time. In Windows you will search for Device Manager,
#press the line for COM and you can find which it is plugged into. You will
#have to do some digging around for how to see that on a MacOS.
arduino = serial.Serial('COM5', 115200, timeout=.1)
time.sleep(1)

#initializing data to accept characters.
data = 'o'

#the magic loop
#Will run indefinitely, it opens both .txt and .csv files to append to the
#current files. It will then read the serial communication from the arduino
#and write it to the .txt and .csv files. It is then printed to the screen
#for the user to see. After that it closes the files so that it simulates
#saving the files each time.
while True:
    liveData = open("temp.txt", "a")
    excelData = open("temp.csv", "a")
    data = arduino.readline()
    liveData.write(data)
    excelData.write(data)
    print data
    liveData.close()
    excelData.close()
