#Delete file
import os
import shutil
path = "fodler"

try:
   #os.remove(path) #delete file #klasörü silmek için izin yok uyarısı verdi # tek dosyayı silebilir
   #os.rmdir(path)  #delete an empty directory   #klasörü sildi  #klasörün içinde başka bir dosya olduğunda silemez
   shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not permission to delere tahat")
except OSError:
    print("You cannot delete that using that function")


else:
    print(path+ "Was deleted")