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

def req_1(catalog, brand, form_factor):
    """
    Retorna el resultado del requerimiento 1
    Filtra equipos por marca y factor de forma
    """
    start_time = get_time()
    
    filtered_computers = al.new_list()
    
    computers_by_ff = sc.get(catalog["form_factor_map"], form_factor)
    
    if computers_by_ff is not None:
        for i in range(1, al.size(computers_by_ff) + 1):
            computer = al.get_element(computers_by_ff, i)
            if computer["brand"] == brand:
                al.add_last(filtered_computers, computer)
    
    total_count = al.size(filtered_computers)
    
    if total_count > 0:
        total_price = 0
        for i in range(1, total_count + 1):
            computer = al.get_element(filtered_computers, i)
            total_price += float(computer["price"])
        average_price = total_price / total_count
        
        def sort_criteria(comp1, comp2):
            price1 = float(comp1["price"])
            price2 = float(comp2["price"])
            if price1 > price2:
                return True
            elif price1 < price2:
                return False
            else:
                return comp1["model"] < comp2["model"]
        
        al.merge_sort(filtered_computers, sort_criteria)
        
        if total_count > 20:
            result_computers = filtered_computers["elements"][:10] + filtered_computers["elements"][-10:]
        else:
            result_computers = filtered_computers["elements"]
    else:
        average_price = 0
        result_computers = []
    
    end_time = get_time()
    execution_time = delta_time(start_time, end_time)
    
    return {
        "execution_time": execution_time,
        "total_count": total_count,
        "average_price": average_price,
        "computers": result_computers
    }


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


def req_4(catalog, cpu_brand, gpu_model):
    """
    Retorna el resultado del requerimiento 4
    Obtiene el precio promedio para una combinación CPU Brand - GPU Model
    """
    start_time = get_time()
    
    filtered_computers = al.new_list()
    
    computers_by_gpu = mp.get(catalog["gpu_model_map"], gpu_model)
    
    if computers_by_gpu is not None:
        for i in range(1, al.size(computers_by_gpu) + 1):
            computer = al.get_element(computers_by_gpu, i)
            if computer["cpu_brand"] == cpu_brand:
                al.add_last(filtered_computers, computer)
    
    total_count = al.size(filtered_computers)
    
    if total_count > 0:
        total_price = 0
        total_vram = 0
        total_ram = 0
        total_cpu_boost = 0
        
        for i in range(1, total_count + 1):
            computer = al.get_element(filtered_computers, i)
            total_price += float(computer["price"])
            total_vram += float(computer["vram_gb"])
            total_ram += float(computer["ram_gb"])
            total_cpu_boost += float(computer["cpu_boost_ghz"])
        
        average_price = total_price / total_count
        average_vram = total_vram / total_count
        average_ram = total_ram / total_count
        average_cpu_boost = total_cpu_boost / total_count
        
        def sort_criteria(comp1, comp2):
            price1 = float(comp1["price"])
            price2 = float(comp2["price"])
            if price1 > price2:
                return True
            elif price1 < price2:
                return False
            else:
                return float(comp1["weight_kg"]) < float(comp2["weight_kg"])
        
        al.merge_sort(filtered_computers, sort_criteria)
        
        top_2 = []
        for i in range(1, min(3, total_count + 1)):
            computer = al.get_element(filtered_computers, i)
            top_2.append({
                "model": computer["model"],
                "brand": computer["brand"],
                "release_year": computer["release_year"],
                "cpu_model": computer["cpu_model"],
                "price": computer["price"]
            })
    else:
        average_price = 0
        average_vram = 0
        average_ram = 0
        average_cpu_boost = 0
        top_2 = []
    
    end_time = get_time()
    execution_time = delta_time(start_time, end_time)
    
    return {
        "execution_time": execution_time,
        "total_count": total_count,
        "average_price": average_price,
        "average_vram": average_vram,
        "average_ram": average_ram,
        "average_cpu_boost": average_cpu_boost,
        "top_2": top_2
    }


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
