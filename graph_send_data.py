import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os
import winsound
import socket
import requests
import json
host = '192.168.43.12'
port = 3000
BUFFER_SIZE = 2000

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))


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
        MESSAGE = str.encode("{acceleration},{speed},{time}\n".format(acceleration=acc,speed=yar[-1],time=xar[-1]))
        if(acc<-30):
            # requests.get("http://localhost/sihcodes/twiliocall/makecall.php?number=918779686105")
            print("second call")
            winsound.Beep(frequency, duration)
        time.sleep(1)
        tcpClientA.send(MESSAGE)
        
            # text_send="GAJD6-919987746997-19.123456-72.123456"
            # mobile_to_send='919004910418'
            # response=json.loads(requests.get("https://www.smsgatewayhub.com/api/mt/SendSMS?APIKey=eOViacIZGkKbu8bo82s5xg&senderid=SMSTST&channel=2&DCS=0&flashsms=0&number={mobile_to_send}&text={text_send}&route=1".format(text_send=text_send,mobile_to_send=mobile_to_send)).text)
            # if(response['ErrorCode']=='000' and response['ErrorMessage']=='Success'):
            #     print("sms successfull")
            #     response_call=json.loads(requests.get("http://localhost/sihcodes/twiliocall/makecall.php?phone={phone1}".format(phone1='919987746997')).text)
            #     response_call_var=json.loads(requests.get("http://localhost/sihcodes/twiliocall/makecall.php?phone={phone2}".format(phone2='918779686105')).text)

            #     if(response_call['status']=='SUCCESS'):
            #         print("call successfull")
            #         print(response_call['message'])
            #     else:
            #         print(response_call['message'])
            # else:
            #     winsound.Beep(1000, 500)
            # requests.get("http://localhost/sihcodes/twiliocall/makecall.php?phone1={phone1}&phone2={phone2}".format(phone1='918779686105',phone2='919987746997'))



            # os.system("accident.mp3")


        print(acc)
    except:
        pass
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()