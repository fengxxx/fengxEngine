#coding:utf-8 
def loadOBJ(filename): 
    vs=[]
    ns=[]
    fs=[]
    f=open(filename,"r")
    for line in f: 
        vals=line.replace("\n","").split(" ")
        if vals[0] == "v":
            if vals[1]==" " or vals[1]=="": 
                v = map(float, vals[2:6]) 
            else:
                v = map(float, vals[1:5]) 
            vs.append(v)

        elif vals[0] == "vn": 
            if vals[1]==" " or vals[1]=="": 
                n = map(float, vals[2:6])
            else :
                n = map(float, vals[1:5])
            ns.append(n) 
        elif vals[0] == "f": 
            if vals[1]==" " or vals[1]=="": 
                print "f"
                pf=[]
                for f in vals[2:]: 
                    p = f.split("/")
                    pfp=[]
                    for s in p:
                        if s=="" or s=="":
                            pfp.append(0)
                        else:
                            pfp.append(int(s))
                    #pfp=map(int, p)
                    pf.append(pfp)
                fs.append(pf)
            else :
                #print "fs"
                pf=[]
                pn=[]
                pt=[]
                for f in vals[1:]: 
                    p = f.split("/")
                    pfp=[]
                    for s in p:
                        if s=="" or s=="":
                            pfp.append(0)
                        else:
                            pfp.append(int(s))
                    #pfp=map(int, p)
                    #pfp=map(int, p)
                    pf.append(pfp)
                fs.append(pf)
    return (vs,ns, fs) 
    f.close()

#print loadOBJ("C:\\Users\\xiaodong\\Desktop\\test.obj")[2][1]
