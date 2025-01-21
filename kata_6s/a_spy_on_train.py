# Task
#
# You are a spy. You lurk in the enemy's control zone. Your task is to get the length data of a railway, a
# ccurate to meters.
#
# Although you have taken all kinds of technical measures, you still haven't finished your task.
#
# Now, You can only use the last method: Take the train, record the sounds you hear, and then calculate
# the length of the railroad.
#
# You will hear these voices:
#
# 1. "呜呜呜". This is the whistle of the train when it comes in or out of the station.
#
# That is, When you hear the sound for the first time, the train leaves the
# station and goes into high speed; When you hear the sound for the second
# time, The train pulled into the station and goes into low speed. and so on.
#
# 2. "哐当". This is the sound of the train hitting the railroad track.
#
# That is, Every time you hear it, the train advances 20 meters(high speed)
# or 10 meters(low speed).
#
# 3. Any other sound. These are all noise, please ignore them ;-)
# Examples
#
# For sounds="呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当"
# The output should be 150.
#
# For sounds="呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当呜呜呜哐当哐当哐当哐当哐当"
# The output should be 300.
#
# For sounds="呜呜呜哐当哐当面包饮料矿泉水了啊，哐当桶面火腿肠茶叶蛋了啊哐当哐当呜呜呜哐当哐当哐当北京站到了，
# 下车的旅客请带好您的行李，准备下车哐当哐当"
# The output should be 150.

def length_of_railway(sounds):
    sounds = "".join(x for x in sounds if x in "哐当呜")
    print(sounds)

    high = False
    low = True
    t20 = 20
    t10 = 10
    counter = 0

    train = "呜呜呜"
    distance = "哐当"

    for i, char in enumerate(sounds):
        if sounds[i: i + 3] == train and not high:
            high = True
        elif sounds[i: i + 3] == train and high:
            high = False
            low = True
        if sounds[i: i + 2] == distance:
            if high:
                counter += t20
            elif low:
                counter += t10

    return counter


def length_of_railway2(sounds):
    speed = False
    multi = 10
    m = 0

    s = sounds.split("呜呜呜")

    for char in s:
        x = char.count("哐当")
        m += (x * multi)
        if not speed:
            speed = True
            multi = 20
        else:
            speed = False
            multi = 10
    return m


def length_of_railway3(s):
    s = s.replace("呜呜呜", "a").replace("哐当", "b")
    total = 0
    num = 10
    for char in s:
        if char == "a":
            num = 20 if num == 10 else 10
        if char == "b":
            total += num
    return total


def length_of_railway4(s):
    speed = False
    number = 10
    total = 0

    train = "呜呜呜"
    distance = "哐当"

    for i, char in enumerate(s):

        if s[i:i + 3] == train:
            speed = True if not speed else False
        if s[i:i + 2] == distance:
            number = 20 if speed else 10
            total += number
    return total