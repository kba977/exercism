def to_rna(string):
    map_dic = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    rna = ''

    for letter in string:
        if letter not in map_dic:
            return ''
        else:
            rna += map_dic[letter]
    return rna

    