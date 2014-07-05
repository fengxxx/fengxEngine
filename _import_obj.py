def loadOBJ(filename): 
    numVerts = 0 
    vertexs = []
    faces=[] 
    norms = [] 
    vertsOut = [] 
    normsOut = [] 
    f=open(filename)
    #line=f.readline()

    for line in f: 
        #print line
        vals=line.replace("\n","").split(" ")
        #print vals
        if vals[0] == "v":
            #print vals 
            if vals[1]==" " or vals[1]=="": 
                v = map(float, vals[2:6]) 
                vertexs.append(v) 
            else:
                ()
                v = map(float, vals[1:5]) 
                vertexs.append(v)
            #print v
        elif vals[0] == "vn": 
            if vals[1]==" " or vals[1]=="": 
                n = map(float, vals[2:6])
            else :
                n = map(float, vals[1:5])
            norms.append(n) 
        elif vals[0] == "f": 

            for f in vals[1:]: 
                w = f.split("/")
                #if w[0]
                faces.append(int(w[0])-1)
                #print w
                #print w[0] 
                # OBJ Files are 1-indexed so we must subtract 1 below 
                #vertsOut.append(list(verts[int(w[0])-1])) 
                #normsOut.append(list(norms[int(w[0])-1])) 
                numVerts += 1
    return vertexs, faces ,norms  
    f.close()

#print loadOBJ("D:/desktop/testObj.obj")[1]