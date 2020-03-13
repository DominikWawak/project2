from flask import Flask, render_template, request   # Importing the Flask modules required for this project
import RPi.GPIO as GPIO     # Importing the GPIO library to control GPIO pins of Raspberry Pi
from time import sleep      # Import sleep module from time library to add delays
 
# Pins where we have connected servos
servo_pin = 26          

 
GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(servo_pin, GPIO.OUT)     

 
# Created PWM channels at 50Hz frequency
p = GPIO.PWM(servo_pin, 50) #what is a pwm channel

 
# Initial duty cycle
p.start(0)

 
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
# Enable debug mode
app.config['DEBUG'] = True
 
# Store HTML code
TPL = "index.html"
 
# which URL should call the associated function.
@app.route("/")
def home():
    return render_template (TPL)
 
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider1 = request.form["button"]
    
    # Change duty cycle
    p.ChangeDutyCycle(float(slider1))
   
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
   
    return render_template (TPL)
 
# Run the app on the local development server
#if __name__ == "__main__":
    app.run(host= '0.0.0.0')
