import random
import time
import subprocess
from difflib import SequenceMatcher
import time


a = 1
b = 1
c = 1

text = ""

with open("words.txt", "r") as file:
  text = file.read()

words = text.split("\n")


name=str(input("Welcome to Type Racer!\nWhat is your name?\n"))
print("Hello",name+". Would you like to start?\n")

while a == 1:
    answer=str(input())
    if (answer in ["yes", "Yes"]):
        print("\nGreat! Lets start then!")
        a = 2
        break
    elif (answer in ["no", "No"]):
        print("Thats disappointing.")
        time.sleep(5)
        #popen.terminate()
    else:
        print("Sorry, I didn't quite get that, can you answer with either yes or no?")


print("You will get a random sentence, which you must type out as fast as possible.\nYou must also be as accurate as possible.\n")
print("Ready?")
while a == 1:
    answer=str(input())
    if (answer in ["yes", "Yes"]):
        print("Starting in 5 seconds!")
        b = 2

        break
    elif (answer in ["no", "No"]):
        print("Thats disappointing.")
        time.sleep(5)
        #popen.terminate()
    else:
        print("Sorry, I didn't quite get that, can you answer with either yes or no?")

while c == 1:
    start = time.time() 
    random.shuffle(words)
    print("\n")
    print(words[0])
    ansString=str(input())
    end = time.time()

    s = SequenceMatcher(None, ansString, words[0])

    ratio = s.ratio() * 100
    timeSpent = end - start


    print(f"\nYou completed the sentence in {timeSpent:.1f} seconds. Your accuracy was {ratio:.2f}%. Congratulations! Do you want to try again?\n")
    retryAgain=str(input())

    if (retryAgain in ["no", "No"]):
        break
    else:
        print("\n")
