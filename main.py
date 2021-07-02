# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import telnetlib
import smtplib
import dns.resolver
import  datetime
import  os


def telnet (ip,port):

    message = ''
    try:
        tn = telnetlib.Telnet(ip,port,100)
    except Exception as e:
        message = 'Error'
        print('Telnet Failed')
        print(e)
    return message


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dateStr = datetime.date.strftime(datetime.datetime.now(),'%Y%m%d%I%M%S')
    error_message = ''
    gmail_user = 'metamia6@gmail.com'
    gmail_password = 'Jonathan812'
    sent_from = gmail_user
    to = ['it_ops@guosen.com.hk']
    subject = 'Tencent SMS Network Check'
    body = 'SMS IP Unavailable: '
    port = 28
    list = []
    path = "C:\\Log\\"
    result = dns.resolver.resolve('smtp.easeye.com.cn')
    for ipval in result:
        if telnet(str(ipval),port) == 'Error':
            list.append(ipval)
    if list:
        if not os.path.exists(path):
            os.makedirs(path)
        f = "Log_"+dateStr+"_" + ".txt"
        with open(os.path.join(path, f), "wb") as file:
            for i in list:
                #file.write("Error".encode() + "\n")
                file.write(str(i).encode())

#             body = body + str(ipval)
#             email_text = """\
# From: %s
# To: %s
# Subject: %s
#
# %s
# """ % (sent_from, ", ".join(to), subject, body)
#             print(email_text)
#             try:
#                 server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#                 server.ehlo()
#                 server.login(gmail_user, gmail_password)
#                 server.sendmail(sent_from, to, email_text)
#                 server.close()
#                 body = 'SMS IP Unavailable: '
#             except Exception as e:
#                 print(e)
#                 print('Send Email Failed')

