#Python 3
'''
Function Arguments :
		@param  :m (boolean matrix of size n*n), n(no of rows and cols )
		@return : Integer
'''
def getId(m,n):
    stack = [i for i in range(n)] # assume all the indexes can be celebrities.

    while(len(stack) > 1): # while more than one person is left in the stack.

        # get two persons from the stack.
        person_A = stack.pop()
        person_B = stack.pop()

        # if A knows B and B knows A.. Both can't be celebs.
        if (m[person_A][person_B] == 1 and m[person_B][person_A] == 1) :
            continue

        # if A knows B .. A can't be celeb
        elif m[person_A][person_B] == 1:
            # discard A and put B again in stack.
            stack.append(person_B)

        # if B knows A .. B can't be celeb
        elif m[person_B][person_A] == 1:
            # discard A and put B again in stack.
            stack.append(person_A)

        # 4th case is not possible as only one celebrity is there
    if len(stack) == 0:
        # no celebrity is there
        return -1
    else:
        possible_celeb = stack.pop()
        # we have to verify if the given element in actually a celeb
        for i in range(n):
            if i != possible_celeb and (m[possible_celeb][i] or m[i][possible_celeb] == 0): # if celeb knows someone or other doesn't know celeb
                return -1  # return -1 as no celeb is there

        return possible_celeb # we got our celeb, as this one doesnot know anyone else
