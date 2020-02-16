if word_a[i] == word_b[j]:
    # the leters match
    cell[i][j] = cell[i-1][j-1] + 1
else:
    # the letters do not match
    cell[i][j] = max(cell[1-i][j], cell[i][j-1])