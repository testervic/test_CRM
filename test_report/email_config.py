#coding:utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import time
import datetime
#from config.email_config import email_config

def send_email_report(email_info):

    if '' in (email_info['sender'], email_info['receiver'], email_info['smtpserver'], email_info['username'], email_info['password'], email_info['mail_title'], email_info['mail_body']):
        print '邮件发送失败，除附件外，各字段不可为空!'
        return False
    else:
        msgRoot = MIMEMultipart()

        # 邮件标题时间设置
        week_list = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
        date_str = str(datetime.datetime.now()).split('.')[0] + ' ' + week_list[time.localtime().tm_wday]

        msg = MIMEText(email_info['mail_body'], 'html', 'utf-8')
        msgRoot['Subject'] = Header(email_info['mail_title'] + date_str, 'utf-8')
        msgRoot.attach(msg)

        # 构造附件
        attachment_num = len(email_info['attachment'])
        if attachment_num != 0:
            for i in range(0, attachment_num):
                att = MIMEText(open(email_info['attachment'][i], 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename=' + email_info['attachment'][i]
                msgRoot.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(email_info['smtpserver'])
        smtp.login(email_info['username'], email_info['password'])
        smtp.sendmail(email_info['sender'], email_info['receiver'].split(';'), msgRoot.as_string())
        smtp.quit()

email_config = {
    #发件人
    "sender" : 'zhongwei@guxiansheng.cn',
    #收件人,多个收件人按;隔开
    "receiver" : 'liuxu@guxiansheng.cn',
    #邮件发送服务器
    "smtpserver" : 'smtp.ym.163.com',
    #发件人账号
    "username" : 'zhongwei@guxiansheng.cn',
    #发件人密码
    "password" : '469858846',
    #邮件标题
    "mail_title" : '自动化测试报告',
    #邮件内容
    "mail_body" : '测试一下邮件到达情况',
    #附件,list
    "attachment": ['HTMLReport.html']
}
email_config['receiver'] = 'zhongwei@guxiansheng.cn'
send_email_report(email_config)
