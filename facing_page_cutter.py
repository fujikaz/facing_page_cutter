#!/usr/bin/env python3
# Copyright (c) 2022, Kazuhiro FUJIHARA

import PyPDF2
from optparse import OptionParser
import sys
import re
import copy

ROTATE_ANGLE = 90
vcut = False

# parse options and args
usage = "usage: /path/to/%prog [options] <pdf filename w/ .pdf>"
parser = OptionParser(usage = usage)
parser.add_option("-v", "--vertical", action="store_true", dest="vertical", help="縦書き(右開き)")

(options, args) = parser.parse_args()

if len(args) != 1:
    parser.print_help()
    sys.exit()

output_filename = re.match(r'(.*)\.pdf', args[0]).groups()[0] + '_cut.pdf'

# open files
pdf_reader = PyPDF2.PdfFileReader(args[0])
pdf_writer = PyPDF2.PdfFileWriter()

# get page size
page = pdf_reader.getPage(0)
(x0, y0) = page.mediaBox.getLowerLeft()
(x1, y1) = page.mediaBox.getUpperRight()

if x1 - x0 > y1 - y0:
    vcut = True

# crop half size pages and rotate if needed
for i in range(pdf_reader.getNumPages()):
    p1 = pdf_reader.getPage(i)
    p2 = copy.copy(p1)
    if vcut == True:
        p1.cropBox.lowerLeft = (x0, y0)
        p1.cropBox.upperRight = ((x0 + x1) / 2, y1)
        p2.cropBox.lowerLeft = ((x0 + x1) / 2, y0)
        p2.cropBox.upperRight = (x1, y1)
    else:
        p1.cropBox.lowerLeft = (x0, y0)
        p1.cropBox.upperRight = (x1, (y0 + y1) / 2)
        p2.cropBox.lowerLeft = (x0, (y0 + y1) / 2)
        p2.cropBox.upperRight = (x1, y1)
        p1.rotateClockwise(ROTATE_ANGLE)
        p2.rotateClockwise(ROTATE_ANGLE)
    
    if options.vertical is True:
        p1, p2 = p2, p1

    pdf_writer.addPage(p1)
    pdf_writer.addPage(p2)

with open(output_filename, mode='wb') as f:
    pdf_writer.write(f)