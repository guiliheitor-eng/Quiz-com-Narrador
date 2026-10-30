import pyttsx3


motor = pyttsx3.init()

genero = input('Qual sera o lingua da voz que deseja: Ingles // Portugues')

if genero == 'Ingles':
    
    voices = motor.getProperty("voices")  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    motor.setProperty("voice", voices[1].id)  # changing index, changes voices. 1 for female

elif genero =='Portugues':
        voices = motor.getProperty("voices")  # getting details of current voice
        # engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
        motor.setProperty("voice", voices[0].id)  # changing index, changes voices. 1 for female
else:
      print('Pfv digite um nome valido')


#Começo Quiz
motor.say('Bem-vindo ao quiz de conhecimentos gerais')
motor.runAndWait()
pontos = 0


#Primeira pegunta
motor.say('1. Qual é a capital do Brasil? ')
motor.runAndWait()

res_1 = input('Qual e sua resposta?')

if res_1 == "brasilia" :
    motor.say("Certo!")
    motor.runAndWait()
    pontos += 1
    
else:
        motor.say("Errado! A resposta certa é 'Brasília'.")
        motor.runAndWait()


#Segunda pegunta
motor.say('2. Quantos dias tem um ano que não é bissexto? ')
motor.runAndWait()

res_2 = input('Qual e sua resposta?')

if res_2 == '365' :
    motor.say("Certo!")
    motor.runAndWait()
    pontos += 1
    
else:
        motor.say("Errado! A resposta certa é '365'.")
        motor.runAndWait()


#Terceira pegunta
motor.say('3. Qual é o maior planeta do Sistema Solar? ')
motor.runAndWait()

res_3 = input('Qual e sua resposta?')

if res_3 == "jupiter" :
    motor.say("Certo!")
    motor.runAndWait()
    pontos += 1
    
else:
        motor.say("Errado! A resposta certa é 'Júpiter'.")
        motor.runAndWait()


#Quarta pegunta
motor.say('4. Qual é o maior oceano do mundo? ')
motor.runAndWait()

res_4 = input('Qual e sua resposta?')

if res_4 == "pacifico" :
    motor.say("Certo!")
    motor.runAndWait()
    pontos += 1
    
else:
        motor.say("Errado! A resposta certa é 'Pacífico'.")
        motor.runAndWait()


#Quinta pegunta
motor.say('5. Quem pintou a Mona Lisa? ')
motor.runAndWait()

res_5 = input('Qual e sua resposta?')

if res_5 == "leonardo da vinci" :
    motor.say("Certo!")
    motor.runAndWait()
    pontos += 1
    
else:
        motor.say("Errado! A resposta certa é 'Leonardo da Vinci'.")
        motor.runAndWait()
