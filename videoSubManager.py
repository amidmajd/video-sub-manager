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
					)
parser.add_argument('-exclude', '-e',
					help='exclude these folders from this program; format for multiple folders : -e "f1, f2, f3"',
					)
args = parser.parse_args()


try:
	if args.target is not None and args.target != "" and args.target != " ":
		target_folder = os.path.abspath(args.target)
	else:
		raise Exception
except Exception as e:
	print('Target folder error!')
	sys.exit()


try:
	if args.name is not None and args.name != "" and args.name != " ":
		fname = args.name
	else:
		fname = os.path.basename(target_folder)
except Exception as e:
	print('Name Error!')
	sys.exit()


try:
	if args.exclude is not None and args.exclude != "" and args.exclude != " ":
		excludes = args.exclude.split(', ')
	else:
		excludes = []
except Exception as e:
	print('Excludes Error!')
	sys.exit()


#Changing names
for root, dirs, files in os.walk(target_folder):
	if os.path.basename(root) not in excludes:
		for name in files:
			# searching for season number
			tmp_snumber = os.path.relpath(root)
			season_number = re.search(pattern=r"[1-9]+", string=tmp_snumber)
			if season_number is None:
				season_number = 0
			else:
				season_number = season_number.group()

			result = re.search(pattern=r"\d{1,2}.{0,3}\d{0,2}", string=name)

			if result is not None:
				numbers_list = re.findall(pattern=r"\d{1,2}", string=result.group())
				if len(numbers_list) == 1:
					s_num = season_number
					e_num = numbers_list[0]
				elif len(numbers_list) == 2:
					s_num, e_num = numbers_list
				else:
					print("????UNKOWN ERRRRRRRRRRRROR?????")
					sys.exit()
				s_num, e_num = s_num.zfill(2), e_num.zfill(2)


				old_path = os.path.join(abs_base_path, root, name)
				new_name = fname + "S" + s_num + "E" + e_num + os.path.splitext(name)[1]
				new_path = os.path.join(abs_base_path, root, new_name)

				if old_path != new_path:
					# print(old_path)
					print("New Filename:", new_path)
					os.system('mv "{}" "{}"'.format(old_path, new_path))
				else:
					pass
	else:
		print("Excluding", os.path.basename(root), "Folder")

print("Done!")
