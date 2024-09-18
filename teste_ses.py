import boto3
from botocore.exceptions import ClientError

def send_email():
    # Cria o cliente do SES
    ses_client = boto3.client('ses', region_name='sa-east-1')  # Substitua pela sua região

    # Configurações do e-mail
    sender_email = "bruna.magalhaes@nouvenn.com"   # E-mail verificado no SES
    recipient_email = "dev.bruna.magalhaes@gmail.com"  # E-mail do destinatário
    subject = "Teste de envio de email pelo Amazon SES"
    body_text = "Este é um e-mail de teste enviado usando Amazon SES com o Python boto3."

    # Mensagem
    email_message = {
        'Source': sender_email,
        'Destination': {
            'ToAddresses': [recipient_email],
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
                # Se quiser enviar HTML, descomente abaixo e defina o HTML do corpo
                # 'Html': {
                #     'Data': body_html,
                #     'Charset': 'UTF-8'
                # }
            }
        }
    }

    # Tentativa de envio
    try:
        response = ses_client.send_email(**email_message)
        print(f"E-mail enviado com sucesso! ID da mensagem: {response['MessageId']}")
    except ClientError as e:
        print(f"Erro ao enviar o e-mail: {e.response['Error']['Message']}")

# Executar a função
send_email()
