import datetime

time = datetime.datetime.now()
def timestamp():
    f = open("/Users/andypatari/Development/code/post-projects/scraper-projects/myfile.txt", "a")
    f.write(f"testing, {time} \n")
    f.close()

if __name__ == "__main__":
    timestamp()