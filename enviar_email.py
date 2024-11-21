import smtplib
from email.mime.text import MIMEText

# Configuração da mensagem de email
remetente = "seuemail@exemplo.com"
destinatario = "destinatario@exemplo.com"

# Corpo do email em HTML
html_content = """
<html>
    <body style="font-family: Arial, sans-serif;">
        <h2 style="color: #2c3e50;">Mensagem Importante</h2>
        <p>Prezado usuário,</p>
        <p>Este é um email com <span style="color: #e74c3c;">formatação especial</span> e conteúdo personalizado.</p>
        <hr>
        <ul>
            <li>Suporte técnico: support@exemplo.com</li>
            <li>Website: www.exemplo.com</li>
        </ul>
        <p style="font-style: italic;">Atenciosamente,<br>Equipe de Suporte</p>
    </body>
</html>
"""

mensagem = MIMEText(html_content, "html")
mensagem["Subject"] = "Notificação Importante - Sistema de Email"
mensagem["From"] = remetente
mensagem["To"] = destinatario

# Conectar ao servidor SMTP e enviar o email
with smtplib.SMTP("localhost", 1025) as servidor:
    servidor.sendmail(remetente, destinatario, mensagem.as_string())

print("Email enviado com sucesso!")
