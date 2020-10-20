#수직체크 , 대각선 체크를 하는 함
def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row]-current_col)==current_row-queen_row:
            return False
    return True

#current_candidate => 이전 행까지의 퀸 위치 정보를 담는 변수
def DFS(N,current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return
    # 해당 행의 모든 열을 검사함 ex) (1,0) (1,1) (1,2) (1,3) ,,,,의 경우
    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N,current_row+1,current_candidate,final_result)
            current_candidate.pop()

def solve_n_queens(N):
    final_result = []
    DFS(N,0,[],final_result)
    return final_result

print(solve_n_queens(4))