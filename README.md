# AmongUs Bot
## Introdução
### Esse é um bot de discord em desenvolvimento usando python para ajudar na hora de mutar e desmutar no jogo Among Us.
## Instalação
### Para utilizar o bot, você deve seguir os seguintes passos:
#### > Instalar as bibliotecas, utilizando o comando:
```shell
pip install -r requirements.txt 
```
#### > Instalar o [tesseract](https://github.com/UB-Mannheim/tesseract/wiki), ele será usado para fazer a conversão de imagem para texto. Caso esteja usando Windows, é só baixar o instalador no link anterior. Caso esteja usando Linux, basta executar as seguintes linhas no terminal:
```shell
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev 
```
#### > Agora só falta configurar no arquivo .env o seu token de acesso e rodar o bot usando o seguinte comando no terminal aberto na pasta do bot:
```shell
python bot.py
```
