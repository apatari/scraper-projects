import datetime

time = datetime.datetime.now()

f = open("myfile.txt", "a")
f.write(f"testing, {time} \n")
f.close()