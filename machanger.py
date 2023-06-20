import subprocess
import optparse
import re

def obtener_argumentos():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interfaz", help="Elige una interfaz para cambiar su direccion MAC.")
    parser.add_option("-m", "--mac", dest = "nueva_mac", help="Elige una nueva direccion MAC para reemplazar la original.")
    (options, arguments) = parser.parse_args()
    if not options.interfaz:
        parser.error("[-] Selecciona una interfaz, usa -h o --help para mas informacion")
    elif not options.nueva_mac:
        parser.error("[-] Ingresa una nueva direccion MAC, usa -h o --help para mas informacion")
    return options

def cambiar_mac(interfaz, nueva_mac):
    print("")
    print("[+] Cambiando direccion MAC para " + interfaz + " a " + nueva_mac)
    print("")

    subprocess.call(["ifconfig", interfaz, "down"])
    subprocess.call(["ifconfig", interfaz, "hw", "ether", nueva_mac])
    subprocess.call(["ifconfig", interfaz, "up"])

def obtener_mac_actual(interfaz):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interfaz])
    buscar_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if buscar_mac:
        return buscar_mac.group(0)
    else:
        print(" ")
        print("[-] No se pudo leer la direccion MAC ingresada")

options = obtener_argumentos()

mac_actual = obtener_mac_actual(options.interfaz)

print('''
                               MACHANGER v.1 by: wh04m1                                                  
                       Cambia tu direccion MAC automaticamente                       
                             Elige tu lado y diviertete...                 
''')

print("Direccion MAC actual = " + str(mac_actual))

cambiar_mac(options.interfaz,options.nueva_mac)

mac_actual = obtener_mac_actual(options.interfaz)

if mac_actual == options.nueva_mac:
    print("[+] La direccion MAC a sido cambiada correctamente a " + mac_actual)
else:
    print("")
    print("[-] La direccion MAC no pudo ser cambiada")
