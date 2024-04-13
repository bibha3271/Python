try:
    with open("C:\\Users\\BIBHA\\Desktop\\Python\A.txt") as f2:
     with open("C:\\Users\\BIBHA\\Desktop\\Python\B.txt","w") as f3:
         for i in f2:
             f3.write(i)
except:
    print("File not available...please create first...!")  
else:
    f2.close()    
    print("File closed...!")      
