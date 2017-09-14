def is_isogram(string):
    
    lower_string = string.lower()

    for s in lower_string:
        if s.isalpha():
            if lower_string.count(s) > 1:
                return False
    return True
