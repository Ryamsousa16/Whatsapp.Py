import pywhatkit as kit
import time

question = str(input('''Você sabe o DDD da pessoa??? S/N
: ''')).upper().strip()

if question in 'S':
    ddd = int(input('DDD: '))

if question in 'N':
    print('Espero que esta lista de DDD do nosso território nacional ajude-o')
    time.sleep(1.5)
    print('''– Distrito Federal (61)
    – Goiás (62 e 64)
    – Mato Grosso (65 e 66)
    – Mato Grosso do Sul (67)
    – Alagoas (82)
    – Bahia (71, 73, 74, 75 e 77)
    – Ceará (85 e 88)
    – Maranhão (98 e 99)
    – Paraíba (83)
    – Pernambuco (81 e 87)
    – Piauí (86 e 89)
    – Rio Grande do Norte (84)
    – Sergipe (79)
    – Acre (68)
    – Amapá (96)
    – Amazônas (92 e 97)
    – Pará (91, 93 e 94)
    – Rondônia (69)
    – Roraima (95)
    – Tocantins (63)
    – Espírito Santo (27 e 28)
    – Minas Gerais (31, 32, 33, 34, 35, 37 e 38)
    – Rio de Janeiro (21, 22 e 24)
    – São Paulo (11, 12, 13, 14, 15, 16, 17, 18 e 19)
    – Paraná (41, 42, 43, 44, 45 e 46)
    – Rio Grande do Sul (51, 53, 54 e 55)
    – Santa Catarina (47, 48 e 49)''')
    ddd = int(input("Qual o DDD???\n: "))

number = int(input('Número: ').replace('-', ''))
result = str((f'+55{ddd}', number))

message = str(input('Digite a mensagem que deseja enviar: '))

hour = int(input("Que horas esta mensagem será enviada (exemplo) : "))

minutes = int(input('''Qual minuto deseja que a mensagem seja enviada???
    : '''))

kit.sendwhatmsg(result, message, hour, minutes)


