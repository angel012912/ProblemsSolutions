class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Se hace la excepcion para el caso base:
        if (len(strs) == 1):
            return strs[0]
        # Se ordena la lista lexicograficamente (abc < bac)
        sortedStrings = sorted(strs)
        # Se inicializa un string vacío donde se alamacenara el prefijo mas
        # largo
        longestPrefix = ""
        # Se recorre la palabra que sea de menor tamaño, unicamente comparando
        # la primera y la ultima del array ordenado
        for index in range(min(len(sortedStrings[0]), len(sortedStrings[-1]))):
            # Se evalua si el caracter de la iteracion es diferente
            if sortedStrings[0][index] != sortedStrings[-1][index]:
                # En dado caso devuelve lo que tenga la variable de
                # longestPrefix
                return longestPrefix
            # Se acumula el caracter que coincide
            longestPrefix += sortedStrings[0][index]
        # En dado caso que concluya el ciclo se regresa lo que tenga
        return longestPrefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
