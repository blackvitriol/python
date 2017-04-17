#python hello world
#A7MD0V TEST

import time
answer = raw_input("Who are you ?")
print(answer)
if answer=="ahmad":
    print("Authenticating. Please wait.")
    time.sleep(0.5)
    print("Hello World, and hello Ahmad !")

else:
    print("Sorry, you aren't authorized to use this program.")
