import re, os, pprint 

# find all .py file
files = os.listdir()
py_regex = re.compile(r'^quiz.*.py$')
quizs = []
for f in files:
	mo = py_regex.search(f)	
	if mo:
		quizs.append(mo.group())

# TODO: add the __doc__ to the file 
'''
# generate doc_dict from docs.py
doc_file = open('docs.py', 'w')
doc_file.write('doc_dict = {}\n')
for quiz in quizs:
	doc_file.write('import %s\n'%(quiz[:-3]))
	doc_file.write('doc_dict["%s"] = %s.__doc__\n' % (quiz[:-3], quiz[:-3]))
doc_file.close()
	
# save to quizs.txt
import docs
quizs_file = open('quizs.txt', 'w')
quizs.sort() # sort
for quiz in quizs:
	quizs_file.write('%s\t-->\t%s\n' % (quiz, docs.doc_dict[quiz]))
quizs_file.close()
'''

# save in 'quizs.txt'
quizs.sort()
f = open('quizs.txt', 'w')
for quiz in quizs:
	f.write(quiz + '\n')
f.close()


print('Done.')

