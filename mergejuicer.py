import os

exclude = ['mergejuicer.py', 'README.md', '.git']
juiceTypes = ['brutal', 'distracting', 'annoying']

def brutal (): 
	replacements = {'o': '0', 'l': '1', 'b': '8'}

	for filename in os.listdir(os.getcwd()):
		if filename not in exclude:
			infile = open(filename, 'r')
			outfile = open('temp', 'w+')
	 
			for line in infile:
				for key, value in replacements.iteritems():
					line = line.replace(key, value)
				outfile.write(line)
			infile.close()
			outfile.close()
	 
			os.remove(filename)
			os.rename('temp', filename)
			print '*', filename, ' is juiced'


def distract():
	replacements = {'9':'6', '--': '-'}

	for filename in os.listdir(os.getcwd()):
		if filename not in exclude:
			infile = open(filename, 'r')
			outfile = open('temp', 'w+')

			count = 0;
			for line in infile:		
				for key, value in replacements.iteritems():
					if count % 2 == 0:
						line = line.replace(key, value)
				count += 1
				outfile.write(line)

			infile.close()
			outfile.close()

			os.remove(filename)
			os.rename('temp', filename)
			print '*', filename, ' is juiced'


print "How would you like to juice?"

for i, val in enumerate(juiceTypes):
	print "press ", i+1, "for ",val.upper()

answer = raw_input('>>>')

if int(answer) == 1:
	brutal()
elif int(answer) == 2:
	distract()
# elif int(answer) == 3:
# 	annoying()



