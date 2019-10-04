import requests

urlInitial1 = 'https://ssl.gstatic.com/dictionary/static/pronunciation/2018-11-15/audio/'
urlEnding1 = '_en_gb_1.mp3'

urlInitial2 = 'https://lex-audio.useremarkable.com/mp3/'
urlEnding2 = '_gb_1.mp3'

url = ""
count = 0
failure = 0

outputFolder = 'C:\\Users\\SUSHANT\\Desktop\\DAA project\\mp3\\ing'
inputFile = 'C:\\Users\\SUSHANT\\Desktop\\DAA project\\10words(ing).txt'
failedFile = 'C:\\Users\\SUSHANT\\Desktop\\DAA project\\failed.txt'

file = open(inputFile, "r")
content = file.read().split("\n")
file.close()

file2 = open(failedFile, "w")

for word in content:
    count = count + 1
    url = urlInitial1 + word + urlEnding1
    r = requests.get(url)

    if(r.status_code == 200):
        file = open(outputFolder + word + '.mp3', 'wb')
        file.write(r.content)
        file.close()
        print(word + ' audio downloaded')
    else:
        url = urlInitial2 + word + urlEnding2
        r = requests.get(url)

        if (r.status_code == 200):
            file = open(outputFolder + word + '.wav', 'wb')
            file.write(r.content)
            file.close()
            print(word + ' audio downloaded')

        else:
            failure = failure + 1
            file2.write(word+'\n')
            print('ERROR: ' + word + ' audio download')

file2.close()
print("Failed download = " + str(failure) + "/" + str(count))