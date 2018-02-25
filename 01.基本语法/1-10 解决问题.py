# 解决问题 
# 备份重要文件

# 第一版
import os
import time

source=['/Users/swa/notes']

target_dir=['/Users/swa/backup']

target=target_dir+os.sep+\
    time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command='zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed')


# 第二版

import os
import time

source=['Users/swa/notes']

target_dir='/Users/swa/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today=target_dir+os.sep+time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')

target=today+os.sep+now+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successully created directory',today)

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed')


# 第四版
import os
import time

source=['/Users/swa/notes']

target_dir='/Users/swa/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today=target_dir+os.sep+time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')

comment=input('Enter a comment-->')

if len(comment)==0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+\
    comment.replace(' ','_')+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successully created directory',today)

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup Failed')
