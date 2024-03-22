from ftplib import FTP

#Definindo configuração do servidor ftp
ftp = FTP('ftp.us.debian.org')

#Chamar tentativa de login no servidor definido anteriormente "ftp.us.debian.org"
ftp.login()

#Alternando pasta, funciona como o comando "cd nome_diretório"
ftp.cwd("debian")

#Listagem de arquivos e diretórios dentro do diretório atual.
ftp.dir()

#Obtendo arquivo servidor FTP
with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README.html', fp.write)