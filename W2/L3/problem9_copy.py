#L3 PROBLEM 9


lo, hi, status  = 0, 100, True
mid = (hi + lo)/2
print 'Please think of a number between 0 and 100!'
while status == True:
    print ("Is your number " + str(mid) + "?")
    guess_number = raw_input( "Enter 'h' to indicate the guess is    too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess_number == 'h':
        hi = mid
        mid =(hi + lo)/2
    elif guess_number == 'l':
        lo = mid
        mid =(hi + lo)/2
    elif guess_number == 'c':
        print ("Game over. Your secret number was:" + str(mid))
        status = False
    else:
        print ("Sorry, I did not understand your input.")
