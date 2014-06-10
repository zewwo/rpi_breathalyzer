from RPiLcdBackpack import AdafruitLcd
from time import sleep
from Adafruit_ADS1x15 import ADS1x15
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)					' numbering scheme
GPIO.cleanup()							' reset channels
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)					' set the output pin

ADS115 = 0x01							' 16-bit ADC ADS115
gain = 4096								' +/- 4.096V
sps = 250								' samples per second
adc = ADS1x15(ic=ADS115)				' initialize ADC with default I2C

bLCD = AdafruitLcd()					' LCD object



while True:
	print "\nW = Pin 17 HIGH\t L = Test LCD\n S = Pin 17 LOW\t A = Test Read\nQ = Quit\n"
	
	input = raw_input("Enter Input: ")
	
	if input.tolower() == "w":
		'GPIO.output(17,GPIO.HIGH)
	elif input.tolower() == "a":
		'GPIO.output(17,GPIO.LOW)
	elif input.tolower() == "l":
		'lcd test
		'lcd.blink(False)
		'lcd.cursor(False)
		'lcd.clear()
		'lcd.backlight(True)
		'lcd.message(string)
		'sleep(x)
	elif input.tolower() == "a":
		'test read
		'volts = adc.readADCSingleEnded(0,gain,sps) / 1000
	elif input.tolower() == "q":
		break
	
