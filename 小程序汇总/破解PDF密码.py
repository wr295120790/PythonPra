import PyPDF2

secretcode = 'DARU'
codeNotFound = True
for i1 in range(1, 27):
    if codeNotFound:
        for i2 in range(1, 27):
            if codeNotFound:
                for i3 in range(1, 27):
                    if codeNotFound:
                        for i4 in range(1, 27):
                            if codeNotFound:
                                code = chr(i1+64)+chr(i2+64)+chr(i3+64)+chr(i4+64)
                                if code == secretcode:
                                    print('\n密码是=', code)
                                    codeNotFound = False
                                    break
                                else:
                                    print(code, end=' ')
