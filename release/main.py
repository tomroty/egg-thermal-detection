import sys
import subprocess
import board
import busio
import adafruit_mlx90640
from datetime import datetime

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

    if (output)>1:
        print(f"{output} eggs detected")
    else:
        print(f"{output} egg detected")

if __name__ == "__main__":
    main()
