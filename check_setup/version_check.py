import sys

if sys.version_info < (3, 8):
    message = """ 
    ########### oh no! ##########
    You need Python 3.8 or higher. You are using version %i.%i 
    """ % (sys.version_info.major,sys.version_info.minor)
    print(message)
    sys.exit(1)

print("You are using a comptabile verison of Python, good job!")
