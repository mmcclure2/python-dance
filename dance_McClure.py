from Myro import *
initialize ("com4")

def yoyo(speed, waitTime):
    forward(speed, waitTime)
    backward(speed, waitTime)
    stop()

def wiggle(speed, waitTime):
    motors(-speed, speed)
    wait(waitTime)
    stop()

def dance():
    yoyo(0.5, 0.5)
    yoyo(-0.5, 0.5)
    wiggle(0.5, 1)
    wiggle(-0.5, 1)
    wiggle(-0.5, 1)
    wiggle(0.5, 1)

def main():
    print("Running the dance routine...")
    for danceStep in range(5):
        dance()

    print("I'm done!!!")

main()


