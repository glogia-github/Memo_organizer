import os
import itertools
import re
import string


def replace_file_extension(filename, new_extension):  # file_name is str ; new_extension is str(e.g. '.txt')
    pattern_extension = re.compile('^\.[^.]+$')  # for . followed by anything
    if filename.endswith(new_extension) is False:  # and not [u == '.' for u in Name]
        if pattern_extension.match(filename) is True:
            for x in range(1, len(filename)):
                y = filename[len(filename) - 1]
                if y == '_' or len(filename) < 11:
                    break
                if y != '.':
                    filename = filename[0:len(filename) - 1]
                    continue
                if y == '.':
                    filename = filename[0:len(filename) - 1] + new_extension
                    filename = filename + new_extension
                    break
        else:
            filename = filename + new_extension
    return filename


def inverse_date(date):
    # input dd-mm-yyyy ; write date as yyyy-mm-dd
    l = []
    for k in date:
        l.append(k)
    l[0], l[1] = l[1], l[0]
    l[3], l[4] = l[4], l[3]
    l[6], l[7], l[8], l[9] = l[9], l[8], l[7], l[6]
    l.reverse()
    return ''.join(l)

'''
OLD , WORKS TO CERTAIN EXTENT
def format_memo_dates(dates):
		# returns formated list of dates
			# ?make sure every line has 8 charachters
			# ?make sure dates are one per line

		pattern1 = re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")  # dd-mm-yyyy
		# pattern2 = re.compile("^(0[1-9]|[12][0-9]|3[01])")
		with open(Memo_dates_path, 'r') as D:
			lines1 = D.readlines()
			most_recent = ''
			count = 0
			errors = 0
			for k in lines1:
				if len(k) > 11:
					print 'error element %s longer than 11' % k
					errors = errors + 1
					pass
				if pattern1.match(k):
					most_recent = k
					lines1[count] = str(most_recent[0:10])
					pass
				if True:
					lines1[count] = str(k[0:2]) + str(most_recent[2:10])
					pass
				else:
					errors = errors + 1
					pass
				count = count + 1
		print 'errors in memo dates = %s' % errors
		return lines1	
'''


def check_for_symbol(memo, sym_list):
    # check for forbidden symbols ( /, =, [, ], \, ", ', ?, :, ;, |) in text
    x = open(memo, 'r')
    lines = x.readlines()
    for j in sym_list:
        try:
            if j in lines[0]:
                return False
            else:
                return True
        except IndexError:
            return False


def fix_memo(memo2, sym_list):
    # removes forbidden symbols from first line
    # returns memo2 as list
    x = open(memo2, 'r+')
    lines = x.readlines()
    for j in sym_list:
        if j in lines:
            lines.replace(j, '_NA_')
    print lines
    return lines


'''Listdatesdoc = raw_input('list dates file name(without extension):')
nameofdir = raw_input('directory of memos file name(without extension):'''

forbidden_symbol = ['/', '=', '[', ']', '\ ', '"', "'", '?', ':', ';', '|']
# symbols that don't cause the error ':' '-' '_' non ASCII e.g. e(grave)
#

# memo dates: find directory and format
Memo_dates_path = os.path.join(os.path.expanduser('~'), 'Documents', '013_Python', 'Text_and_binary_files',
                               'list dates samsung a5 26-08-17 part 2')
Memo_dates_file = open(Memo_dates_path, 'r')
pattern1 = re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")  # dd-mm-yyyy
	with Memo_dates_file as D:
		lines1 = D.readlines()
		template=''
		current=''
		count_dates=0
		error_dates=0
		for i in lines1:
			if pattern1.match(i):
				template = i
				count_dates+=1
				continue
			else:
				current= i
				pass
			#remove spaces and extend string
			current.replace(" ","-")
			if len(current)>11:
				error_log_dates = open(Error log.txt, a)
				error_log_dates.write("Error (length) at date:%s " % count_dates + " ; " + "Date=%s" % i + '\n' )
				error_log_dates.close()
				error_dates+=1
				count_dates+=1
				continue
			while len(current)<10
				current = current + "-"
			#for dd
			try:
				if current[0:1] == "--"
					current[0:1] == template[0:1]
			#for mm
			try:
				if current[3:4] == "--"
					current[3:4] == template[3:4]
			#for yyyy
			try:
				if current[6:10] == "----"
					current[6:10] == template[6:10]
			if pattern1.match(current):
				lines1[count_dates]=current
			else:
				error_log_dates = open(Error log.txt, a)
				error_log_dates.write("Error (unknown) at date:%s" % count_dates + " ; " + "Date=%s" % i + '\n' )
				error_log_dates.close()
				error_dates+=1
			count_dates+=1
Memo_dates_file.close()
Memo_dates = lines1


# memos: find directory and sort
Memo_path = os.path.join(os.path.expanduser('~'), 'Documents', '013_Python', 'Text_and_binary_files',
                         '26-08-17_part2')
Memo_dir = os.listdir(Memo_path)
os.chdir(Memo_path)
Memos = filter(os.path.isfile, Memo_dir)  # eliminates non text files
Memos.sort(key=lambda x: os.path.getmtime(x))  # sort memo by modification date
Memos.reverse()


# check memo, fix memo?, couple memo to memo_dates
Memo_dictionary = {}
error_memos = 0
count_memos = 0
for i, j in itertools.izip(Memos, Memo_dates):  # will stop at end of shorter list. use .izip.longest() otherwise
	count_memos+=1 #just for error checking 
    if check_for_symbol(i, forbidden_symbol) is True:
		Memo_dictionary[i] = j
        pass
    else:
        with open('Error log.txt', 'a') as error_log: 
            error_log.write( "Error at Memo:%s" % count_memos + '\n' 
			+ '  Path = ' + os.path.join(Memo_path, i) + '\n' 
			+ '  Filename = ' + os.path.basename(i) + '\n' 
			+ '  Date of memo = %s' % j + '\n')
            error_log.close()
            error_memos+=1
        print i
        #fix_memo(i, forbidden_symbol)
		Memo_dictionary["error"] = j
        pass
	
# rename memo
for k,l in Memo_dictionary:
	if k == "error":
		continue
	if 'z' in k[0]:
		Name = str(k)
		Name = Name[1:len(Name)]
		Name = replace_file_extension(Name, '.txt')
		pass
	else:
		M = open(k, 'r')
		Name = M.readline()
		Name = Name.strip('\n')
		M.close()
		if len(Name) > 35:
			Name = Name[:35]
	Name = inverse_date(l) + '_' + Name
	os.rename(os.path.join(Memo_path, k), Name)

print 'Total Memos = %s' % count_memos , len(Memos)
print 'Total Dates = %s' % len(memo_dates)
print 'Memos Organized = %s' % len(Memo_dictionary)
print 'errors in dates = %s' % error_dates
print 'errors in memos = %s' % error_memos
print 'end'

print Memo_dictionary
print Memo_dates
print Memos

'''error caused when there is a / or other non permitted symbol in the first line or the text doc'''
'''make sure memo will run, i.e. fix error where some files will not rename properly
        I think this is because of forbidden symbols( /, =, [, ], \, ", ', ?, :, ;, |) in the first line of
        text where i get the new filename make copy of originals automatically '''
