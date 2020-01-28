#!/usr/bin/env python

import sys
import subprocess

if sys.argv[1:]:
    try:
        #aws s3 cp sys.argv[1] s3://ninfo-gclid/
        cmdline = 'aws s3 cp ' + str(sys.argv[1]) + ' s3://ninfo-gclid/'
        subcmd = subprocess.Popen(cmdline.split(), stdout=subprocess.PIPE)       
        exitcode = subcmd.wait()
        if (exitcode != 0):
            print('Error exitcode: ' + str(exitcode))
            sys.exit(exitcode)
        for line in subcmd.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
    except Exception as e:
        print(str(e))
        sys.exit(1)
sys.exit(0)
