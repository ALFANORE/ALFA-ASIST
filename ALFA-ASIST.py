import subprocess
import webbrowser
import os
import sys
def abrir_firefox():
    webbrowser.get('firefox').open_new_tab('https://chat.openai.com/')    
def servidor_ngrok():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', comando_ngrok])
comando_ngrok = "ngrok start --all"
def editar_servidor():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', comando])
comando = "cd /var/www/html/ && micro index.html"
def apache2_start():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', start_apache])
start_apache = "service apache2 start"
def apache2_stop():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', stop_apache])
stop_apache = "service apache2 stop"
def ssh_start():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', start_ssh])
start_ssh = "service ssh start"
def ssh_stop():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', stop_ssh])
stop_ssh = "service ssh stop"
def mysql_stop():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', stop_mysql])
stop_mysql = "service mysql stop"
def mysql_start():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', start_mysql])
start_mysql = "service mysql start"
def local():
    webbrowser.get('firefox').open_new_tab('localhost/')
def todos_procesos_start():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', start_procesos_todos])
start_procesos_todos = "service apache2 start && service ssh start && service mysql start"
def todos_procesos_stop():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', stop_procesos_todos])
stop_procesos_todos = "service apache2 stop && service ssh stop && service mysql stop"

#comenzar = "service apache2 start && exit && exit"
#menu
os.system("clear")
print("     ◢█  █◣")   
print("    ◢█◤  ◥█◣")
print("   ◢█◤    ◥█◣")
print("  ◢█◤      ◥█◣")
print(" ◢█◤        ◥█◣")
print(" █◤          ◥█") 
print("  ◢██████████◣ \n      ALFA")
inicio = input("\nDo you want use 'ALFA' ? [y/n]: ")
if inicio == 'y':
    os.system("clear")
    print("     ◢█  █◣")   
    print("    ◢█◤  ◥█◣")
    print("   ◢█◤    ◥█◣")
    print("  ◢█◤      ◥█◣")
    print(" ◢█◤        ◥█◣")
    print(" █◤          ◥█") 
    print("  ◢██████████◣ \n      ALFA")
    print("\033[31m1 ChatGPT\n2 SERVER NGROK\n3 EDIT SERVER\n4 SERVICES\n5 LOCALHOST WEB\n6 EXIT\n7 HELP")
    opcion = input("\nSELECT THE OPTION: \033[0m")

    # Ejecutar la opción seleccionada
    if opcion == '1':
        abrir_firefox()
    elif opcion == '2':
        servidor_ngrok()
    elif opcion == '3':
        editar_servidor()
    elif opcion == '4':
        os.system("clear")
        print("\033[31m1 APACHE2\n2 SSH\n3 MYSQL\n4 ALL SERVICES")
        opcion2=input("What [SERVICE] you want ?: \033[0m")
        if opcion2 == '1':
            if os.geteuid() != 0:
                os.system("clear")
                print("\033[91mYou need access root\033[0m")
                print("Press [ENTER] for exit") 
                code=input("")
                sys.exit(1)
            else:
                os.system("clear")
                election=input("you need [START] or [STOP] ?: ")
                if election == 'START':
                    apache2_start()
                elif election == 'STOP':
                    apache2_stop()
                else:
                    print("IS NOT A VALID OPTION")
        elif opcion2 == '2':
            if os.geteuid() != 0:
                os.system("clear")
                print("\033[91mYou need access root\033[0m")
                print("Press [ENTER] for exit") 
                code=input("")
                sys.exit(1)
            else:
                os.system("clear")
                election=input("you need [START] or [STOP] ?: ")
                if election == 'START':
                    ssh_start()
                elif election == 'STOP':
                    ssh_stop()
                else:
                    print("IS NOT A VALID OPTION")
        elif opcion2 == '3':
            if os.geteuid() != 0:
                os.system("clear")
                print("\033[91mYou need access root\033[0m")
                print("Press [ENTER] for exit") 
                code=input("")
                sys.exit(1)
            else:
                os.system("clear")
                election=input("you need [START] or [STOP] ?: ")
                if election == 'START':
                    mysql_start()
                elif election == 'STOP':
                    mysql_stop()
                else:
                    print("IS NOT A VALID OPTION")
        elif opcion2 == '4':
            if os.geteuid() != 0:
                os.system("clear")
                print("\033[91mYou need access root\033[0m")
                print("Press [ENTER] for exit") 
                code=input("")
                sys.exit(1)
            else:
                os.system("clear")
                election=input("you need [START] or [STOP] ?: ")
                if election == 'START':
                    todos_procesos_start()
                elif election == 'STOP':
                    todos_procesos_stop()
                else:
                    print("IS NOT A VALID OPTION")
    elif opcion == '5':
        local()
    elif opcion == '6':
        sys.exit(1)    
    elif opcion == '7':
        print("LOS SERVICIOS PARA NGROK SE ENCUENTRAN EN /home/~/.config/ngrok/ngrok.yml LO PUEDES EDITAR\n DE LA MANERA QUE TU NECESITES PARA AUTOMATIZAR LOS SERVICIOS")
    else: 
        print("EXIT")
        sys.exit(1)
