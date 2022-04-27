import speech_recognition as sr
import pyttsx3
while True:
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say('Olá, meu nome é sexta feira, o que posso fazer por você hoje senhor?')
    maquina.runAndWait()


    def executa_comando():

        try:
            with sr.Microphone() as source:
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()

                if 'agile' in comando:
                    comando = comando.replace('agile', '')
                    maquina.say(comando)
                    maquina.runAndWait()
        except:
            print('Microfone não está conectado')
        return comando

comando_voz_usuario()
