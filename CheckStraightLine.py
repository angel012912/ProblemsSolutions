class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # Se recorre el array de coordenadas
        prevM = None
        # Estas banderas se ocupan para identificar si hubo una linea
        # previamente vertical o horizontal
        vertical = False
        horizontal = False
        for coordinateIndex in range(0, len(coordinates)):
            # Si es la primera iteracion no hay nada que evaluar
            if coordinateIndex == 0:
                continue
            # Se definen en variables las coordenadas actuales
            actualXCoordinate = coordinates[coordinateIndex][0]
            actualYCoordinate = coordinates[coordinateIndex][1]
            # Se obtienen las coordenadas de la iteracion en variables
            prevXCoordinate = coordinates[coordinateIndex - 1][0]
            prevYCoordinate = coordinates[coordinateIndex - 1][1]
            # Se obtienen las diferencias de las actuales menos las previas
            yAxisDifference = actualYCoordinate - prevYCoordinate
            xAxisDifference = actualXCoordinate - prevXCoordinate
            # Se previene el caso de dividir entre 0 para evitar
            # errores de ejecucion
            if yAxisDifference == 0 or xAxisDifference == 0:
                # Se evaluan los casos en donde puede ser una linea
                # vertical recta
                if prevM is not None and prevM != 0:
                    return False
                if yAxisDifference == 0 and xAxisDifference != 0:
                    if horizontal:
                        return False
                    vertical = True
                    prevM = 0
                    continue
                elif xAxisDifference == 0 and yAxisDifference != 0:
                    if vertical:
                        return False
                    horizontal = True
                    prevM = 0
                    continue
                # En este caso ambas coordenadas estan en el mismo punto
                else:
                    return False
            # Se verifica si la pendiente es igual al anterior
            m = yAxisDifference / xAxisDifference
            if prevM is None:
                prevM = m
                continue
            elif prevM == m:
                continue
            else:
                return False
        # Si se termino de recorrer quiere decir que si es recta
        return True


if __name__ == '__main__':
    solution = Solution()
    coordinates = [[0, 0], [0, 1], [0, -1]]
    print(solution.checkStraightLine(coordinates=coordinates))
