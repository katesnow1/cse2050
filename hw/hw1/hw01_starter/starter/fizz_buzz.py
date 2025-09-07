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
# checks for divisibility by 15 first, then divisibility by 3 second, then by 5 third
# and if none applies, it just prints out the number
    lst = range(start, finish+1)
    for x in lst:
        if((x % 3 == 0) and (x % 5 == 0)):
            print("fizzbuzz")
        elif(x % 3 == 0):
            print("fizz")
        elif(x % 5 == 0):
            print("buzz")
        else:
            print(x)


fizz_buzz(1, 15)