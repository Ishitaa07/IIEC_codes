import os
g = True
apps = ["chrome","notepad","jupyter notebook","media player","idle","spyder"]
aff = ["run","load","launch","execute"]
print('Hello user, \nhere is the list of programs to run: \n')
for x in apps:
	print(x, end=', ' )
while g == True:
     print("\nEnter your command please : " , end="")
     com=input().lower().split()
     if "not" in com:
          print("COMMAND DID NOT RUN !!!")
     else:
          for j in apps:
               if j in com:
                    ch = j
          for i in aff:
               if i in com:
                    if os.system(ch) == 0:
                         print('PROGRAM EXECUTED SUCCESSFULLY!!!')
                         break
                    else:
                         print("OOPS!! \nUNABLE TO EXECUTE PROGRAM.")
                         break
               else:
                    continue
     print('Press any key to continue or "n" to terminate: ', end="")
     ans = input().lower()
     if ans == "n":
           g = False
           print("BYE BYE !!!")
