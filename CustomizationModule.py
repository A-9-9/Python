# when is import the module, python would seek the py file under the specific path
# the path is setting under the sys.path variable, if we wanna import some module but not under the seek
# we can change the path file for python to seek.

import sys
sys.path.append('/test')
# import success cause we append the module path, and python can find the module
import test01
