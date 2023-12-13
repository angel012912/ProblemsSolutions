class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # O(n)
        # Declarar un profit maximo inicial de 0
        maxProfit = 0
        # Se define el costo minimo encontrado, inicialmente sería el primer
        # numero de la lista
        minCost = prices[0]
        # Se recorre la lista
        for price in prices:
            # Se evalua si el costo minimo encontrado es menor al precio actual
            if minCost < price:
                # En dado caso, se obtiene el profit actual
                actualProfit = price - minCost
                # Se reasigna el profit maximo
                maxProfit = max(actualProfit, maxProfit)
            else:
                # si el costo minimo no es menor, entonces tenemos que
                # actualizar el costo minimo
                minCost = price
        # Se regresa el maxProfit al terminar de recorrer el ciclo
        return maxProfit
        # O(n^2)
        # # Declaro un profit maximo inicial de 0
        # maxProfit = 0
        # # Recorro el array de precios
        # for priceIndex in range(len(prices)):
        #     # Por cada precio, recorro los precios restantes
        #     for nextPriceIndex in range(priceIndex + 1, len(prices)):
        #         # Se verifica que el valor del siguiente precio es mayor que
        #         # el actual y si esa diferencia es mayor al profit actual
        #         actualProfit = prices[nextPriceIndex] - prices[priceIndex]
        #         if actualProfit > maxProfit:
        #             # En dado caso se actualiza el valor del maxProfit
        #             maxProfit = actualProfit
        # # Cuando termina de iterar se regresa el valor del maxProfit
        # return maxProfit


if __name__ == '__main__':
    # Instancio la clase Solution
    solution = Solution()
    # Declaro una lista de numeros enteros
    prices = [2, 4, 1]
    # Muestro en pantalla el resultado de la funcion maxProfit
    print(solution.maxProfit(prices))
