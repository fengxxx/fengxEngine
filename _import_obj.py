#coding:utf-8 
def getVals_from_objFile(filename): 
    vs=[]
    vt=[]
    vn=[]
    fs=[]
    objectName=[]
    groupName=[]
    smoothGroup=[]
    materials=[]
    file_obj=open(filename,"r")
    vert_count=0
    face_count=0
    for line in file_obj: 
        line_split=line.split()
        if not line_split:
            continue
        line_start=line_split[0]
        if line_start == "v":
            vert_count+=1
            vs.append(map(float, line_split[1:5]) )
        elif line_start == "vn": 
            vn.append(map(float, line_split[1:5])) 
        elif line_start == "vt": 
            vt.append(map(float, line_split[1:5])) 
        elif line_start == "f": 
            face_count+=1
            faces=[]
            for f in line_split[1:]: 
                f_split = f.split("/")
                face_data=[]
                if len(f_split)==1:
                    face_data.append(int(line_split[1]))
                    face_data.append(0)
                    face_data.append(0)
                elif len(f_split)==3:
                    for s in f_split:
                        if s=="":
                            face_data.append(0)
                        else:
                            face_data.append(int(s))
                elif len(f_split)==2:
                    for s in f_split:
                        face_data.append(int(s))
                    face_data.append(0)
                faces.append(face_data)
            fs.append(faces)
        elif line_start == "s": 
            smoothGroup.append([line_split[1],face_count])
        elif line_start == "g":
            if len(line_split)>1:
                groupName.append(line_split[1])
            else: groupName.append("noName")
        elif line_start == "o": 
            if len(line_split)>1:
                objectName.append(line_split[1])
            else: objectName.append("noName")
        elif line_start == "usemtl":
            materials.append([line_split[1],face_count])
             
    file_obj.close()
    return vs,vt,vn,fs,objectName,groupName,smoothGroup,materials


if __name__ == '__main__':
    import os 
    filename="d:\\desktop\\tem.obj"  
    #filename="D:\\desktop\\ssss.obj"
    if os.path.isfile(filename):
        a=getVals_from_objFile(filename)
        # for s in a:
           # print s
        print len(a[0]),len(a[1]),len(a[2]),len(a[3])
        print a[7],a[6]
        #for s in a[7]:
        #    print s
        '''
        for s in a[3]: 
            for ss in s:
                if ss[1]>6489:
                    print ss[1]
        '''
        #print len(a[3])
    else:
        print"filename: is exist!"
