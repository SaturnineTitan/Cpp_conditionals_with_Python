strings = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight"} # dictionary with values in question 
f = open("output.cpp", "w") # open the output file in write mode 
f.write('if (n > 9) {' + '\n\t' + 'printf("Greater than 9");' + '\n' + '}\n') # set up the first conditional check 
for item in strings.keys(): # write the rest of the conditionals with a loop 
	f.write('else if (n == ' + str(item) + ')' + ' {' + '\n\t' + 'printf("' + strings[item] + '");' + '\n' + '}' + '\n')
