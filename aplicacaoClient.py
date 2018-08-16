
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Fisica da Computacao
#Carareto
#17/02/2018

####################################################

def int_to_bytes(val, num_bytes):
    return [(val & (0xff << pos*8)) >> pos*8 for pos in range(num_bytes)]


def int_to_byte(values, length):
    result = []
    for i in range(0,length):
        result.append(values >> (i*8)& 0xff)

    result.reverse()

    return result


print("comecou")

from enlace import *
import time
from PIL import Image,ImageDraw
import io,os


# voce devera descomentar e configurar a porta com atraves da qual ira fazer a
# comunicacao
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

serialName = "/dev/ttyACM1"           # Ubuntu (variacao de)
#serialName = "/dev/cu.usbmodem1421" # Mac    (variacao de)
#serialName = "COM5"                  # Windows(variacao de)



print("porta COM aberta com sucesso")



def main():

    img = Image.open('dragon.jpg', mode='r')

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicacao foi aberta
    print("comunicacao aberta")


    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    #como fazer isso
    print ("gerando dados para transmissao :")



    txLen    = len(imgByteArr)
    infoArray = int_to_byte(txLen, 5)
    print(len(infoArray))

    txBuffer = imgByteArr
    print(txLen)
    print(bytes(infoArray))

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))
    com.sendData(bytes(infoArray))

    time.sleep(5)
    print("Acordou")
    com.sendData(txBuffer)


    # Atualiza dados da transmissao
    txSize = com.tx.getStatus()


    # Encerra comunicacao
    print("-------------------------")
    print("Comunicacao encerrada")
    print("-------------------------")
    com.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
