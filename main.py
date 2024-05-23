# Pseudocode
# Define class as "TV"
# Define attributes channel
# Define a constructor
# Create TV objects
# Set Values
# Print Values

#Define class as TV
class TV:
    # class variable
    def __init__(self, channel=1, volumelevel=1 ):
        self.channel = channel
        self.volumelevel = volume

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        if 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1
