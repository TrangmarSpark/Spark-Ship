# Spark-Ship Hybrid Controls - voice + physical + touchscreen
import RPi.GPIO as GPIO
from pocketsphinx import LiveSpeech

# Physical switch pins (example - you can change later)
HEATING_PIN = 17
LIGHTS_PIN = 18
WIPERS_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(HEATING_PIN, GPIO.OUT)
GPIO.setup(LIGHTS_PIN, GPIO.OUT)
GPIO.setup(WIPERS_PIN, GPIO.OUT)

def handle_physical_button(pin, name):
    state = GPIO.input(pin)
    print(f"Physical {name} toggled - state: {state}")
    # Real code will control heating, lights, etc.

# Simple offline voice (PocketSphinx)
def listen_for_voice():
    speech = LiveSpeech()
    for phrase in speech:
        print("Heard:", phrase)
        if "heating" in str(phrase):
            GPIO.output(HEATING_PIN, not GPIO.input(HEATING_PIN))
            print("Heating toggled via voice")

print("🚀 Spark-Ship hybrid controls started")
print("Offline voice + physical switches + touchscreen ready")
