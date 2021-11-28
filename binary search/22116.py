# 격자의 크기 N
N = int(input())

# 격자의 요소
graphs = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    number = list(map(int, input().split()))
    graphs.append(number)

global final_path
final_path = []

# 위에서 아래로 우측과 아래로 가는 알고리즘
def printAllPathsUtil(mat, i, j, path, pi):
     
    # Reached the bottom of the matrix
    # so we are left with only option to move right
    if (i == N - 1):
        for k in range(j, N):
            path[pi + k - j] = mat[i][k]
        
        current_path = []
        for l in range(pi + N - j):
            current_path.append(path[l])
            
        return current_path
 
    # Reached the right corner of the matrix
    # we are left with only the downward movement.
    if (j == N - 1):
     
        for k in range(i, N):
            path[pi + k - i] = mat[k][j]
        final_path = []
        for l in range(pi + N - i):
            final_path.append(path[l])
            print(path[l], end = " ")
        print()
        print(final_path)
        return
 
    # Add the current cell
    # to the path being generated
    path[pi] = mat[i][j]
 
    # Print all the paths
    # that are possible after moving down
    printAllPathsUtil(mat, i + 1, j, path, pi + 1)
 
    # Print all the paths
    # that are possible after moving right
    printAllPathsUtil(mat, i, j + 1, path, pi + 1)
 
    # Print all the paths
    # that are possible after moving diagonal
    # printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1);
 
# The main function that prints all paths
# from top left to bottom right
# in a matrix 'mat' of size mXn
def printAllPaths(mat):
    path = [0 for i in range(2*N)]
    printAllPathsUtil(mat, 0, 0, path, 0)

printAllPaths(graphs)
