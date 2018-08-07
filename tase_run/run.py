import unittest
from  BSTestRunner import BSTestRunner
import time,logging
import sys
#path='D:\\AutoTest\\govlan_test\\'
#sys.path.append(path)

test_dir='../test_case'
report_dir='../reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,
                        title='Govlan Test Report',
                        description='Govlan Android App Test Report')
    logging.info('开始执行测试...')
    runner.run(discover)