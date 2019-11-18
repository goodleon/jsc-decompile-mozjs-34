#coding=utf-8  
import os,sys  
  
print(sys.path[0])

file_path = []        
def getNameList(dir,wildcard,recursion):  
    exts = wildcard.split(" ")  
    files = os.listdir(dir)  
    for name in files:  
        fullname = os.path.join(dir,name)  
        if os.path.isdir(fullname) & recursion:  
            getNameList(fullname,wildcard,recursion)  
        else:  
            for ext in exts:  
                if(name.endswith(ext)):  
                    file_path.append(fullname)  
                    print("wcx "+fullname)  
                    break  
          
def run():  
    getNameList(sys.path[0],".jsc .jsc",1)  
    file_name_list = file_path  
    for file_name in file_name_list:  
        a = file_name.find(".jsc")  
        if a <> -1:  
            cmd = "php jsc2js.php %s > %s.js"%(file_name,file_name)
            print cmd  
            #os.popen(cmd)  
            os.system(cmd)  

            cmd1 = "rm -rf %s"%(file_name)
            os.system(cmd1)  
            # print("wcx111->add file|    %s | %s"%(file_name,file_name))  
          
if __name__ == "__main__":  
    run()  
