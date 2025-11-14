

table showing the realtion betwen space and time for each pace:
pace   1 2 3 4 5 0 -5 -4 -3 -2 -1
space  1 1 1 1 1 0 -1 -1 -1 -1 -1
time   1 2 3 4 5 1  5  4  3  2  1


task:
generate a movement sequence(list of paces)

conditions:
Your spaceship can only gradually step up the pace as well as step down
 -1 <-> -2 <-> -3 <-> -4 <-> -5 <-> 0 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 
 you must start and end on 0
 you must start at 0 with pace 0 and end with pace 0(note both will take 1 time unit)
 the pace sequecne must equaly exactly p space units in at most t time units
 so for each pace you will take the from the table the space and time units
 -1 and 1 are endponits so you can only go back to 2 from 1 or -2 from -1
 if the p is negative than you must get to -p with negative paces similarly to positive paces
 you hav to think about this relations of many paces to reach the destination and time. 


input explanation:
N
p t

p - is the final position of the spaceship
t - maximum time allowed to reach that position

input:
3
2 25
5 39
-7 46

output:
0 5 5 0
5 4 3 4 5 0
0 -5 -4 -3 -2 -3 -4 -5 0
