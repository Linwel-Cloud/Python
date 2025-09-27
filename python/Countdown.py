import time
x = input("Enter a number to countdown from: ")

while int(x) >= 0:
    print(x)
    time.sleep(1)
    x = int(x) - 1
print("Countdown finished!")