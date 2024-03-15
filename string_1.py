def solution(S):
    # Iterate through the strings that we have in the array
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            # Check the position by iterating
            for k in range(len(S[i])):
                #See if the current position is the same as the ind letter
                if S[i][k] == S[j][k]:
                 
                    return [i, j, k]
    # return empty array if no similar letter is found
    return []



# Tests
print(solution(["abc", "bca", "dbe"]))  
print(solution(["zzzz", "ferz", "zdsr", "fgtd"]))  
print(solution(["gr", "sd", "rg"]))  
print(solution(["bdafg", "ceagi"])) 
