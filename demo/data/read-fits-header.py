#!/bin/env python

from astropy.io import fits
import sys

if __name__ == "__main__":
    fits_file = sys.argv[1]
    hdus = fits.open(fits_file)
    if len(sys.argv) == 2:
        print(hdus.info())
        exit(0)
    hdu_index = int(sys.argv[2])
    for k, v in hdus[hdu_index].header.items():
        print(f"{k}: {v}")
