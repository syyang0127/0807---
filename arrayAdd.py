import numpy as np

arr1 = ([1,2,3,4])
arr2 = ([5,6,7,8])
twoDim = np.array([[1,2,3],[4,5,6],[7,8,9]])

A = np.array([1,2,3,4])
B = np.array([5,6,7,8])

result1 = A + B          # 1x4 짜리 배열의 각 자리끼리 더한 값이 저장 
result2 = arr1 + arr2    # 연결 연산자. 1x8의 리스트 배열이 됨.
result3 = A < 3          
result4 = B < 3

print(result1)
print(result2)
print(result3)
print(result4)
print(twoDim)
print(twoDim[0][0],twoDim[0][1],twoDim[0][2]) # 1 2 3 이 출력됨


"""
terminal output
<result1> [ 6  8 10 12]
<result2> [1, 2, 3, 4, 5, 6, 7, 8]
<result3> [ True  True False False]
<result4> [False False False False]
<result5>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""