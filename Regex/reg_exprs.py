	
# . 	Any character (except newline character) 	"he..o" 	
# ^ 	Starts with 	"^hello" 	
# $ 	Ends with 	"planet$" 	
# * 	Zero or more occurrences 	"he.*o" 	
# + 	One or more occurrences 	"he.+o" 	
# ? 	Zero or one occurrences 	"he.?o" 	
# {} 	Exactly the specified number of occurrences 	"he.{2}o" 	
# | 	Either or 	"falls|stays"

# \d  contains digits (numbers from 0-9) 	    "\d" 	
# \D  NOT contain digits 	                    "\D" 	
# \s  contains a white space character 	    "\s" 	
# \S  NOT contain a white space character 	"\S" 	
# \w  contains any word characters        	"\w" 	
# \W  DOES NOT contain any word characters    "\W"

# [arn] 	    (a, r, or n) is present 	
# [a-n] 	    alphabetically between a and n 	
# [^arn] 	    any character EXCEPT a, r, and n 	
# [0123] 	    (0, 1, 2, or 3) are present 	
# [0-9] 	    digit between 0 and 9 	
# [0-5][0-9] 	two-digit numbers from 00 and 59 	
# [a-zA-Z] 	between a and z, lower case OR upper case