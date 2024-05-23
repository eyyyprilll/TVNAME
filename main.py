# Pseudocode
# Define class as "TV"
# Define attributes channel
# Define a constructor
# Create TV objects
# Set Values
# Print Values

# Define class as TV
class TV:
    # class variable
    def __init__(self, channel=1, volumeLevel=1):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel


