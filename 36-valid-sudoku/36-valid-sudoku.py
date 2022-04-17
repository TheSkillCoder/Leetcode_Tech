class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited_arr = set()
        
        for i in range(9):
            for j in range(9):
                curr_val, previous_length = board[i][j], len(visited_arr)
                if curr_val == ".": 
                    continue
                visited_arr.update([(curr_val, i, "row"), (curr_val, j, "col"), (curr_val, i//3,j//3)])
                if (previous_length + 3) != len(visited_arr):
                    return False
                
        return True