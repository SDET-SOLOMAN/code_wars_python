# Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor. You have travelled a total of 3 + 6 = 9 floors of distance.

# Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.

# // simple examples
# [5,2,8] => 9
# [1,2,3] => 2
# [7,1,7,1] => 18

# // if two consecutive floors are the same,
# //distance travelled between them is 0
# [3,3] => 0
# Array will always contain at least 2 floors. Random tests will contain 2-20 elements in array, and floor values between 0 and 30.

def elevator_distance(a):
    
    dis = 0
    
    for ind, char in enumerate(a[1:], 1):
        if a[ind - 1] > char:
            dis += a[ind - 1] - char
        elif a[ind - 1] < char:
            dis += char - a[ind - 1]
        else:
            dis += 0
        print(dis)
    return dis

def elevator_distance(floors):
    return sum(abs(floors[i + 1] - floors[i]) for i in range(len(floors) - 1))