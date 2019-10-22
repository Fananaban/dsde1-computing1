repeat = 2
phrase = "one"

for i in range(int(repeat)):
    phrase = phrase + phrase
#print(str(phrase)*int(repeat))
# hint: you can add strings together 
# in order to concatenate them
print(phrase)