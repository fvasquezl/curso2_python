set_countries={'mex','col','per'} # inmutable
set_numbers={2,4,4,3,2,2} # {2,3,4}
set_from_string = set("hola")
set_from_tuple = set(('a','b','c','d','d'))
set_from_list = set([1,2,3,4,4])
print(set_countries)
print(set_numbers)
print(set_from_string)
print(set_from_tuple)
print(set_from_list) 
"""
    add(): Añade un elemento.
    update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
    discard(): Elimina un elemento y si ya existe no lanza ningún error.
    remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
    pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “ke
y error”.
    clear(): Elimina todo el contenido del conjunto.
"""
print('mex' in set_countries)
set_countries.update({'arg','bol'})  #modifica el set sin crear una copia
print(set_countries)
set_countries.discard('arg') 
print(set_countries)
set_countries.clear() 
print(len(set_countries))

"""
Operaciones set

    union(set): Realiza la operacion “union” entre dos conjuntos. La unión entre dos conjuntos es sumar 
        los elementos de estos sin repetir elementos. Esta operación tambien se puede realizar con el 
        signo “|”: set_a | set_b.
    
    intersection(set): Realiza la operacion “intersection” entre dos conjuntos. La intersección entre dos 
        conjuntos es tomar unicamente los elementos en común de los conjutnos. Esta operación tambien se 
        puede realizar con el signo “&”: set_a & set_b.
    
    difference(set): Realiza la operacion “difference” entre dos conjuntos. La diferencia entre dos conjuntos
        es restar los elementos del segundo conjunto al primero. Esta operación tambien se puede realizar 
        con el signo “-”: set_a - set_b.
    
    symmetric_difference(set): Realiza la operacion “symmetric_difference” entre dos conjuntos. 
        La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos 
        exceptuando el elemento en común. Esta operación tambien se puede realizar con el
        signo “^”: set_a ^ set_b.

NOTA: No se pueden realizar operaciones con otras colecciones de datos, solo se puede 
únicamente entre conjuntos.
"""

set_a ={'col','mex','bol'}
set_b={'pe','bol'}

set_c =set_a.union(set_b)
print(set_c)

set_c =set_a.intersection(set_b) # set_a & set_b
print(set_c)

set_c =set_a.difference(set_b) # set_a - set_b
print(set_c)

set_c =set_a.symmetric_difference(set_b) # set_a ^ set_b
print(set_c)


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set.update(countries,northAm,centralAm,southAm)


print(new_set)
