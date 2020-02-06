import os
import sys

try:
    libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    sys.path.insert(0, libdir)
except:
    pass

import game

if __name__ == '__main__':
    game.run()
