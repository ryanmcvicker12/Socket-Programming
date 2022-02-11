#prototype for parsing command line arguments in this 
# client/server project, cause trig is boring and i have
# nothing else better to do 

''' if you wanna know what i'm doing or how i'm doing 
this, it's all from official documentation. Heres a link 

https://docs.python.org/3/howto/argparse.html

'''
import argparse  # BRAND NEW!!!! SOO SHINYYYY!!! ( kinda  )


parser = argparse.ArgumentParser()
parser.parse_args()

#been a while since parsing command line arguments so this might be a little sloppy at the moment 


#need to figure out if persistentConnection and nonPersistentConnection are optional or not . For now they are optional
# but going to default to persistantConnection for TCP's sake
''' basically copying over this long sentence 
               print("usage: server.py [options] [target]\nOptions:\n\t-p\t\tinclude to enable Persistant Connection with client\n\t-P, --port\t\tSpecify port number for server [not working]\n\n")
'''
parser.add_argument("-p" , help="Include to enable Persistant Connection with client.")
parser.add_argument("-P", "--port",type=int , help="Include to enable Persistant Connection with client.")

args = parser.parse_args()

# check input to stop the wrong ports from being used 
if args.port:
    print(f"port number entered : {args.port}")



