###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def fizz_buzz(start, finish):
    """Replaces numbers that are divisible by 3 or 5, contain 3 or 5, or have both properties with 'fizz', 'buzz', or 'fizzbuzz' """

    lst = range(start, finish+1)
    for num in lst:
        if((num % 3 == 0) and (num % 5 == 0)): print("fizzbuzz")
        elif(("3" in str(num)) and ("5" in str(num))): print("fizzbuzz")
        elif((num % 3 == 0) and ("5" in str(num))): print("fizzbuzz")
        elif((num % 5 == 0) and ("3" in str(num))): print("fizzbuzz")
        elif(num % 3 == 0): print("fizz")
        elif("3" in str(num)): print("fizz")
        elif(num % 5 == 0): print("buzz")
        elif("5" in str(num)): print("buzz")
        else: print(num)


#fizz_buzz(5, 100)