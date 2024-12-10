import sys
import subprocess
import board
import busio
import adafruit_mlx90640
from datetime import datetime
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
#from sendnotif import sendNotification

'''
def Adddata(Number) :
    cred = credentials.Certificate('./credentials.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection("Egg").document("Actually")
    doc_ref.set({"nombre" : Number})
'''

#Get data from thermal camera and write them in a file
def write_input():
    i2c = busio.I2C(board.SCL, board.SDA)
    mlx = adafruit_mlx90640.MLX90640(i2c)
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
    frame = [0] * 768
    mlx.getFrame(frame)
    file_name = "input.txt"
    f = open(file_name, "w")
    for h in range(24):
        for w in range(32):
            t = frame[h * 32 + w]
            c = "X"
            if t < 23:
                c = "."
            elif t < 25:
                c = "-"
            elif t < 27:
                c = "*"
            elif t < 29:
                c = "+"
            elif t < 31:
                c = "x"
            elif t < 33:
                c = "%"
            elif t < 35:
                c = "#"
            elif t < 37:
                c = "X"
            f.write(c)
        f.write("\n")
    f.close()




def main():
    
    write_input()
    process = subprocess.Popen(["./detection", "./input.txt"], stdout=subprocess.PIPE)
    output, err = process.communicate()
    output = output.decode("utf-8")
    sys.stdout.write(output)
    output = int(output)

    '''
    if (output):
        
        if output == 1:
            body='Hey, you got an egg ! 🥚'
        else:
            body='Hey, you got ' + str(output) + ' eggs ! 🥚'
        
        response = sendNotification(
        token='ExponentPushToken[token]', #put token here
        title='MyChicken',
        body=body)
    Adddata(output)
    '''
    if (output)>1:
        print(f"{output} eggs detected")
    else:
        print(f"{output} egg detected")

if __name__ == "__main__":
    main()
