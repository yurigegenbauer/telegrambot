import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        token = 'My Private Token'
        self.url_base = f'https://api.telegram.org/bot{token}/'

#1- Iniciar o bot
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.recebendo_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    primeira_mensagem_cliente = mensagem['message']['message_id'] == 1
                    resposta = self.criar_resposta(mensagem,primeira_mensagem_cliente)
                    self.responder(resposta,chat_id)

#2- Obter mensagens
    def recebendo_mensagens(self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)


#3- Criar resposta
    def criar_resposta(self,mensagem,primeira_mensagem_cliente):
        mensagem = mensagem['message']['text']
        if primeira_mensagem_cliente == True or mensagem.lower() == "menu":
            return f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Olá seja bem vindo(a)! Oque gostaria de pedir hoje? Digite o primeiro caractere para continuar.{os.linesep}
Cardapio - Para acessar o cardápio da casa.{os.linesep}
Local - Para ver onde fica a localização do restaurante.{os.linesep}
Reclamação - Iremos te enviar um email para contato.{os.linesep}
(C/L/R)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''
        else:
            print('Digite apenas os comandos selecionados')
        if mensagem.lower() in ('c'):
            return f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Esses são os salgados que temos em nosso cardápio: {os.linesep}
1- Pizza.{os.linesep}
2- Hamburguer.{os.linesep}
3- Coxinha.{os.linesep}
(1/2/3)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''

        if mensagem.lower() in ('l'):
            return f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
R. lalalala, 80 - Centro, Curitiba - PR, 12345-678
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='''

        if mensagem.lower() in ('r'):
            return f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Para conseguir fazer sua reclamação, envie um email para reclamacao@restaurante.com
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''


        if mensagem == '1':
            return f'''A Pizza custa 35 reais!{os.linesep}Gostaria de confirmar seu pedido ou adicionar uma bebida?{os.linesep}(S/BP)'''
        if mensagem == '2':
            return f'''O Hamburguer custa 23 reais!{os.linesep}Gostaria de confirmar seu pedido ou adicionar uma bebida?{os.linesep}(S/BH)'''
        if mensagem == '3':
            return f'''A Coxinha custa 8 reais!{os.linesep}Gostaria de confirmar seu pedido ou adicionar uma bebida?{os.linesep}(S/BC)'''

        if mensagem.lower() in ('s','sim'):
            return 'Pedido Confirmado!'

            #Caso a pessoa compre 1 Pizza
        if mensagem.lower() in ('bp'):
            return f'''
            4p- Para pedir uma Coca, ela custa R$7{os.linesep}5p- Para pedir um Suco, ele custa R$5{os.linesep}6p- Para pedir uma Cerveja, ela custa R$6
            '''
        elif mensagem == '4p':
            return f'''O pedido final deu 42 reais! Pague na entrega.'''
        elif mensagem == '5p':
            return f'''O pedido final deu 40 reais! Pague na entrega.'''
        elif mensagem == '6p':
            return f'''O pedido final deu 41 reais! Pague na entrega.'''

            #Caso a pessoa compre 1 Hamburguer
        if mensagem.lower() in ('bh'):
            return f'''
            4h- Para pedir uma Coca, ela custa R$7{os.linesep}5h- Para pedir um Suco, ele custa R$5{os.linesep}6h- Para pedir uma Cerveja, ela custa R$6
            '''
        elif mensagem == '4h':
            return f'''O pedido final deu 30 reais! Pague na entrega.'''
        elif mensagem == '5h':
            return f'''O pedido final deu 28 reais! Pague na entrega.'''
        elif mensagem == '6h':
            return f'''O pedido final deu 29 reais! Pague na entrega.'''
            
            #Caso a pessoa compre 1 Coxinha
        if mensagem.lower() in ('bc'):
            return f'''
            4c- Para pedir uma Coca, ela custa R$7{os.linesep}5c- Para pedir um Suco, ele custa R$5{os.linesep}6c- Para pedir uma Cerveja, ela custa R$6
            '''
        elif mensagem == '4c':
            return f'''O pedido final deu 15 reais! Pague na entrega.'''
        elif mensagem == '5c':
            return f'''O pedido final deu 13 reais! Pague na entrega.'''
        elif mensagem == '6c':
            return f'''O pedido final deu 14 reais! Pague na entrega.'''

        else:
            return 'Gostaria de acessar o menu? Digite "menu"'


#4- Responder
    def responder(self,resposta,chat_id):
    #5- Enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()