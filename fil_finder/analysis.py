'''

Analysis routines for the output of the filament finder. These can be run from the filament finder or from a saved .csv file.

'''

import numpy as np
from scipy.stats import nanmean, nanmedian, nanstd

class Analysis(object):
    """

    The Analysis class is meant to house the statistical analysis of the fil_finder output.
    *The complete functionality is not yet in place.*

    """
    def __init__(self, dataframe, save=False ,save_name=None, verbose=False):
        '''
        Parameters
        ----------

        dataframe : Pandas dataframe
                    The dataframe contains the output of fil_finder. This is the .csv file
                    saved by the algorithm.

        verbose : bool
                  Enable this for visual inspection of this histograms. If False,
                  it will enable saving the plots.

        save : bool
               This sets whether to save the plots.

        save_name : str
                    The prefix for the saved file. If None, the name from the header is used.
        '''
        super(Analysis, self).__init__()
        if isinstance(dataframe, str):
            from pandas import read_csv
            self.dataframe = read_csv(dataframe)
        else:
            self.dataframe = dataframe
        self.save_name = save_name
        self.verbose = verbose
        self.save = save



    def make_plots(self, num_bins=50):
        import matplotlib.pyplot as p

        ## Histogram of Widths
        widths = [float(x) for x in self.dataframe["Widths"] if is_float_try(x)]
        widths_stats = [nanmean(widths), nanstd(widths), nanmedian(widths)]

        ## Histogram of Lengths
        lengths = self.dataframe["Lengths"]
        lengths_stats = [nanmean(lengths), nanstd(lengths), nanmedian(lengths)]

        ## Histogram of Curvature
        rht_curvature = self.dataframe["RHT Curvature"]
        rht_curvature_stats = [nanmean(rht_curvature), nanstd(rht_curvature), nanmedian(rht_curvature)]



        if self.verbose:
            print "Widths Stats: %s" % (widths_stats)
            print "Lengths Stats: %s" % (lengths_stats)
            print "Curvature Stats: %s" % (rht_curvature_stats)

            p.subplot(131)
            p.hist(widths, num_bins)
            p.xlabel("Widths (pc)")
            p.subplot(132)
            p.hist(lengths, num_bins)
            p.xlabel("Lengths (pc)")
            p.subplot(133)
            p.hist(curvature, num_bins)
            p.xlabel("Curvature")
            p.show()
        if self.save:
            p.hist(widths, num_bins)
            p.xlabel("Widths (pc)")
            p.savefig("".join([self.save_name,"_widths.pdf"]))
            p.close()

            p.hist(lengths, num_bins)
            p.xlabel("Lengths (pc)")
            p.savefig("".join([self.save_name,"_lengths.pdf"]))
            p.close()

            p.hist(rht_curvature, num_bins)
            p.xlabel("RHT Curvature")
            p.savefig("".join([self.save_name,"_rht_curvature.pdf"]))
            p.close()

        return self

def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False