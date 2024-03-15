def solution(S):
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            for k in range(len(S[i])):
                if S[i][k] == S[j][k]:
                    return [i, j, k]
    return []

# Tests
print(solution(["abc", "bca", "dbe"]))  
print(solution(["zzzz", "ferz", "zdsr", "fgtd"]))  
print(solution(["gr", "sd", "rg"]))  
print(solution(["bdafg", "ceagi"])) 
