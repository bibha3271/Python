try:
    f=open("C:\\Users\\BIBHA\\Desktop\\Python\B.txt","r")
    print(f.readline())
except:
    print("File not available...please create first...!")  
else:
    f.close()    
    print("File closed...!")      
