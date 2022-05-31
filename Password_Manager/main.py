from colorama import * #Libreria de colores en python
from tqdm import tqdm 
from time import sleep 
init(autoreset=True)
menu = ''
length = 3 #Las veces que se desplazara en la abecedario
def encriptado(data,length):
    encriptado = ''
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):#Letras mayusculas
            encriptado += chr((ord(char)+length-65)%26+65)#Operaciones para encontrar caracter buscado
        elif(char.islower()):#Letras minusculas
            encriptado += chr((ord(char)+length-97)%26+97)
        elif(char.isdigit()):#Numeros
            num = (int(char)+length)%10
            encriptado += str(num)
        else: #En caso de que sea demasiado largo
            encriptado += char
    return encriptado
def desencriptado(data,length):
    desencriptado = ''
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):#Letras mayusculas
            desencriptado += chr((ord(char)-length-65)%26+65)#Operaciones para encontrar caracter buscado
        elif(char.islower()):#Letras minusculas
            desencriptado += chr((ord(char)-length-97)%26+97)
        elif(char.isdigit()):#Numeros
            num = (int(char)-length)%10
            desencriptado += str(num)
        else: #En caso de que sea demasiado largo
            desencriptado += char
    return desencriptado
clave = encriptado('hola',length)
contraseña_intentos = 0
while menu != '1' or menu != '2' or menu != '3':
    #Función principal
    print(Style.BRIGHT + Fore.YELLOW + f"\nSUSAN PASSWORD MANAGER")
    print("-----------------------")
    print(Fore.GREEN+f'\n1) Nueva contraseña'+
        Fore.CYAN+f'\n2) Ver contraseñas guardadas'+
        Fore.RED+f'\n3) Borrar todo\t'+
        Fore.BLUE+f'\n4) Salir\t')
    menu = input()
    if menu == '1':
        #Opcciones segun el caso
        Name = input("Nombre del sitio \033 ")
        User = input("Nombre de usuario para este sitio \033 ")
        Passord = input("Contraseña para este sitio \033 ")
        #Abre un archivo para agregarlo o crea el archivo si no existe
        file = open('Basededatosdecontraseñas.txt','a')
        #Escribe en dicho documento
        file.write(encriptado(Name,length)+' | '+encriptado(User,length)+' | '+encriptado(Passord,length)+'\n')
        #Cierro el archivo para evitar problemas con cache/memoria
        file.close()
    elif(menu == '2'):
        while True:
            seguridad = str(input('Contraseña: '))
            if (seguridad == desencriptado(clave,length)):
                print(Fore.CYAN + f'\nCONTRASEÑAS GUARDADAS\n')
                file = open('Basededatosdecontraseñas.txt','r')
                print(Fore.MAGENTA+f'Sitio\t\t'+Fore.BLUE+f'Usuario\t\t'+Fore.RED+f'Contraseña')
                #Le ingreso un caracter para distingir
                for i in file:
                    data = i.split(' | ')
                    print(desencriptado(data[0],length)+'\t\t'+desencriptado(data[1],length)+'\t\t'+desencriptado(data[2],length))
                file.close()
                #Termino llamando la función para desencriptar mis datos mas una separación
                break
            else:
                if (contraseña_intentos > 1):
                    print(Fore.RED+f'DEMASIADOS INTENTOS ADIOS POPO!')
                    exit()
                else:
                    print(Fore.YELLOW+f'**CONTRASEÑA INCORRECTA**')
                    contraseña_intentos += 1
                    continue
    elif(menu == '3'):
        while True:
            seguridad = str(input('Contraseña: '))
            if (seguridad == desencriptado(clave,length)):
                #Simulación de croonometro
                for i in tqdm(range(0, 100), desc ="Borrando los datos"): 
                    sleep(.1) 
                file = open('Basededatosdecontraseñas.txt','w')
                file.write('')
                file.close()
                print(Fore.GREEN+f"Base de datos borrada")
                break
            else:
                if (contraseña_intentos > 1):
                    print(Fore.RED+f'DEMASIADOS INTENTOS ADIOS POPO!')
                    exit()
                else:
                    print(Fore.YELLOW+f'**CONTRASEÑA INCORRECTA**')
                    contraseña_intentos += 1
                    continue
    elif(menu == '4'):
        exit()