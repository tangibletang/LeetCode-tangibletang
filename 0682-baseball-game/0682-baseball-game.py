class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_array = []
        total_score = 0 
        for op in operations:
            if op == "C":
                score_array.pop() #get rid of the last score
            elif op == "D":
                temp_sum = score_array[-1] * 2
                score_array.append(temp_sum)
            elif op == "+":
                new_sum = score_array[-1] + score_array[-2] #may need to create error condition 
                score_array.append(new_sum)
            else: #must be a positive/negative number
                score_array.append(int(op)) #add to the top of the stack
        print(score_array)
        #once score_array made, add all up
        for i in score_array: 
            total_score += i
        return total_score

            