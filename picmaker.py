#python file
#all:
#python imgmaker.py
import random
r=open("colordistance.ppm",'w')
def head():
    return "P3 500 500 255 \n"
def body(color):
    #returns random assortment of colors
    bodyAdd=''
    for i in range(500):
        for j in range(500):
            if color=='color':
                r=random.randint(0,j)
                g=(random.randint(0,j)+r)%255
                b=(random.randint(0,j)+g)%255
                bodyAdd+="%d %d %d " % (r,g,b)
        bodyAdd+="\n"
    return bodyAdd
r.write(head()+body('color'))
r.close()
