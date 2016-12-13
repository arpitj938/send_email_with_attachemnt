from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from reportlab.pdfgen import canvas

def pdf_gen(request):
	buffer=StringIO()
	p=canvas.Canvas(buffer)
	p.drawString(100,100,"HELLOWORLD")
	p.showPage()
	p.save() 
	pdf=buffer.getvalue()
	buffer.close() 
	return pdf

def send_mail_with_attach(request):
	EmailMsg=EmailMessage("YourSubject","YourEmailBodyCopy",'email@email.com',["arpitj938@gmail.com"],headers={'Reply-To':'arpitj938@gmail.com'})
	pdf=pdf_gen(request)
	EmailMsg.attach('yourChoosenFileName.pdf',pdf,'application/pdf')
	EmailMsg.send()
	return HttpResponse("Ok")
