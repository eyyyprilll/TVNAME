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

    def volumeUp(self):
        if self.volumelevel < 7:
            self.volumelevel += 1

    def volumeDown(selfself):
        if self.volumelevel < 1:
            self.volumeLevel -= 1

# TestTV Program
def TestTV():
    # Create two TV
    tv1 = TV()
    tv2 = TV()

    #Set Values for tv1
    tv1.turnOn()
    tv1.setchannel(30)
    tv1.setVolume(3)

    #Set Values for tv2
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)

    # Print Values
    print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
    print(f"tv2's channel is {tvw.getChannel()} and volume level is {tv2.getVolume()}")








