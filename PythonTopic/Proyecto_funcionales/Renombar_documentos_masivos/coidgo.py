import os  #this libreria es para trabajar con documentos
import shutil
def main():
    i = 0
    #ruta
    path = 'C:/Users/JUNIOR/Desktop/AprenderDev/PythonTopic/Proyecto_funcionales/Renombar_documentos_masivos/img_para_renombrar/'
    new_path = 'C:/Users/JUNIOR/Desktop/AprenderDev/PythonTopic/Proyecto_funcionales/Renombar_documentos_masivos/'
    for filename in  os.listdir(path):
        my_dest = "img" + str(i) + '.jpg'
        my_source =path + filename
        my_dest =path + my_dest
        #aqui renombrar los documento en la misma carpeta
        os.rename(my_source , my_dest)
        #este parte seria pasar a otra carpeta los archivo
        shutil.move(my_dest, new_path)
        i += 1
        
if __name__ == '__main__':
    main()
    
    
