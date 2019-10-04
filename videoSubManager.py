import re, sys, os
import argparse

abs_base_path = os.path.abspath('.')

#Parsing input
parser = argparse.ArgumentParser()
parser.add_argument('-target', '-t',
					help="Location of the folder that includes videos+sub files should be given",
					required=True)
parser.add_argument('-name', '-n',
					help="Name of the series (for naming files) (taking base folder name as default)",
					default=os.path.basename(os.path.abspath(''))
					)
args = parser.parse_args()

try:
	target_folder = os.path.abspath(args.target)
except Exception as e:
	print('Target folder error!')
	sys.exit()

try:
	fname = args.name
except Exception as e:
	print('Name Error!')
	sys.exit()

#Changing names
for root, dirs, files in os.walk(target_folder):
	for name in files:
		result = re.search(pattern=r"(S|s)\d+(e|E)\d+", string=name)
		if result:
			found = result.group()
			old_path = os.path.join(abs_base_path, root, name)
			new_name = fname + found + os.path.splitext(name)[1]
			new_path = os.path.join(abs_base_path, root, new_name)
			os.system("mv '{}' '{}'".format(old_path, new_path))
