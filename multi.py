#2.5 gb

import psutil
import os
print('there are three docker images present in the computer \n 1:nvidia-smi,\n 2:rah:1.0,\n 3:cv:1.0')
mem_req =3

def docks(a):
    #print('there are three docker images present in the computer \n 1:nvidia-smi,\n 2:rah:1.0,\n 3:cv:1.0')
    if a == 1:
        os.system(' sudo docker run --gpus all nvidia/cuda:10.0-base nvidia-smi')
    elif a == 2:
        os.system('sudo docker run --gpus all rah:1.0')
    elif a == 3:
        os.system('sudo docker run --rm -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --env="QT_X11_NO_MITSHM=1" cv:1.0')


while mem_req<psutil.virtual_memory()[1]/1000000000:
    psutil.virtual_memory()[1]
    a = int(input('enter between 1 and 3'))
    docks(a)
   
#request = input('do you want to go back to the begining of the while loop')

   

        

    
