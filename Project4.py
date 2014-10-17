def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
returns a dictionary of dictionaries, whose entries are indexed by pairs of characters
in alphabet plus '_'. 
Given two characters row_char and col_char, we can access the matrix entry corresponding 
to this pair of characters via scoring_matrix[row_char][col_char]
The score for any entry indexed by one or more dashes is dash_score.
The score for the remaining diagonal entries is diag_score. 
The score for remaining off-diagonal entries is off_diag_score.
Include an entry for two dashes, which will never be used. 
    """
    score_matrix = {}
    for i in alphabet:
        i_dict = {}
        for j in alphabet:
            if i == j != '-':
                i_dict[j] = diag_score
            elif i == j == '-':
                i_dict[j] = 'null'
            elif i == '-' or j == '-':
                i_dict[j] = dash_score
            else:
                i_dict[j] = off_diag_score
        score_matrix[i] = i_dict
    return score_matrix


matric = build_scoring_matrix('ATGC-', 4, 2, -2)
print matric

print matric['G']['A']

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    If global_flag is True, use ComputeGlobalAlignmentScores. If global_flag is False, do something else.
    Returns: the alignment_matrix for seq_x and seq_y.
    """
    def ComputeGlobalAlignmentScores(seq_x, seq_y, scoring_matrix):
        """
        Returns dynamic programming table S
        """
        m = len(seq_x)
        n = len(seq_y)
        alignment_matrix = {{}}
        alignment_matrix [0][0] = 0
            for i in range(m):
            alignment_matrix = alignment_matrix[i][0]
            for j i range(n):
            alignment_matrix = alignment_matrix[0][j]
            for i in range(m):
            for j in range(n):

    if global_flag == True:
        return ComputeGlobalAlignmentScores(seq_x, seq_y, scoring_matrix))

    else:
        return somethingelse
                         
"""
def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
            

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):

"""
