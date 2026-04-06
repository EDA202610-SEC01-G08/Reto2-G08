import sys
import App.logic as logic
from DataStructures import array_list as al
from DataStructures import map_linear_probing as mp

def new_logic():
    return logic.new_logic()


def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    filename = input("Ingrese el nombre del archivo (ej: computer_prices_10): ")
    filepath = "Data/" + filename + ".csv"
    start = logic.get_time()
    logic.load_data(control, filepath)
    end = logic.get_time()
    print("Datos cargados exitosamente")
    print("Total registros:", al.size(control["computers"]))
    print("Tiempo de carga:", logic.delta_time(start, end), "ms")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    if id < 1 or id > al.size(control["computers"]):
        print("ID inválido")
        return
    
    computer = al.get_element(control["computers"], id)
    print("\n" + "="*80)
    print(f"Tipo de dispositivo: {computer['device_type']}")
    print(f"Marca: {computer['brand']}")
    print(f"Modelo: {computer['model']}")
    print(f"Sistema operativo: {computer['os']}")
    print(f"Factor de forma: {computer['form_factor']}")
    print(f"Marca del procesador: {computer['cpu_brand']}")
    print(f"Modelo del procesador: {computer['cpu_model']}")
    print(f"Memoria RAM: {computer['ram_gb']} GB")
    print(f"Tipo de almacenamiento: {computer['storage_type']}")
    print(f"Capacidad de almacenamiento: {computer['storage_gb']} GB")
    print(f"Precio: ${computer['price']}")
    print("="*80 + "\n")

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    print("\n" + "="*80)
    print("REQ 1: Consultar equipos por marca y factor de forma")
    print("="*80)
    
    brand = input("Ingrese la marca del equipo (ej: HP, Lenovo, Dell): ")
    form_factor = input("Ingrese el factor de forma (ej: ATX, Gaming): ")
    
    result = logic.req_1(control, brand, form_factor)
    
    print("\n" + "-"*80)
    print(f"Tiempo de ejecución: {result['execution_time']:.2f} ms")
    print(f"Total de equipos encontrados: {result['total_count']}")
    print(f"Promedio de precios: ${result['average_price']:.2f}")
    print("-"*80)
    
    if result['total_count'] == 0:
        print("\nNo se encontraron equipos con los criterios especificados.")
    else:
        if result['total_count'] > 20:
            print(f"\nMostrando los primeros 10 y últimos 10 de {result['total_count']} equipos:\n")
        else:
            print(f"\nMostrando los {result['total_count']} equipos encontrados:\n")
        
        for idx, computer in enumerate(result['computers'], 1):
            print(f"\n{'─'*80}")
            print(f"Equipo #{idx}")
            print(f"{'─'*80}")
            print(f"  Tipo de dispositivo:        {computer['device_type']}")
            print(f"  Modelo:                     {computer['model']}")
            print(f"  Sistema operativo:          {computer['os']}")
            print(f"  Marca del procesador:       {computer['cpu_brand']}")
            print(f"  Memoria RAM:                {computer['ram_gb']} GB")
            print(f"  Capacidad de almacenamiento: {computer['storage_gb']} GB")
            print(f"  Precio:                     ${computer['price']}")
        
        print("\n" + "="*80 + "\n")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    gpu_model = input("Ingrese el modelo de GPU con espacio antes de los ultimos 2 digitos (ej: RTX 40 90): ")
    brand = input("Ingrese la marca del equipo (ej: Dell): ")
    n = int(input("Ingrese el número de equipos a listar (N): "))
    test = mp.get(control["gpu_model_map"], gpu_model)
    if test is not None:
            print("Equipos con ese GPU:", al.size(test))
            print("Ejemplo brand:", al.get_element(test, 1)["brand"])
    else:
        print("GPU model no encontrado en el mapa")
    
    start = logic.get_time()
    result, total = logic.req_3(control, gpu_model, brand, n)
    end = logic.get_time()
    
    print("\nTiempo de ejecución:", logic.delta_time(start, end), "ms")
    print("Total equipos encontrados:", total)
    
    if result is None or al.size(result) == 0:
        print("No se encontraron equipos con esos criterios.")
        return
    
    avg_ram = 0
    for i in range(1, al.size(result) + 1):
        avg_ram += float(al.get_element(result, i)["ram_gb"])
    avg_ram = avg_ram / al.size(result)
    print("Promedio RAM:", avg_ram, "GB")
    
    print("\nTop", n, "equipos más costosos:")
    print("-" * 80)
    for i in range(1, al.size(result) + 1):
        c = al.get_element(result, i)
        print(f"  {i}. {c['model']}")
        print(f"     Tipo: {c['device_type']} | RAM: {c['ram_gb']} GB | Storage: {c['storage_gb']} GB")
        print(f"     GPU: {c['gpu_brand']} {c['gpu_model']} | Peso: {c['weight_kg']} kg")
        print(f"     Precio: ${c['price']}")
        print()


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print("\n" + "="*80)
    print("REQ 4: Precio promedio para combinación CPU Brand - GPU Model")
    print("="*80)
    
    cpu_brand = input("Ingrese la marca del CPU (ej: Intel, AMD): ")
    gpu_model = input("Ingrese el modelo del GPU (ej: RTX 40 50, RX 6000 60): ")
    
    result = logic.req_4(control, cpu_brand, gpu_model)
    
    print("\n" + "-"*80)
    print(f"Tiempo de ejecución: {result['execution_time']:.2f} ms")
    print(f"Total de computadores encontrados: {result['total_count']}")
    print("-"*80)
    
    if result['total_count'] == 0:
        print("\nNo se encontraron computadores con los criterios especificados.")
    else:
        print("\nESTADÍSTICAS PROMEDIO:")
        print(f"  Precio promedio:              ${result['average_price']:.2f}")
        print(f"  VRAM promedio:                {result['average_vram']:.2f} GB")
        print(f"  RAM promedio:                 {result['average_ram']:.2f} GB")
        print(f"  CPU Boost promedio:           {result['average_cpu_boost']:.2f} GHz")
        
        if len(result['top_2']) > 0:
            print("\n" + "="*80)
            print(f"LOS {len(result['top_2'])} COMPUTADORES MÁS COSTOSOS:")
            print("="*80)
            
            for idx, computer in enumerate(result['top_2'], 1):
                print(f"\n{'─'*80}")
                print(f"Computador #{idx}")
                print(f"{'─'*80}")
                print(f"  Modelo:           {computer['model']}")
                print(f"  Marca:            {computer['brand']}")
                print(f"  Año de lanzamiento: {computer['release_year']}")
                print(f"  CPU Model:        {computer['cpu_model']}")
                print(f"  Precio:           ${computer['price']}")
        
        print("\n" + "="*80 + "\n")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    print("\n" + "="*80)
    print("REQ 5: Top N equipos mejor equipados por marca y factor de forma")
    print("="*80)
    
    n = int(input("Ingrese el número de computadores a listar (ej: 3, 5, 10): "))
    year_initial = int(input("Ingrese el año de lanzamiento inicial (ej: 2019): "))
    year_final = int(input("Ingrese el año de lanzamiento final (ej: 2024): "))
    brand = input("Ingrese la marca (ej: HP, Lenovo, Dell): ")
    form_factor = input("Ingrese el factor de forma (ej: ATX, Gaming): ")
    
    result = logic.req_5(control, n, year_initial, year_final, brand, form_factor)
    
    print("\n" + "-"*80)
    print(f"Tiempo de ejecución: {result['execution_time']:.2f} ms")
    print(f"Total de computadores encontrados: {result['total_count']}")
    print(f"Computadores con procesador Intel: {result['intel_count']}")
    print(f"Computadores con procesador AMD: {result['amd_count']}")
    print("-"*80)
    
    if result['total_count'] == 0:
        print("\nNo se encontraron computadores con los criterios especificados.")
    else:
        if len(result['top_n']) > 0:
            print(f"\n{'='*80}")
            print(f"TOP {len(result['top_n'])} COMPUTADORES MEJOR EQUIPADOS:")
            print(f"{'='*80}")
            
            for idx, computer in enumerate(result['top_n'], 1):
                print(f"\n{'─'*80}")
                print(f"Computador #{idx}")
                print(f"{'─'*80}")
                print(f"  Tipo de dispositivo:  {computer['device_type']}")
                print(f"  Modelo:               {computer['model']}")
                print(f"  Memoria RAM:          {computer['ram_gb']} GB")
                print(f"  CPU Boost:            {computer['cpu_boost_ghz']} GHz")
                print(f"  Precio:               ${computer['price']}")
                print(f"  Año de lanzamiento:   {computer['release_year']}")
                print(f"  Marca de CPU:         {computer['cpu_brand']}")
                print(f"  Modelo de CPU:        {computer['cpu_model']}")
        
        print("\n" + "="*80 + "\n")


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
