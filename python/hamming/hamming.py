def distance(seq1, seq2):
    L = len(seq1)
    if L != len(seq2):
        raise ValueError
    if L == 0:
        return 0
    dist = sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
    return dist
