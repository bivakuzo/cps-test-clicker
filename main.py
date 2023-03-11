import mouse
import keyboard
import time
# after_10_sec = time.time()+10
after_1_sec = time.time()+1

while time.time()<=after_1_sec:
    mouse.click('left')
    time.sleep(0.1)
