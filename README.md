## Amazon SES Email Sender

Esta é uma aplicação simples em Python, desenvolvida para enviar e-mails utilizando o **Amazon SES (Simple Email Service)** da AWS.

### Requisitos

- Python 3.x
- AWS CLI configurado
- Conta na AWS com permissões no SES
- Endereços de e-mail verificados no Amazon SES (se estiver no modo sandbox)

### Instalação

1. **Clonar o repositório:**

   ```bash
   git clone https://github.com/BrunaDev/PoC_SES.git
   cd PoC_SES
   ```

2. **Instalar dependências:**

   Instale a biblioteca Boto3, que é usada para interagir com a AWS:

   ```bash
   pip install boto3
   ```

3. **Configurar o AWS CLI:**

   Configure suas credenciais da AWS (caso ainda não tenha feito):

   ```bash
   aws configure
   ```

   Informe:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Região (ex: `sa-east-1` para São Paulo)
   - Formato de saída (ex: `json`)

4. **Verificar endereços de e-mail no SES:**

   No console da AWS, verifique o endereço de e-mail de envio no SES:
   - Acesse o [Amazon SES](https://console.aws.amazon.com/ses/)
   - Navegue até **Verified Identities**
   - Verifique o e-mail que você deseja usar como remetente.

### Como usar

1. Modifique o script Python para incluir o endereço de e-mail verificado no SES:

   ```python
   sender_email = "seuemail@exemplo.com"
   recipient_email = "destinatario@exemplo.com"
   ```

2. Execute o script para enviar o e-mail:

   ```bash
   python3 teste_ses.py
   ```
