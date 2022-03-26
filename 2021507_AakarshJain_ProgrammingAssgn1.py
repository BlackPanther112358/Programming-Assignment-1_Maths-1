#Declaring global variables
vectors = []    #List to store the tuples for comparing

#Declaring a class tuples (tuple is already a data structure in python, hence tuples) 
class tuples:
    def __init__(self, tup:list):                      #Initialising the class
        self.val = tuple(tup)
    def __add__(self, other):                           #Overloading '+' operator to perform addition on 2 tuples
        ans = []
        for itr in range(len(self.val)):                        #Iterating every element in the tuple
            ans.append(self.val[itr]^other.val[itr])            #As 1 + 1 = 0, we can use XOR operator to get the sum.
        return tuples(ans)
    def __mul__(self, other):                           #Overloading '*' operator to perform scalar mutliplication
        ans = []
        for itr in range(len(self.val)):                        #Iterating every element in the tuple
            ans.append(self.val[itr]*other)
        return tuples(ans)
    def __eq__(self, other):                            #Overloading the '==' operator to check for equality
        if len(self.val) != len(other.val):                     #To check if the tuples have same length
            return False
        for itr in range(len(self.val)):                        #To check if every element of tuple is same
            if self.val[itr] != other.val[itr]:                 #If element is not same, return False
                return False    
        return True                                             #Finally, return True
    def output(self):                                   #Prints the tuple, for debugging, not required otherwise 
        print(self.val)

#Defining all the functions
def input_length()->int:                                    #Function for taking input for the numbers of tuple
    try_cnt = 0
    while try_cnt < 3:                                          #Allow users 3 wrong attempts before terminating the program
        try_cnt += 1
        try:
            num = int(input('Please enter the number of tuples: ').strip())
        except Exception:
            print('Pleas enter an integer value.')
            continue
        if num > 0:                                             #Check if the entered input is positive
            return num
        print('Please enter a positive integer.')
    print('Program terminated due to multiple invalid inputs.')
    return False                                                #If correct input is not entered after 3 tries, return False to terminate the program

def input_tuple(sno:int)->tuples:                        #Function to take input of the tuple.
    try_cnt = 0
    while try_cnt < 3:                                          #Allow users 3 wrong attempts before terminating the program
        try_cnt += 1
        try:
            line = list(map(int, input(f'Please enter the space separated values for tuple no. {sno}: ').split()))
        except Exception:
            print('Please provide input in proper format')
            continue
        if len(line) == 4:                                 #Checks if the length of tuple is equal to required length
            nums = [0, 1]
            check = True
            for num in line:
                if num not in nums:                             #Checks if the input integers are 0 or 1
                    check = False
                    break
            if check:
                return tuples(line)
            else:
                print('The input can contain only 0\'s and 1\'s')
        else:
            print('Please enter exactly 4 space - seperated integers in a single line.')
    print('Program terminated due to multiple incorrect inputs.')
    return False                                                #If correct input is not entered after 3 tries, return False to terminate the program

def check_closure_over_addition()->bool:                    #Function to check closure over addition of tuples
    num = len(vectors)                                          #Find the number of vectors to check
    for i in range(num):                                        #Iterate i from 0 to 3, to check i'th vector
        for j in range(i + 1, num):                             #Iterate j from i + 1 to 3, to check if sum of i'th and j'th vector is present
            tup = vectors[i] + vectors[j]
            if tup not in vectors:                              #If the sum of vectors is not present, return False
                return False
    return True                                                 #Finally, return True

def check_closure_over_scalar_multiplication()->bool:       #Function to check closure over scalar multiplication
    #NOTE: As we are only checking for scalar multiplication by 0 and 1, only checking if null vector is present would have sufficed.
    num = len(vectors)                                          #Find the number of vectors to check
    for i in range(num):                                        #Iterate i from 0 to 3, to obtain the i'th vector
        tup = vectors[i]*0
        if tup not in vectors:                                  #If not closed over multiplication by 0, return False
            return False
        tup = vectors[i]*1
        if tup not in vectors:                                  #If not closed over multiplication by 1, return False
            return False
    return True

def main():                                                 #Main function to run the required code.
    # NOTE : We need not check for existence of additive identity as scalar multiplication by 0 also achieves the same.
    global vectors                                              #Use the global variable vectors to store the ones inputted by the user
    print('Please first enter the number of tuples to be entered. Then, individually input each tuple as space seperated integers')
    print()
    length = input_length()                                     #Input the length of each vector
    if length is False:
        return
    for i in range(length):                                         #Loop to take input for each tuple
        tup = input_tuple(i + 1)                                    #Take input of the vector
        if tup is False:
            return
        vectors.append(tup)                                     #Add vector to the list vectors
    ans = True                                                  #Initialise the ans variable to True, make it False, if answer is False
    if check_closure_over_addition() is False:                  #Check if it is closed over addition
        print('The given vectors are not closed over addition')
        ans = False
    if check_closure_over_scalar_multiplication() is False:     #Check if it is closed over scalar multiplication
        print('The given vectors are not closed over scalar multiplication')
        ans = False
    if ans:                                                     #If ans is still True, It is a subspace
        print('The vectors form a subspace.')
    print(ans)                                                  #True/False depending on whether it is a subspace or not
    return

#Driver Code
if __name__ == '__main__':                                  #Check if this file is being run directly, and not being imported
    print('-'*100)
    main()                                                      #Call the main function to run the program
    print('-'*100)
else:
    raise Exception('Please run the file directly')