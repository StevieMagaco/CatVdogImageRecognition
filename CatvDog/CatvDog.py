from PIL import Image
import numpy as np
np.seterr(over='ignore')
import matplotlib.pyplot as plt
from collections import Counter
import math
import pandas as pd


def CATvDogthreshold(imageArray):
    balanceAr = []
    newAr = imageArray
    #for eachRow in imageArray:
    #    for eachPix in eachRow:
    #        avgNum = reduce(lambda x, y: x + y, eachPix[:2]) / len(eachPix[:2])
    #        balanceAr.append(avgNum)
    #balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    x = 0
    for eachRow in newAr:
        for eachPix in eachRow:
            #if reduce(lambda x, y: x + y, eachPix[:2]) / len(eachPix[:2]) > balance:
                if math.isnan(math.floor(eachPix[0]/ math.sqrt(eachPix[0]))) == False:
                    eachPix[0] = math.floor(eachPix[0]/ math.sqrt(eachPix[0]))#1 #255

                if math.isnan(math.floor(eachPix[1]/ math.sqrt(eachPix[1]))) == False:
                    eachPix[1] = math.floor(eachPix[1]/ math.sqrt(eachPix[1]))#1 #255

                if math.isnan(math.floor(eachPix[2]/ math.sqrt(eachPix[2]))) == False:
                    eachPix[2] = math.floor(eachPix[2]/ math.sqrt(eachPix[2]))#1 #255
            #else:
                #eachPix[0] = 0 #0
                #eachPix[1] = 0 #0
                #eachPix[2] = 0 #0

        x+=1

    #print(x)
    return newAr

def CATvDogcreateExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,5000)
    catDog = ['cat', 'dog']
    newSize = 64,64
    for eachNum in catDog:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum * 2))
            imgFilePath = 'train/'+str(eachNum)+'.'+str(furtherNum * 2)+'.jpg'
            ei = Image.open(imgFilePath)

            ei.thumbnail(newSize)

            eiar = np.array(ei)


            eiar = CATvDogthreshold(eiar)

            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

def returnIsDog(filePath, path):
    matchedAr = []
    loadExamps = path

    newSize = 64, 64

    i = Image.open(filePath)

    i.thumbnail(newSize)

    pic = np.array(i)

    iar = CATvDogthreshold(pic)

    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            # x = 0
            for x in range(0, len(eachPixEx), 1):
                if eachPixEx[x] == eachPixInQ[x]:
                    if currentNum == 'cat':
                        matchedAr.append(1)
                    elif currentNum == 'dog':
                        matchedAr.append(2)

                        # x += 1
        except Exception as e:
            # print(str(e))
            x = e

    # print(matchedAr)
    x = Counter(matchedAr)

    if (x[1] > x[2]):
        return False
    else:
        return True

def CATvDogwhatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    newSize = 64, 64

    i = Image.open(filePath)

    i.thumbnail(newSize)

    pic = np.array(i)

    iar = CATvDogthreshold(pic)

    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            #x = 0
            for x in range(0,len(eachPixEx),1):
                if eachPixEx[x] == eachPixInQ[x]:
                    if currentNum == 'cat':
                        matchedAr.append(1)
                    elif currentNum == 'dog':
                        matchedAr.append(2)

                #x += 1
        except Exception as e:
            #print(str(e))
            x = e

    #print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]

    isdog = 'dog'
    if (x[1] > x[2]):
        isdog = 'cat'

    print(x[1])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax1.title.set_text('This is a: '+ isdog)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)
    ax2.set_xlabel('<== CAT / DOG ==>')

    ax1.imshow(np.array(i))
    ax2.bar(graphX, graphY, align='center')

    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()


def Submission(x):

    id = range(1, x, 1)
    label = []
    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    for index in id:
        print(index)
        imgFilePath = 'test/' + str(index) + '.jpg'
        if returnIsDog(imgFilePath, loadExamps) == True:
            label.append(1)
        else:
            label.append(0)

    print(label)
    subs = {'id': id, 'labels': label}
    sub = pd.DataFrame(subs)

    sub.to_csv('submission.csv', index=False)


CATvDogwhatNumIsThis('test/114.jpg')
#Submission(101)
#CATvDogcreateExamples()
