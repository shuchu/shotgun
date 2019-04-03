#!/usr/bin/env python3
import sys
import scipy.io as si
import numpy as np

if __name__ == "__main__":
    ifile = sys.argv[1]
    print('input file: {}'.format(ifile))
    d = np.genfromtxt(ifile, delimiter=',')
    si.mmwrite(ifile[:-4]+'.mtx', d)
    print('output file: {}'.format(ifile[:-4]+'.mtx'))

