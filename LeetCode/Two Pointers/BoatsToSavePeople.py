# This problem is called 881. Boats to Save People
# You can access it here: https://leetcode.com/problems/boats-to-save-people/

# The program recieves an integer array named people where people[i] is the weight of the ith person.
# The program also recieves an integer limit. Each boat can carry a maximum weight of limit.
# However each boat can carry at most two people
# provided that the sum of the weights of those two people does not exceed limit.
# The program will return the minimum number of boats to carry every given person.
# For example if people =  [1,2] and if limit = 3
# Then the  output will be 1.
# Because the minimum number of boats to carry every given person is 1. 
# That one boat an carry the person with weight 1 and 2. Since the sum of the weights does not exceed limit.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Intially sort the list so that the greater weights can be toward the end of the list 
        # and the lesser valued weights can be at the beginning of the list 
        people.sort() 
        
        # Create two pointers so that pointer_one can point to the beginning of the list. 
        # pointer_two will point to the last item in the list
        number_of_boats = 0 
        pointer_one = 0 
        pointer_two = len(people) - 1 
        
        while pointer_one <= pointer_two: 
            remain = limit - people[pointer_two]
            pointer_two -= 1 
            number_of_boats += 1 
            if pointer_one <= pointer_two and remain >= people[pointer_one]:
                pointer_one +=1 
            else: 
                break
        return number_of_boats
                
            
              