class Solution(object):
    def mergeArrays(self, nums1, nums2):
        
        # Convertir lista en diccionario.
        def lista_de_listas_en_diccionario(lista_de_listas):
            diccionario = {} #llave y valor (id,valor)
            for sublista in lista_de_listas: #recorrer cada sublista entre
                clave = sublista[0] #id
                valor = sublista[1] #valor
                diccionario[clave] = valor
            return diccionario
        
        diccionario1 = lista_de_listas_en_diccionario(nums1)
        diccionario2 = lista_de_listas_en_diccionario(nums2)
                
        resultado = {} #creamos otro diccionario c: 
        # Sumatoria de valores con la misma llave
        for key in diccionario1:  #clave en nums 1 ; id  matrices
            if key in diccionario2:
                resultado[key] = diccionario1[key] + diccionario2[key]  #iteracion por claves
                #print(diccionario1[clave])
                #print(diccionario2[clave])
            else:
                resultado[key] = diccionario1[key]
                #print(diccionario1[clave]) #el valor diferente de id en nums 1

        for key in diccionario2:
            if key not in diccionario1:
                resultado[key] = diccionario2[key]

        diccionario_ordenado = {k: resultado[k] for k in sorted(resultado)}
        lista_de_listas = [[clave, valor] for clave, valor in diccionario_ordenado.items()]
        #print(lista_de_listas)
        return lista_de_listas
    
    