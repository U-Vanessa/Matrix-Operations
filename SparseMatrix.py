class SparseMatrix:
    def __init__(self, numRows=None, numCols=None, matrixFilePath=None):
        if matrixFilePath:
            self.load_from_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.elements = {}

    def load_from_file(self, matrixFilePath):
        self.elements = {}
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()
            self.numRows = int(lines[0].split('=')[1])
            self.numCols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                line = line.strip()
                if line:
                    try:
                        row, col, value = map(int, line.strip('()').split(','))
                        if row >= self.numRows or col >= self.numCols:
                            raise ValueError("Matrix entry out of bounds")
                        self.elements[(row, col)] = value
                    except ValueError:
                        raise ValueError("Input file has wrong format")

    def getElement(self, row, col):
        return self.elements.get((row, col), 0)

    def setElement(self, row, col, value):
        if row >= self.numRows or col >= self.numCols:
            raise ValueError("Matrix entry out of bounds")
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.elements.items():
            result.setElement(row, col, value + other.getElement(row, col))
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.setElement(row, col, value)
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.elements.items():
            result.setElement(row, col, value - other.getElement(row, col))
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.setElement(row, col, -value)
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(self.numRows, other.numCols)
        for (row1, col1), value1 in self.elements.items():
            for col2 in range(other.numCols):
                value2 = other.getElement(col1, col2)
                if value2 != 0:
                    result.setElement(row1, col2, result.getElement(row1, col2) + value1 * value2)
        return result

    def write_to_file(self, filepath, operation, other, result):
        with open(filepath, 'w') as file:
            file.write(f"{operation} result of matrices from {filepath} and {other}:\n")
            for (row, col), value in result.elements.items():
                file.write(f"({row}, {col}, {value})\n")

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: python SparseMatrix.py <operation> <matrix_file_1> <matrix_file_2>")
        return

    operation = sys.argv[1].lower()
    file1 = sys.argv[2]
    file2 = sys.argv[3]

    matrix1 = SparseMatrix(matrixFilePath=file1)
    matrix2 = SparseMatrix(matrixFilePath=file2)

    if operation == 'add':
        result = matrix1.add(matrix2)
        operation_name = "Addition"
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
        operation_name = "Subtraction"
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
        operation_name = "Multiplication"
    else:
        print("Invalid operation. Choose from add, subtract, multiply.")
        return

    result.write_to_file('results.txt', operation_name, file2, result)
    print(f"{operation_name} result written to results.txt")

if __name__ == "__main__":
    main()
