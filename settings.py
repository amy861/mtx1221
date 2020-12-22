#配置文件（一些公关的东西）
#变量=值的写法
import os

IP='http://121.42.15.146:9090/'
HEADERS={'X-Requested-With': 'XMLHttpRequest'}
ABS_PATH=os.path.abspath(__file__)
DIR_NAME=os.path.dirname(ABS_PATH)
JUMP_URL=None