from colorama import Fore
import admin.terminales.main as tm
import admin.main as mn

def menuAdmin():

    while True:
        print('=====================')
        print("ELEGIR UNA OPCION")
        print('=====================')
        print('1. MANTENIMIENTO DE TERMINALES')
        print('2. MANTENIMIENTO DE UNIDADES')
        print('3. MANTENIMIENTO DE RUTAS')
        print('4. REPORTES')
        print('5. SALIR')
        option = int(input("Ingrese una opción 1 - 2 - 3 - 4 - 5 \n" ))
        if option<0 and option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
            print(Fore.RED,"PORFAVOR INGRESE UN VALOR CORRECTO",Fore.RESET)
            # menuAdmin()
            mn.menuAdmin()
        elif option == 1:
            # mantTerminales()
            tm.mantTerminales()
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            break

