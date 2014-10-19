import random

cols = 3
rows = 3
matrix = []
for i in range(0, rows):
    row = []
    for j in range(0, cols):
        row.append(random.randint(1, 10))
    matrix.append(row)
print matrix

sum_two_elem = matrix[0][1] + matrix[0][2]
print 'sum of last two elements is: %d' % sum_two_elem

col_2 = []
for i in range(0, rows):
    col_2.append(matrix[i][1])
min_in_col = min(col_2)
print 'min of second col is: %d' % min_in_col

max_numb = max(max(row) for row in matrix)
print 'max of whole array is: %d' % max_numb

empty_index = True
for row in matrix:
    if 4 in row:
        empty_index = False
        print 'index of sub-array where 4 occured is:', matrix.index(row)

if empty_index:
    print "We have not 4 in matrix"
