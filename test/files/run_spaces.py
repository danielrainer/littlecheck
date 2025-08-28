# RUN: /usr/bin/python3 %s %arg

import sys

print(sys.argv[1:])
# CHECK: ['arg with spaces']
