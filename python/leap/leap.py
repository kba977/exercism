def is_leap_year(year):
    ''' 判断是否为闰年, 是闰年的条件如下面两个
        1. 能被 400 整除
        2. 能被 4 整除, 但不能被 100 整除
    '''
    if year % 400 == 0 or (year % 4 ==0 and year % 100 != 0):
        return True
    return False
