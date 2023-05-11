import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os
import winsound

# from gtts import gTTS
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
# sound_obj=gTTS(text="Accident has occured",lang='en',slow=False)
# sound_obj.save("accident.mp3")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
try:
    os.remove("sampleT.txt")
except:
    pass
def animate(i):
    pullData = open("sampleT.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            if int(float(x)) in xar:
                continue
            else:
            	xar.append(int(float(x)))
            	yar.append(int(float(y)))
    ax1.clear()
    ax1.plot(xar,yar)
    try:
        acc=(yar[-1]-yar[-2])/1.5
        if(acc<-30):
            print("Accident has happened")
            winsound.Beep(frequency, duration)
            # os.system("accident.mp3")


        print(acc)
    except:
        pass
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()