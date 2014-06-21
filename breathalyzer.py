#from RPiLcdBackpack import AdafruitLcd
from time import sleep
from Adafruit_ADS1x15 import ADS1x15
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)							# numbering scheme
GPIO.setwarnings(False)

fLED = 17										# pin for SLOW FADING LED
rLED = 22										# pin for RED LED
rButton = 24									# pin for RED momentary switch 
bButton = 25									# pin for BLUE momentary switch
rButLED = 23									# pin for the RED momentary switch LED
bButLED = 27									# pin for the BLUE momentary switch LED

GPIO.setup(fLED, GPIO.OUT)						# setup the output pins
GPIO.setup(rLED, GPIO.OUT)
GPIO.setup(rButLED, GPIO.OUT)						
GPIO.setup(bButLED, GPIO.OUT)
GPIO.setup(rButton, GPIO.IN)					# setup input pins
GPIO.setup(bButton, GPIO.IN)


ADS115 = 0x01									# 16-bit ADC ADS115
gain = 4096										# +/- 4.096V
sps = 250										# samples per second
#adc = ADS1x15(ic=ADS115)						# initialize ADC with default I2C

#bLCD = AdafruitLcd()							# LCD object

input = ""


while input.lower() != "q":
	print "\nW - LED Test #1\t\tS - LED Test #2\t\tL - LCD Test\nA - Alcohol Test\tB - Button Test\t\tQ - End Script\n"
	
	input = raw_input("Enter Input: ")
	
	if input.lower() == "w":					# led test 2
		print "\nFADE ON -- RED OFF"
		GPIO.output(fLED, True)
		GPIO.output(rLED, False)
	elif input.lower() == "s":					# led test 2
		print "\nFADE OFF -- RED ON"
		GPIO.output(fLED, False)
		GPIO.output(rLED, True)
	#elif input.lower() == "l":					# LCD test
		#print "\nlcd test"
		#lcd.blink(False)
		#lcd.cursor(False)
		#lcd.clear()
		#lcd.backlight(True)
		#lcd.message("testing!")
		#sleep(2)
	#elif input.lower() == "a":					# MQ3 alcohol sensor test
		#print "\nsensor reading test"
		#volts = adc.readADCSingleEnded(0,gain,sps) / 1000
	elif input.lower() == "b":					# button test
		print "\nBUTTON TESTING -- \nRED -> TEST PRINT -- BLUE -> EXIT TEST"
		#GPIO.output(rButton, True)
		GPIO.output(rButLED, True)				# turn on button LEDS
		GPIO.output(bButLED, True)
		
		while GPIO.input(bButton) == False:
			if GPIO.input(rButton):				# read button presses
				print "Red is Pressed!"
				sleep(0.5)						# debouncing
		print "Blue is Pressed!"
		GPIO.output(rButLED, False)				# turn off button LEDS
		GPIO.output(bButLED, False)
		
	sleep(0.1)

GPIO.output(fLED, False)
GPIO.output(rLED, False)
#GPIO.output(rButton, False)	
GPIO.cleanup()

