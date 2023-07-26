# dictionary with values in question 
strings = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
# open the output file in write mode 
f = open("output.cpp", "w")
 # set up the first conditional check 
f.write('if (n > 9) {' + '\n\t' + 'printf("Greater than 9");' + '\n' + '}\n')
# write the rest of the conditionals with a loop 
for item in strings.keys():
	f.write('else if (n == ' + str(item) + ')' + ' {' + '\n\t' + 'printf("' + strings[item] + '");' + '\n' + '}' + '\n')
