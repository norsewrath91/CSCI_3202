__author__ = 'Nick'



sampleArray = [0.82,	0.56,	0.08,	0.81,	0.34, 0.22, 0.37, 0.99, 0.55, 0.61, 0.31, 0.66, 0.28, 1.0, 0.95,
0.71,	0.14,	0.1,	1.0,	0.71,	0.1,	0.6,	0.64,	0.73,	0.39,	0.03,	0.99,	1.0,	0.97,	0.54,	0.8,	0.97,
0.07,	0.69,	0.43,	0.29,	0.61,	0.03,	0.13,	0.14,	0.13,	0.4,	0.94,	0.19, 0.6,	0.68,	0.36,	0.67,
0.12,	0.38,	0.42,	0.81,	0.0,	0.2,	0.85,	0.01,	0.55,	0.3,	0.3,	0.11,	0.83,	0.96,	0.41,	0.65,
0.29,	0.4,	0.54,	0.23,	0.74,	0.65,	0.38,	0.41,	0.82,	0.08,	0.39,	0.97,	0.95,	0.01,	0.62,	0.32,
0.56,	0.68,	0.32,	0.27,	0.77,	0.74,	0.79,	0.11,	0.29,	0.69,	0.99,	0.79,	0.21,	0.2,	0.43,	0.81,
0.9,	0.0,	0.91,	0.01]


def prior():
    #list of [couldy,rain,sprinkler,wetgrass] samples
    samples = []
    cloudy = False
    sprinkler = False
    rain = False
    wetGrass = False
    count = 0

    while count < 100:
        if sampleArray[count] < 0.5:
            cloudy = True


        count += 1

        if cloudy == True:
            if sampleArray[count] < 0.1:
                sprinkler = True

            if sampleArray[count + 1] < 0.8:
                rain = True

        else: #cloudy = False
            if sampleArray[count] < 0.5:
                sprinkler = True

            if sampleArray[count + 1] < 0.2:
                rain = True

        count += 2

        if sprinkler == True and rain == True:
            if sampleArray[count] < 0.99:
                wetGrass = True

        elif sprinkler == False and rain == True:
            if sampleArray[count] < 0.9:
                wetGrass = True

        elif sprinkler == True and rain == False:
            if sampleArray[count] < 0.9:
                wetGrass = True


        samples.append([cloudy,sprinkler,rain,wetGrass])
        cloudy = False
        sprinkler = False
        rain = False
        wetGrass = False
        count += 1

    #out of while loop
    total = 25.0
    cloudCount = 0
    rainCount = 0
    cloudyRainCount = 0
    sprinklerCount = 0
    sprinklerWetCount = 0
    wetGrassCount = 0
    cloudyWet = 0
    cloudySprinklerWet = 0

    for list in samples:
        if list[0] == True:
            cloudCount += 1
        if list[1] == True:
            sprinklerCount +=1
        if list[2] == True:
            rainCount += 1
        if list[3] == True:
            wetGrassCount += 1
        if list[0] == True and list[2] == True:
            cloudyRainCount += 1
        if list[1] == True and list[3] == True:
            sprinklerWetCount += 1
        if list[0] == True and list[3] == True:
            cloudyWet += 1
        if list[0] == True and list[1] == True and list[3] == True:
            cloudySprinklerWet +=1


    print "Calculated Probabilities using Prior Sampling"
    print "P(c=true):"
    print cloudCount/total
    print "P(c=true|r=true):"
    print ((cloudyRainCount/total)/(rainCount/total))
    print "P(s=true|w=true):"
    print ((sprinklerWetCount/total)/(wetGrassCount/total))
    print "P(s=true|c=true,w=true): "
    print cloudySprinklerWet
    print cloudyWet
    print ((cloudySprinklerWet/total)/(cloudyWet/total))


def rejection1():
  #list of [couldy,rain,sprinkler,wetgrass] samples
    cloudyCount = 0
    count = 0

    while count < 100:
        if sampleArray[count] < 0.5:
            cloudyCount += 1
        count += 1

    print "Calculated probabilities using Rejection Sampling"
    print "P(c=true) using rejection sampling:"
    print cloudyCount/100.0

def rejection2():

    cloudy = False
    cloudyCount = 0
    rainCount = 0
    cloudyRain = 0
    total = 0.0
    count = 0
    count2 = 100 #make sure we always have at least 3 samples left

    while count < 100 and count2 > 3:
        if sampleArray[count] < 0.5:
            cloudy = True
            cloudyCount +=1
        count += 1
        count2 -= 1

        if cloudy == True:
            if sampleArray[count] < 0.8:
                rainCount += 1
                cloudyRain += 1
                total += 1

        else: #cloudy = False
            if sampleArray[count + 1] < 0.2:
                rainCount += 1
                total += 1
        count += 1
        count2 -= 1

        cloudy = False

    print "P(c=true|rain):"
    print (cloudyRain/total)/(rainCount/total)

def rejection3():

    cloudy = False
    sprinkler = False
    rain = False
    wetGrassCount = 0
    sprinklerWetGrassCount = 0
    count = 0
    count2 = 100
    total = 0.0

    while count < 100 and count2 > 4:
        if sampleArray[count] < 0.5:
            cloudy = True
        count += 1
        count2 -= 1

        if cloudy == True:
            if sampleArray[count] < 0.1:
                sprinkler = True
            if sampleArray[count + 1] < 0.8:
                rain = True
        else: #cloudy = False
            if sampleArray[count] < 0.5:
                sprinkler = True
            if sampleArray[count + 1] < 0.2:
                rain = True
        count += 2
        count2 -= 2

        if sprinkler == True and rain == True:
            if sampleArray[count] < 0.99:

                wetGrassCount += 1
                sprinklerWetGrassCount += 1
                total += 1

        elif sprinkler == False and rain == True:
            if sampleArray[count] < 0.9:

                wetGrassCount += 1
                total += 1

        elif sprinkler == True and rain == False:
            if sampleArray[count] < 0.9:

                wetGrassCount += 1
                sprinklerWetGrassCount += 1
                total += 1
        count += 1
        count2 -= 1


        cloudy = False
        sprinkler = False
        rain = False


    print "P(s=true|w=true):"
    print (sprinklerWetGrassCount/total)/(wetGrassCount/total)

def rejection4():
    return None


def main():
    prior()
    rejection1()
    rejection2()
    rejection3()



main()