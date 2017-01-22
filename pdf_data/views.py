from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage,get_connection
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django import forms
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from reportlab.pdfgen import canvas
import pdfkit
from django.core.mail.backends.smtp import EmailBackend


# def pdf_gen(request):
# 	buffer=StringIO()
# 	p=canvas.Canvas(buffer)
# 	p.drawString(100,100,"HELLOWORLD")
# 	p.showPage()
# 	p.save() 
# 	pdf=buffer.getvalue()
# 	buffer.close() 
# 	return pdf
@csrf_exempt
def send_mail_with_attach(request):
	if request.method=="POST":
		email=str(request.POST.get('email'))
		backend = EmailBackend(host='smtp.gmail.com', port=587, username='email', 
                       password='password', use_tls=True, fail_silently=True)
		EmailMsg=EmailMessage("AAVARTAN'17","Team Technocracy",'no-reply@gmail.com',[email],connection=backend)
		# pdf = pdfkit.from_url('http://127.0.0.1:8000/test1/',False)
		value= str(request.POST.get('yesno'))
		if value=="yes":
			file=request.FILES['file']
			EmailMsg.attach(file.name,file.read() ,file.content_type)
		EmailMsg.send()
		return HttpResponse("Your email has been sent")
	else:
		return render(request,'email.html')

def test(request):
	user_id=str("Arpit jain")
	return render(request,'test.html',{'user':user_id})