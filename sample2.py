import math

multiChannel = 0

def ChannelSubract(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue -= value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)
    

def ChannelAdd(channelID, value):
    global multiChannel

    currentValue = ChannelGetValue(channelID)
    currentValue += value
    if not ValidateValue(currentValue): return
    ChannelSetValue(channelID, currentValue)

def ChannelSetValue(channelID, value):
    global multiChannel
    if not ValidateValue(value): return
    ChannelClear(channelID)
    multiChannel += value * (1000**(channelID - 1))

def ChannelClear(channelID):
    global multiChannel
    if channelID == -1:
        multiChannel = 0
    else:
        channelValue = ChannelGetValue(channelID)
        multiChannel -= channelValue * (1000**(channelID - 1))

def ValidateValue(value):
    if 0 <= value <= 999:
        return True
    else:
        print("Value out of range, operation not performed")
        return False

def DisplayAllChannels():
    print(f"Channel 1 is {ChannelGetValue(1)}")
    print(f"Channel 2 is {ChannelGetValue(2)}")
    print(f"Channel 3 is {ChannelGetValue(3)}")

def ChannelGetValue(channelID):
    return (multiChannel // (1000**(channelID - 1))) % 1000

###DO NOT ALTER ANY CODE BELOW THIS LINE###

def main():    
    global multiChannel
    multiChannel = 123456789
    ChannelSetValue(2,555)
    ChannelSubract(2,111)
    DisplayAllChannels()
    ChannelClear(-1)
    ChannelSubract(3,1)
    ChannelSetValue(1,111)
    ChannelSetValue(2,888)
    DisplayAllChannels()
    ChannelSubract(1,111)
    ChannelAdd(2,111)
    ChannelAdd(3,5555)
    DisplayAllChannels()

#Start the program
if __name__ == "__main__":
    main()

print("Program terminated")
