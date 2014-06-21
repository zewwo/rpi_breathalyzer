#from RPiLcdBackpack import AdafruitLcd
from time import sleep
from Adafruit_ADS1x15 import ADS1x15
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)							# numbering scheme
GPIO.cleanup()								# reset existing channels
GPIO.setwarnings(False)

fLED = 17								# pin for SLOW FADING LED
rLED = 22								# pin for RED LED
rButton = 18								# pin for RED momentary switch 
bButton = 23								# pin for BLUE momentary switch

GPIO.setup(fLED, GPIO.OUT)						# setup the output pins
GPIO.setup(rLED, GPIO.OUT)
GPIO.setup(rButton, GPIO.IN)						# setup input pins
GPIO.setup(bButton, GPIO.IN)

ADS115 = 0x01								# 16-bit ADC ADS115
gain = 4096								# +/- 4.096V
sps = 250								# samples per second
#adc = ADS1x15(ic=ADS115)						# initialize ADC with default I2C

#bLCD = AdafruitLcd()							# LCD object



while input.lower() != "q":
	print "\nW - LED Test #1\tS - LED Test #2\tL - LCD Test\nA - Alcohol Test\tB - Button Test\tQ - End Script"
	
	input = raw_input("Enter Input: ")
	
	if input.lower() == "w":					# led test 2
		print "FADE ON -- RED OFF"
		GPIO.output(fLED, True)
		GPIO.output(rLED, False)
	elif input.lower() == "s":					# led test 2
		print "FADE OFF -- RED ON"
		GPIO.output(fLED, False)
		GPIO.output(rLED, True)
	#elif input.lower() == "l":					# LCD test
		#print "lcd test"
		#lcd.blink(False)
		#lcd.cursor(False)
		#lcd.clear()
		#lcd.backlight(True)
		#lcd.message("testing!")
		#sleep(2)
	#elif input.lower() == "a":					# MQ3 alcohol sensor test
		#print "sensor reading test"
		#volts = adc.readADCSingleEnded(0,gain,sps) / 1000
	elif input.lower() == "b":					# button test
		print "BUTTON TESTING -- \nRED -> TEST PRINT -- BLUE -> EXIT TEST"
	
		while !GPIO.input(rButton):
			if GPIO.input(rButton):
				print "Red is Pressed!"
		print "Blue is Pressed!"
		
	sleep(1)
	
GPIO.cleanup()

