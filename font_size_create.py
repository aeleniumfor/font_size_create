f = open('font_size.txt','w')



for i in range(100):
    size = i+3
    text = ".size-"+str(size)+"{font-size: "+str(size)+"px;}\n"
    f.write(text)
f.close()
