# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 18:15:40 2018

@author: Arpan
"""
    
from PIL import Image
import math
import heapq as hq
depth=1
dmax=2000


basewidth=640
im = Image.open("me.jpg")
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth,hsize), Image.ANTIALIAS)

val = im.convert('RGB')
valr=val.load()
def quad(x1,y1,x2,y2):
    xm= int((x1+x2)/2)
    ym= int((y1+y2)/2)
    
    return (x1,y1,xm,ym),(xm,y1,x2,ym),(x1,ym,xm,y2),(xm,ym,x2,y2)

def dis(x1,y1,x2,y2):
    if x1==x2 or y1==y2:
        return (0,x1,y1,x2,y2,0,0,0)
    lr=255
    lb=255
    lg=255
    hr=0
    hb=0
    hg=0
    r=0
    b=0
    g=0
    c=0
    var=0
    for i in range(x1,x2):
        for j in range(y1,y2):
            r0,g0,b0 = val.getpixel((i,j))
            
            r+=r0
            lr=min(r0,lr)
            hr=max(r0,hr)
            c+=1
            b+=b0
            lb=min(b0,lb)
            hb=max(b0,hb)
            
            g+=g0
            lg=min(g0,lg)
            hg=max(g0,hg)
            
            var=0-math.sqrt(((hr-lr)**2)+((hb-lb)**2)+((hg-lg)**2))/3
            if var >-20 or x2-x1<10 or y2-y1<10:
            	var=0
    return (var,x1,y1,x2,y2,r/c,g/c,b/c)




def chan(x1,y1,x2,y2,r,g,b):
    for i in range(x1,x2):
        for j in range(y1,y2):
            if i==x1 or i==x2 or j==y1 or j==y2:
                valr[i,j]=(0,0,0)
            else:
                valr[i,j]=(int(r),int(g),int(b))


def final():
    while len(re)!=0:
        var,x1,y1,x2,y2,r,g,b=hq.heappop(re)
        chan(x1,y1,x2,y2,r,g,b)
        
"""
var,x1,y1,x2,y2,r,g,b=dis(0,0,val.size[0],val.size[1])
print(var,x1,y1,x2,y2,r,g,b)    
chan(x1,y1,x2,y2,r,g,b)
val.show()
"""
re=[]
re.append(dis(0,0,val.size[0],val.size[1]))

while depth<=dmax:
    var,x1,y1,x2,y2,r,g,b=hq.heappop(re)
    q1,q2,q3,q4=quad(x1,y1,x2,y2)
    h1 = dis(q1[0],q1[1],q1[2],q1[3])
    h2 = dis(q2[0],q2[1],q2[2],q2[3])
    h3 = dis(q3[0],q3[1],q3[2],q3[3])
    h4 = dis(q4[0],q4[1],q4[2],q4[3])
    #print(re)
    hq.heappush(re,h1)
    hq.heappush(re,h2)
    hq.heappush(re,h3)
    hq.heappush(re,h4)
    depth+=1
    if (re[0][0]>-10):
        break
    

    
final()
val.show()
val.save('meresult.jpg')
