import os.path
if  os.path.isfile('y.txt'):
    print('檔案9存在')
    file = open('y.txt','w')
    file.write('i am kay')
    file.close()
else:
    print('檔案no存在')
    file = open('y.txt','w')
    file.write('no')
    file.close()
    


















