#!/user/bin/python3

import smbus #biblioteca necessaria para o barramento i2c
import time #biblioteca necessaria para o delay
import RPi.GPIO as GPIO #biblioteca necessaria para utilizar os pinos do raspberry
import datetime #bibliotecas necessarias para usar hora e data em tempo real
#from datetime import time
from datetime import datetime
from datetime import date

#classe do sensor
class MLX90614():

    MLX90614_RAWIR1=0x04
    MLX90614_RAWIR2=0x05
    MLX90614_TA=0x06
    MLX90614_TOBJ1=0x07
    MLX90614_TOBJ2=0x08

    MLX90614_TOMAX=0x20
    MLX90614_TOMIN=0x21
    MLX90614_PWMCTRL=0x22
    MLX90614_TARANGE=0x23
    MLX90614_EMISS=0x24
    MLX90614_CONFIG=0x25
    MLX90614_ADDR=0x0E
    MLX90614_ID1=0x3C
    MLX90614_ID2=0x3D
    MLX90614_ID3=0x3E
    MLX90614_ID4=0x3F

    def __init__(self, address=0x8, bus_num=1):
        self.bus_num = bus_num
        self.address = address
        self.bus = smbus.SMBus(bus=bus_num)

    def read_reg(self, reg_addr):
        return self.bus.read_word_data(self.address, reg_addr)

    def data_to_temp(self, data):
        temp = (data*0.02) - 281.15 # +8 graus de offset
        return temp

    def get_amb_temp(self):
        data = self.read_reg(self.MLX90614_TA)
        return self.data_to_temp(data)

    def get_obj_temp(self):
        data = self.read_reg(self.MLX90614_TOBJ1)
        return self.data_to_temp(data)

print ('Temperatura do objeto de teste (08): ')
GPIO.setmode(GPIO.BCM) #ascende o led para indicar que o barramento esta funcionando
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

hoje = date.today() # printa a data de hoje

f = open ("/home/pi/Desktop/tempir08.txt",  'a') #abre o arquivo na froma de leitura e na froma "append" (significa que sempre salva no fim do arquivo referente sem sobreescreve-lo)
f.write (str(hoje))
f.write('\nInfravermelho 08')

#fica preso no while
while(1):
    try:
        if __name__ == "__main__":
            sensor = MLX90614()
            valor = sensor.get_obj_temp()
            print (valor)
            GPIO.output(18,GPIO.HIGH)
            f = open ("/home/pi/Desktop/tempir08.txt",  'a')
            f.write('\n')
            f.write(str(datetime.now().time()))
            f.write(': ')
            f.write(str(valor))
            f.close
            time.sleep(0.5)		#delay de 0.5 segundo
            GPIO.output(18,GPIO.LOW)
		
    except IOError:
        print('quebrei08')
