import time
import csv
import time
from DataStructures import array_list as al
from DataStructures import map_linear_probing as mp
from DataStructures import map_separate_chaining as sc

csv.field_size_limit(2147483647)


def new_logic():
    catalog = {
        "computers": al.new_list(),
        "gpu_model_map": mp.new_map(1000, 0.5),
        "form_factor_map": sc.new_map(1000, 2.0),
    }
    return catalog


def load_data(catalog, filename):
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            al.add_last(catalog["computers"], row)

            # Insertar en gpu_model_map (linear probing)
            gpu = row["gpu_model"]
            existing = mp.get(catalog["gpu_model_map"], gpu)
            if existing is None:
                new_lst = al.new_list()
                al.add_last(new_lst, row)
                mp.put(catalog["gpu_model_map"], gpu, new_lst)
            else:
                al.add_last(existing, row)

            # Insertar en form_factor_map (separate chaining)
            ff = row["form_factor"]
            existing2 = sc.get(catalog["form_factor_map"], ff)
            if existing2 is None:
                new_lst2 = al.new_list()
                al.add_last(new_lst2, row)
                sc.put(catalog["form_factor_map"], ff, new_lst2)
            else:
                al.add_last(existing2, row)

    return catalog

def get_time():
    return float(time.perf_counter() * 1000)

def delta_time(start, end):
    return float(end - start)

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
