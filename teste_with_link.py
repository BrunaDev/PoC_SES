import boto3
from botocore.exceptions import ClientError

def send_password_reset_email(user_email, reset_link):
    # Cria o cliente do SES
    ses_client = boto3.client('ses', region_name='sa-east-1')  # Substitua pela sua região

    # Configurações do e-mail
    sender_email = "seuemail@exemplo.com"   # E-mail verificado no SES
    subject = "Redefinição de senha - Sua Aplicação"

    # Corpo do e-mail em texto puro
    body_text = (
        "Você solicitou a redefinição de sua senha.\n\n"
        "Clique no link abaixo para redefinir sua senha:\n"
        f"{reset_link}\n\n"
        "Se você não solicitou esta alteração, ignore este e-mail."
    )

    # Corpo do e-mail em HTML (opcional)
    body_html = f"""
    <html>
    <head></head>
    <body>
      <h1>Redefinição de senha</h1>
      <p>Você solicitou a redefinição de sua senha. Clique no link abaixo para redefinir sua senha:</p>
      <a href='{reset_link}'>Redefinir senha</a>
      <p>Se você não solicitou esta alteração, ignore este e-mail.</p>
    </body>
    </html>
    """

    # Mensagem do e-mail
    email_message = {
        'Source': sender_email,
        'Destination': {
            'ToAddresses': [user_email],
        },
        'Message': {
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': body_html,
                    'Charset': 'UTF-8'
                }
            }
        }
    }

    # Tentativa de envio do e-mail
    try:
        response = ses_client.send_email(**email_message)
        print(f"E-mail de redefinição enviado com sucesso! ID da mensagem: {response['MessageId']}")
    except ClientError as e:
        print(f"Erro ao enviar o e-mail: {e.response['Error']['Message']}")

# Exemplo de uso da função
user_email = "usuario@exemplo.com"
reset_link = "https://github.com/BrunaDev/PoC_SES"
send_password_reset_email(user_email, reset_link)
