import sys
import glob
import re   
num = 30000
path = '*.txt'
files=glob.glob(path)   
for file in files:   
    with open(file) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            num = 30000
            if 'catholic' in lines[i] or 'orthodox' in lines[i]:
                num = 30000
                religion = lines[i]
                religionnum = i
                z = i
                condz = False
                while condz == False:
                    if 'death=' in lines[z] or 'death =' in lines[z]:
                     i = 1
                     cond = False
                     while cond == False:
                        if "." in lines[z-i] and ('={' in lines[z-1] or '= {' in lines[z-i]):
                            test = re.sub('\s+',' ',lines[z-i])
                            test = test.strip('#')
                            if '}' in test:
                                test = test[2:]
                            num = int(test.split(".")[0].strip())
                            cond = True
                            condz = True
                        else:
                            i = i + 1
                    else:
                        z = z + 1    



             
                if num < 1054:
                    if 'catholic' in religion:
                        copyr = religion.replace("catholic", "imperial")
                        lines[religionnum] = copyr
                        i = religionnum+1
                    elif 'orthodox' in religion:      
                        copyr = religion.replace("orthodox", "imperial") 
                        lines[religionnum] = copyr
                        i = religionnum+1



    with open(file.name, 'w') as f:
       f.writelines(["%s" % line  for line in lines])
                



