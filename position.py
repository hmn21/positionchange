from optparse import OptionParser
import os
import csv
import sys
import logging
import traceback
import shutil

log = logging.getLogger('python_logger')
log.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 2015-08-28 17:01:57,662 - simple_example - ERROR - error message
# formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d: %(message)s')
formatter = logging.Formatter('%(asctime)s %(levelname)-2s [%(filename)s: %(lineno)d] %(message)s')


# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)

usage = "usage: position.py [options] arg"
parser = OptionParser(usage)
parser.add_option("-d", "--directory", dest="directoryname", help="state file directory", metavar="DIR")
options, args = parser.parse_args()
if options.directoryname is None:   # if filename is not given
    log.error('Directoryname not given')
    sys.exit(1)
directory = options.directoryname
log.info('Directory name: %s', directory)
try:
	os.chdir(directory)
	file_list = os.listdir('.')
	for filename in file_list:
		if filename.endswith("_Pos.csv"):
			f1 = open(filename, 'r')
			f2 = open(filename+'_new', 'w')
			reader = csv.reader(f1)
			writer = csv.writer(f2)
			rownum = 0
			for row in reader:
				if rownum == 0:
					header = row
					writer.writerow(row)
				else:
					l = row
					l[1] = int(l[1]) + int(l[3])
					l[2] = int(l[2]) + int(l[4])
					l[3] = 0
					l[4] = 0
					writer.writerow(row)
				rownum += 1
			f1.close()
			f2.close()
			#shutil.move(filename+'_new', filename)
			log.info("Finished position change on %s", filename)
except Exception as e:
	log.error("Got an exception: %s", traceback.format_exc())
	sys.exit(1)
log.info("Finished on: %s", directory)

