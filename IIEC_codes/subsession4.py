import os
import pyttsx3
g = True
apps = ["chrome","notepad","jupyter notebook","wmplayer","idle","spyder"]
aff = ["run","load","launch","execute"]
print('Hello user, \nhere is the list of programs to run: \n')
pyttsx3.speak('Hello user, \nhere is the list of programs to run: \n')
for x in apps:
	print(x, end=', ' )
while g == True:
     print("\n\nEnter your command please : " , end="")
     pyttsx3.speak("\nEnter your command please ")
     com=input().lower().split()
     if "not" in com:
          print("\n\nCOMMAND DID NOT RUN !!!")
          pyttsx3.speak("COMMAND DID NOT RUN !!!")
     else:
          for j in apps:
               if j in com:
                    ch = j
          for i in aff:
               if i in com:
                    if os.system(ch) == 0:
                         print('\n\nPROGRAM EXECUTED SUCCESSFULLY!!!')
                         pyttsx3.speak('PROGRAM EXECUTED SUCCESSFULLY!!!')
                         break
                    else:
                         print("OOPS!!\nUNABLE TO EXECUTE PROGRAM.")
                         pyttsx3.speak("OOPS!! \nUNABLE TO EXECUTE PROGRAM.")
                         break
               else:
                    continue
     print('\n\nPress any key to continue or "n" to terminate: ', end="")
     pyttsx3.speak('\n\nPress any key to continue or "n" to terminate: ')
     ans = input().lower()
     if ans == "n":
           g = False
           print("\n\nBYE BYE !!!\n\n")
           pyttsx3.speak("Goodbye! have a nice day.")
