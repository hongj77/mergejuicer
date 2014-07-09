import os
 
replacements = {'o': '0', 'l': '1', 'b': '8'}
 
for filename in os.listdir(os.getcwd()):
 
	if filename != 'mergejuicer.py':
 
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