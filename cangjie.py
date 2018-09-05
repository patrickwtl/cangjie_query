#coding=utf-8

import json,sys
from datetime import datetime
from workflow import Workflow, web

reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

BASE_URL = 'http://input.foruto.com/cjdict/Images/CJZD_JPG/'

#TODO: 后持支持功能:
#1. 简体字仓颉码查询
#2. 直接显示码在后选结果上
def main(wf):
    query = wf.args[0]
    
    try:        
        if (len(query) == 1):
            big5 = query.decode("utf-8").encode("big5").encode("hex")
            imageUrl = BASE_URL + big5.upper() + '.JPG'
            wf.add_item(title='找到拆码结果:' + big5, subtitle='点击查看详细结果', quicklookurl=imageUrl)
        else:
            wf.add_item(title='无结果', subtitle='只支持单字查询')
    except UnicodeEncodeError:
        wf.add_item(title='无结果', subtitle='没找到匹配Big-5码')
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))