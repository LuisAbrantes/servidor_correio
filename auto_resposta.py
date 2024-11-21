import smtplib
from email.mime.text import MIMEText
from aiosmtpd.controller import Controller

async def handle_mail(server, session, envelope):
    remetente = envelope.mail_from
    destinatarios = envelope.rcpt_tos
    
    resposta = MIMEText("""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <h2 style="color: #2c3e50;">Confirmação de Recebimento</h2>
            <p>Olá,</p>
            <p>Recebemos sua mensagem e retornaremos em breve.</p>
            <p>Esta é uma resposta automática.</p>
            <hr>
            <p style="color: #7f8c8d;">Por favor, não responda a este email.</p>
        </body>
    </html>
    """, "html")
    
    resposta["Subject"] = "Confirmação - Mensagem Recebida"
    resposta["From"] = destinatarios[0]
    resposta["To"] = remetente
    
    with smtplib.SMTP("localhost", 1025) as servidor:
        servidor.sendmail(destinatarios[0], remetente, resposta.as_string())
    
    return '250 Message accepted for delivery'

if __name__ == '__main__':
    controller = Controller(handle_mail, hostname='localhost', port=1025)
    controller.start()
    print("Servidor de auto-resposta ativo - Pressione Ctrl+C para encerrar")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        controller.stop()