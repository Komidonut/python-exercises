import time
pattern=input('print some text,pls!')
pattern_length = len(pattern)
while True:
    for i in range(0,pattern_length+1):
        time.sleep(0.1)
        print(' ' * i + pattern)
    for j in range(pattern_length,-1,-1):
        time.sleep(0.1)
        print(' ' * j + pattern)
