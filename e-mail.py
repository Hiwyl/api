# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random

sim=random.sample(list(range(1,101)),6)
sim=list(map(lambda x:str(x),sim))
sim=' '.join(sim)
# print(sim)
# SMTP协议


mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "576676128@qq.com"  # 用户名
mail_pass = "ofzlynxjaocgbbci"  # 口令
shoujian=input('请输入收件人：')
csr=input('请输入抄送人：')
receivers=csr.split(' ')
receivers=receivers+[shoujian]

# receivers = ['598585055@qq.com','3366987708@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...，如果你收到，祝你开心一万年,您的验证码为%s'%sim, 'plain', 'utf-8')
message['From'] = Header("帅帅的彭老师", 'utf-8')
message['To'] = Header("对面的帅哥", 'utf-8')

subject = '【Python SMTP 邮件测试】'
message['Subject'] = Header(subject, 'utf-8')
# 下面为发送代码段
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(mail_user, receivers, message.as_string())
    print("邮件发送成功")
except:
    print('邮件发送失败')

sim_1=input('请输入您收到的验证码：')
if sim==sim_1:
    print('恭喜您输入的正确')