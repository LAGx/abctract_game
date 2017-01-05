import datetime


def clear(fileName = "log.txt"):
    file = open(fileName, "w")
    file.close()

def time():
    return "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":"+str(datetime.datetime.now().second) + "]"

def log(massage, fileName = "log.txt", timing = False):
    file = open(fileName, "a")
    if timing:
        file.write("LOG" + time() + ": " + massage + "\n")
    else:
        file.write("LOG: " + massage + "\n")
    file.close()

def error(massage, fileName = "log.txt", timing = False):
    print("ERROR: "+ massage)
    file = open(fileName, "a")
    if timing:
        file.write("ERROR" + time() + ": " + massage + "\n")
    else:
        file.write("ERROR: " + massage + "\n")
    file.close()