from threading import Thread

from django.core.mail import send_mail
from django.template.loader import render_to_string


def enviar_email_alteracao_situacao(usuario):
    if usuario.estado_processo == '2':
        message_txt = render_to_string(
            'emails/documentacao_recebida.txt', {'usuario': usuario})
        message_html = render_to_string(
            'emails/documentacao_recebida.html', {'usuario': usuario})
        subject = 'Sistema Nacional de Cultura - Documentação Recebida'
    elif usuario.estado_processo == '3':
        message_txt = render_to_string(
            'emails/aviso_pendencia.txt', {'usuario': usuario})
        message_html = render_to_string(
            'emails/aviso_pendencia.html', {'usuario': usuario})
        subject = 'Sistema Nacional de Cultura - Aviso de Pendência'
    elif usuario.estado_processo == '6':
        message_txt = render_to_string(
            'emails/acordo_publicado.txt', {'usuario': usuario})
        message_html = render_to_string(
            'emails/acordo_publicado.html', {'usuario': usuario})
        subject = 'Sistema Nacional de Cultura - Acordo Publicado'
    else:
        return

    Thread(target=send_mail, args=(
        subject,
        message_txt,
        'naoresponda@cultura.gov.br',
        [usuario.user.email],),
        kwargs = {'fail_silently': 'False', 'html_message': message_html}
    ).start()