# This is a script that is going to write something before every line in python.

FILENAME = ''

class modify:
	
	@staticmethod
	def replace_in_each_line(what_to_change, change):
		with open(FILENAME, 'r') as f:
			stuff_in_file = f.readlines()
			for i in range(len(stuff_in_file)):
				stuff_in_file[i] = stuff_in_file[i].replace(what_to_change, change)
		with open(FILENAME, 'w') as f:
			f.writelines(stuff_in_file)
	
class add:
		
	# this function will obviously add whatever you say in the beginning of each line in a text file
	@staticmethod
	def add_before_beginning_line(change):
		
		with open(FILENAME, 'r') as f:
			stuff_in_file = f.readlines()

		for i in range(len(stuff_in_file)):
			stuff_in_file[i] = change + stuff_in_file[i]
			
		with open(FILENAME, 'w') as f:
			f.writelines(stuff_in_file)

	# This funciton will add a string after the end of each line.
	@staticmethod
	def add_after_end_line(change):
		with open(FILENAME, 'r') as f:
			stuff_in_file = f.readlines()

		for i in range(len(stuff_in_file)):
			stuff_in_file[i] = stuff_in_file[i].rstrip('\n') + change + '\n'
		
		with open(FILENAME, 'w') as f:
			f.writelines(stuff_in_file)
	
class remove:
	
	@staticmethod
	def del_from_end_lines(change):
		with open(FILENAME, 'r') as f:
			stuff_in_file = f.readlines()

		for i in range(len(stuff_in_file)):
			stuff_in_file[i] = stuff_in_file[i].rstrip('\n')
			stuff_in_file[i] = stuff_in_file[i].rstrip(change)
			stuff_in_file[i] = stuff_in_file[i] + '\n'
			
		with open(FILENAME, 'w') as f:
			f.writelines(stuff_in_file)
	
	@staticmethod
	def del_from_beginning_lines(change):
		with open(FILENAME, 'r') as f:
			stuff_in_file = f.readlines()

		for i in range(len(stuff_in_file)):
			stuff_in_file[i] = stuff_in_file[i].lstrip(change)

		with open(FILENAME, 'w') as f:
			f.writelines(stuff_in_file)

def main():
	global FILENAME
	
	choice = True
	while choice:
		print('Welcome to this Text File Manipulation python program made by KPT for making bulk changes in text files easier\n\n')
		FILENAME = input('What file are we working with here? (enter the name of the file with extention if it is in the same directory as this exe, or the entire path of the file with forward slashes):\n\n')
		
		try:
			f = open(FILENAME, 'r')
		except:
			print(f'Sorry, the file {FILENAME} does not exist or is not in the same directory of this file.')
			choice = int(input('\nPress 1 to continue and any other key to quit\n'))
			if choice == 1:
				choice = True
				continue
			else:
				choice = False
				break
		print('What do you want to do:')
		print('1: Add something to the beginning of each line in a text file')
		print('2: Remove something from the beginning of each line in a text file')
		print('3: Add something to the end of each line in a text file')
		print('4: Remove something from the end of each line in a text file')
		print('5: Replace some characters from the file with some other ones')
		print('6: Remove some characters from the file')
		print('7: Concatenate each line with a delimeter')
		
		selection = int(input())
		
		if selection == 1:
			change = input('what do you want to add ? \n')
			add.add_before_beginning_line(change)
			
		if selection == 2:
			change = input('what do you want to remove ? \n')
			remove.del_from_beginning_lines(change)
			
		if selection == 3:
			change = input('what do you want to add ? \n')
			add.add_after_end_line(change)
			
		if selection == 4:
			change = input('what do you want to remove ? \n')
			remove.del_from_end_lines(change)
		
		if selection == 5:
			what_to_change = input('what do you want to replace? \n')
			change = input('what do you want to replace it with? \n')
			modify.replace_in_each_line(what_to_change, change)

		if selection == 6:
			change = input('what do you want to remove? \n')
			modify.replace_in_each_line(change, '')	
			
		if selection == 7:
			delimiter = input('what do you want to delimate the lines with? \n')
			modify.replace_in_each_line('\n', delimiter)
			
		print('All Done Correctly! Enjoy!')
		choice = int(input('\nPress 1 to continue and any other key to quit\n'))
		if choice == 1:
			choice = True
		else: choice = False
		print(choice)
	print('Thank you for using this Program!')
main()