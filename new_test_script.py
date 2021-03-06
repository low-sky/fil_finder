#!/usr/bin/python

from fil_finder import *
from astropy.io.fits import getdata

img,hdr = getdata("/srv/astro/erickoch/gould_belt/chamaeleonI-250.fits",
    header=True)

## Utilize fil_finder_2D class
## See filfind_class.py for inputs
test = fil_finder_2D(img, hdr, 15.1, 30, 5, 50, 95 ,distance=145, glob_thresh=20, region_slice=[620,1400,430,1700])
test.create_mask(verbose=False)
test.medskel()
test.analyze_skeletons()
test.exec_rht(verbose=True)
test.find_widths(verbose=True)
# test.run(verbose=True, save_name="chamaeleonI-250", save_plots=False) ## Run entire algorithm


