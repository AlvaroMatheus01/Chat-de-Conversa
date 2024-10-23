#Titulo 

#Botão iniciar Chat
    #Pop-up
        #titulo (bem vindo ao Papizap)
        #Campo de texto (escreva seu nome)
        #botao (entrar no chat)
            #Sumir com o titulo e o botao inicial
            #fechar o pop-up
            #criar o chat(com a mensagem "nome do usuario" entrou no chat)
            #Embaixo do chat:
                #Campo de texto: digite sua mensagem
                #botaoEnviar
                    #Vai aparecer a mensagem no chat com o nome do usuario
                    
#importar o flet
import flet as ft

#criar a função principal do seu sistema
def main(pagina):
    titulo =ft.Text("PAPIZAP")
    
    def enviar_mensam_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensam_tunel)
    
    titulo_janela = ft.Text("Bem vindo a Papizap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    
    
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        #enviar a mensagem no chat:
            #Usuairo:mensagem
        
        #mensagem do tunel
        pagina.pubsub.send_all(texto)
        
        # Limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()
    
    arquivo = ft.FilePicker()
    texto_mensagem =ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click= enviar_mensagem)
    chat = ft.Column()
    
    
    linha_mensagem= ft.Row([texto_mensagem, botao_enviar])
    #Entrando no chat
    def entrar_chat(evento):
        #tirar o titulo da pagina
        pagina.remove(titulo)
        #tirar o botao_iniciar
        pagina.remove(botao_iniciar)
        #fechar o popup
        janela.open = False
        #criar o chat
        pagina.add(chat)
        #criar campo de texto de enviar mensagem
        pagina.add(linha_mensagem)
        
        #Escrever a mensagem: usuario entrou no chat
        texto_entrou_chat= f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)

        pagina.update()
    
    
    botao_entrar= ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(title= titulo_janela, content= campo_nome_usuario, actions=[botao_entrar])
    
    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
    
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat",on_click=abrir_popup)
    
    
    pagina.add(titulo)
    pagina.add(botao_iniciar)


#executar o seu sistema
ft.app(main, view=ft.WEB_BROWSER)