import sys

if sys.version_info < (3, 8):
    print("########### oh no! ##########")
    print("You need Python 3.8 or higher. You are using version %i.%i \n" % (sys.version_info.major,sys.version_info.minor ))
    sys.exit(1)

print("You are using a comptabile verison of Python, good job!")