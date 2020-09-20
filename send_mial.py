#!/usr/bin/env/python

# coding = utf-8

import smtplib

from datetime import datetime

from email.mime.text import MIMEText

from email.header import Header

from email.mime.multipart import MIMEMultipart


class Send_Email():

    def __init__(self):

        pass

    def send_email(self, **kwargs):

#创建一个带附件的实例

message = MIMEMultipart()

message['From'] = Header("自动化报告", 'utf-8')

message['To'] =  Header("测试", 'utf-8')

subject = 'SMTP 邮件发送测试'

message['Subject'] = Header(kwargs.get(subject), 'utf-8')

        path = 'D:\\XXX\\' + str(datetime.now().date().isoformat() + '_report.html')

        with open(path, 'wb') as fp:

            email_body = fp.read()

        msg = MIMEText(email_body, 'html', 'utf-8')

        try:

            smtpObj = smtplib.SMTP('')

            smtpObj.sendmail(kwargs.get(sender), kwargs.get(receivers), msg.as_string())

            print('邮件发送成功')

        except smtplib.SMTPException:

            print('Error：邮件发送失败')


if __name__ == "__main__":

  sender = '公邮邮箱@xx.com.cn'

  receivers = ['XXXX@qq.com.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

  EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

  EMAIL_USE_TLS = False

  EMAIL_HOST = "XX.XX.XX.XXX"

  EMAIL_PORT = 25

  EMAIL_HOST_USER = "PAB_zdhcspt@pingan.com.cn"

  sendmail = Send_Email(EMAIL_HOST_USER, receivers) 
