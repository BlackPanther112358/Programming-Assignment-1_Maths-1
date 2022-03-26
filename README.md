# Programming-Assignment-1_Maths-1
Programming assignment - 1 for Maths 1 (Linear Algebra)

The following code accepts 4-tuples which are a subset of (Z/2Z)^4 and checks whether they form a subspace or not.

INPUT FORMAT:
In first line, enter the number of 4-tuples to be entered, or the size of the subset
Then, individually enter each tuple as space separated string of integers (0 or 1) in one line, for each 4-tuple in the subset

Algorithm:
1) The code checks whether the result of addition of every vector is already present in the subset.
2) Then it checks that the vector obtained on multiplying each vector by 0 or 1 is present or not.
If both above conditions are fulfilled, True is outputted, else the code outputs False
