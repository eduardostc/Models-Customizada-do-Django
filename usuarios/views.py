from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# # Create your views here.
# def envia_email(request):
#     send_mail('Assunto', 'Esse é o email que estou te enviando', 'eduardostc@hotmail.com', ['carlos.rodrigues@recife.pe.gov.br'])
#     return HttpResponse('olá')

from django.core.mail import EmailMultiAlternatives #o que faz enviar o email
from django.template.loader import render_to_string # conversão
from django.utils.html import strip_tags # remove tudo que parece tag html, e mostra apenas o conteudo de dentro
from django.conf import settings # de quem esse email será enviado

# Create your views here.
def envia_email(request):
    
    html_content = render_to_string('emails/cadastro_confirmado.html', {'nome': 'Eduardo'}) #converteu html para txt
    text_content = strip_tags(html_content) #remove as tags html

    email = EmailMultiAlternatives('Cadastro confirmado', text_content, settings.EMAIL_HOST_USER, ['carlos.rodrigues@recife.pe.gov.br'])# enviar o email de fato
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return HttpResponse('olá')
