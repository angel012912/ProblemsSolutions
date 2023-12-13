def lengthOfLongestSubstring(s: str) -> int:
    # Inicializo un diccionario con los caracteres vistos y su respectivo
    # indice
    charsVisited = {}
    # Inicializar la variable que va a contener la cantidad maxima de
    # caracteres de un substring
    subStringMaxLen = 0
    # Se inicializa una variable que apunte al character izq
    leftPointer = 0
    # Recorrer el array
    for index in range(len(s)):
        # Se evalua si el character esta en el diccionario
        if s[index] in charsVisited:
            # Si el valor del indice del character es mayor al indice del
            # apuntador izq, se actualiza el apuntador izq
            if charsVisited[s[index]] >= leftPointer:
                leftPointer = charsVisited[s[index]] + 1
            # Actualizar el valor del indice del char dentro del
            # diccionario
            charsVisited[s[index]] = index
        else:
            # Si no está, agregar el character con su indice como valor
            # dentro del diccionario
            charsVisited[s[index]] = index
        # Actualizar el valor de subStringMaxLen
        subStringMaxLen = max(subStringMaxLen, (index - leftPointer)+1)
    # Regresar el valor que indica el mayor subString posible encontrado
    return subStringMaxLen


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abba"))
