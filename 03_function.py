
def check_symbols(restricticted_symbols, s):
    for symb in restricticted_symbols:
        if symb in s:
            return True
        return False


username ='dfde434343$#'
email ='wewe@wew.ru'

if check_symbols(['#','$#','@'],username):
    print('username has restricticted symbols') #True, because username consist of $# symbols
if check_symbols(restricticted_symbols =['#', '$#', '%'],s= email):
    print('email has restricticted symbols')  #False, because email does not contain '#', '$#', '%' symbols




# if '#' in username:
#     print('username has restricticted symbols')
#
# if '$#' in username:
#     print('username has retricticted symbols')
# if '@' in username:
#     print('username has retricticted symbols')
