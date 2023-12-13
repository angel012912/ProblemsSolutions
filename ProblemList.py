from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Hago un ciclo while para evaluar la condicion de que la lista contenga datos
        while prices:
            # Obtengo el valor minimo de la lista
            minValue = min(prices)
            # Obtengo el valor maximo de la lista
            maxValue = max(prices)
            # Obtengo el indice en el que se encuentra el valor minimo
            indexMin = prices.index(minValue)
            # Obtengo el indice en el que se encuentra el valor maximo
            indexMax = prices.index(maxValue)
            # Evaluo si el indice del valor minimo se encuentra antes del de el valor maximo
            if indexMin < indexMax:
                # Si se encuentra antes, entonces el resultado es la diferencia
                return maxValue - minValue
            # Si no se encuentra, se tiene que eliminar esos valores de la lista
            prices.pop(indexMin)
            # Se evalua que la lista de precios contenga mas de 2 valores
            if len(prices) > 1:
                prices.pop(indexMax)
        # Si se termina el ciclo, el resultado es 0
        return 0

Solution().maxProfit([7,1,5,3,6,4])