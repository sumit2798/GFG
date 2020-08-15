#Python 3

'''
	Function to return the smallest window in the string s
	having all characters of the text p.
	
	Function Arguments: s and p (given strings)
	Return Type: string or -1.

	Contributed By: Nagendra Jha
'''
def smallestWindow(s,p):
	if(len(p)>len(s)):
		return -1
	shash=[0 for i in range(26)]
	phash=[0 for i in range(26)]

	for char in p:
		phash[ord(char)-ord('a')]+=1

	counter=0
	begin=0
	startindex=-1
	length=0
	minlength=1e10

	for i in range(len(s)):
		shash[ord(s[i])-ord('a')]+=1

		if(phash[ord(s[i])-ord('a')] !=0 and shash[ord(s[i])-ord('a')]<=phash[ord(s[i])-ord('a')]):
			counter+=1

		if(counter==len(p)):
			while(shash[ord(s[begin])-ord('a')]>phash[ord(s[begin])-ord('a')] or phash[ord(s[begin])-ord('a')]==0):
				if(shash[ord(s[begin])-ord('a')]>phash[ord(s[begin])-ord('a')]):
					shash[ord(s[begin])-ord('a')]-=1
					begin+=1
			length=i-begin+1

			if(length<minlength):
				startindex=begin
				minlength=length

	if(startindex==-1):
		return "-1"
	else:
		return s[startindex:startindex+minlength]