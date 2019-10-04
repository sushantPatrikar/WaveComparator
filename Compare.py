from scipy.io import wavfile
import numpy as np
import pingouin  as pg
import pandas as pd

_,data = wavfile.read('wav//ed//mp3baked.wav')
_,data1 = wavfile.read('wav//ing//ingeating.wav')

i= data.shape[0]-1
j = data1.shape[0]-1
index_1 = -1
index_2 = -1


try:
    data.shape[1]
except IndexError:
    data = data.reshape(data.shape[0],1)

try:
    data1.shape[1]
except IndexError:
    data1 = data1.reshape(data1.shape[0],1)

while True:
    if data[i,0] !=0 and index_1==-1:
        index_1 = i
        pass
    if data1[j,0] !=0 and index_2==-1:
        index_2 = j
        pass
    if index_1!=-1 and index_2!=-1:
        break
    i-=1
    j-=1

data = data[-index_1:,:]
data1 = data1[-index_2:,:]

data = data[-2000:,:]
data1= data1[-2000:,:]


x =pg.corr(x=data[:,0],y=data1[:,0])
print(x)



















# print(data.tostring())
# print(data1.tostring())


# data = data[:,:]
# data1 = data1[:,:]
# data = data.reshape(data.shape[0],1)
# data1 = data1.reshape(data1.shape[0],1)
# data = data[-10000:,:]
# data1 = data1[-10000:,:]
# print(data1.shape[1])

# df = pd.DataFrame(data,data1)
# print(df.head())
# print(data1.shape)
# data = data[-5000:,:]
# data1 = data1[-5000:,:]
# #
# x =pg.corr(x=data[:,0],y=data1[:,0])
# print(x)
