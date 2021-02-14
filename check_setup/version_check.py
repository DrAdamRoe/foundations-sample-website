import sys

message = """
############# oh no! ################
## You need Python 3.8 or higher.  ##
## You are using version {}.{}       ##
#####################################

To troubleshoot, make sure that you:

- have Python >3.8 installed
- use the right command, which could be "python3" or "python" or "python3.8"
- have activated the correct virtual environment, if you are using it

## If you are stuck, please contact a fellow student or one of the teachers

""".format(sys.version_info.major, sys.version_info.minor)

if sys.version_info < (3, 8):
    print(message)
    sys.exit(1)

print("\nYou are using a comptabile version of Python, good job!\n")
