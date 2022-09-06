import yagmail
email_to = ["867329009@qq.com"]
email_title = "测试报告"
email_content = "测试报告在附件中"
email_attachments = ['./reports/DiJiarp.html']

with yagmail.SMTP(user = "953242620@qq.com", password = "yesrfysafhywbffe", host = "smtp.qq.com") as yag:
    yag.send(email_to, email_title, email_content, email_attachments)