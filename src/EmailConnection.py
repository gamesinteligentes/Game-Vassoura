'''
Created on Jul 10, 2013

@author: fabiofilho
'''



import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate

from email import Encoders

# Procedimento para enviar o e-mail

class Email(object):
    
    def __init__(self):
        pass

    def send (self,de, para, assunto, mensagem, arquivos=[], servidor='smtp.gmail.com'):
    
       assert type(para) == list
    
       assert type(arquivos) == list
    
       msg = MIMEMultipart()
    
       msg['From'] = de
       msg['To'] = COMMASPACE.join(para)
       msg['Date'] = formatdate(localtime=True)
    
       msg['Subject'] = assunto
    
    
       msg.attach(MIMEText(mensagem))
    
       for f in arquivos:
          parte = MIMEBase('application', 'octet-stream')
          parte.set_payload(open(f, 'rb').read())
          Encoders.encode_base64(parte)
          parte.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    
          msg.attach(parte)
    
       smtp = smtplib.SMTP(servidor, 587)
       smtp.ehlo()
       smtp.starttls()
       smtp.ehlo()
    
       smtp.login('binhor006@gmail.com', '2b4i6n4h6o')
    
       smtp.sendmail(de, para, msg.as_string())
    
    
       smtp.close()



