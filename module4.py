import platform
import os



 
'''print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")'''

print('-----------------------------------------')
print('         YOUR SYSTEM INFORMATION         ')
print('-----------------------------------------')
print('                                         ')


while True:
    print("select operation -\n" \
        "1. OS Details\n" \
        "2. User Name\n" \
        "3. Basic Information\n" \
        "4. Exit\n"    )


    print('-----------------------------------------')                
    A=int(input('select a operation \n'))

    if A==1:
         print(os.name)
    elif A==2:
       print(os.getlogin())
    elif A==3:
      
        print(platform.uname())
    elif A==4:
        break
    else:
        print("error")