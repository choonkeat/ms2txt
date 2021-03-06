#!/usr/bin/env python
"""
Command line tool used to extract the data from metastock files and save it
in text format.
"""

import sys
import os.path
from optparse import OptionParser

from metastock.files import MSEMasterFile
from metastock.files import MSXMasterFile

Usage = """usage: %prog [options] [symbol1] [symbol2] ....

Examples:
    %prog -p 2 --all        extract all symbols from EMASTER file
    %prog FW20 "S&P500"     extract FW20 and S&P500 from EMASTER file
"""

def main():
    """
    launched when running this file
    """

    parser = OptionParser(usage=Usage)
    parser.add_option("-l", "--list", action="store_true", dest="list",
                  help="list all the symbols from EMASTER file")
    parser.add_option("-a", "--all", action="store_true", dest="all",
                      help="extract all the symbols from EMASTER file")
    parser.add_option("-p", "--precision", type="int", dest="precision",
                      help="round the floating point numbers to PRECISION digits after the decimal point (default: 2)")


    (options, args) = parser.parse_args()

    # check if the options are valid
    if not (options.all or options.list or len(args) > 0):
        parser.print_help()
        sys.exit(0)

    # list the symbols or extract the data
    if options.list:
        print "List of available symbols:"
        if os.path.exists('EMASTER'):
            MSEMasterFile('EMASTER', options.precision).list_all_symbols()
        if os.path.exists('XMASTER'):
            MSXMasterFile('XMASTER', options.precision).list_all_symbols()
    else:
        if os.path.exists('EMASTER'):
            MSEMasterFile('EMASTER', options.precision).output_ascii(options.all, args)
        if os.path.exists('XMASTER'):
            MSXMasterFile('XMASTER', options.precision).output_ascii(options.all, args)

if __name__ == "__main__":
    main()
