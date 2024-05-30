import sys
import os

class SparseMatrix:
    def __init__(self, numRows=None, numCols=None, matrixFilePath=None):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = {}
        
        if matrixFilePath:
            self.load_from_file(matrixFilePath)

    def load_from_file(self, filePath):
        with open(filePath, 'r') as file:
            lines = file.readlines()
        
        self.numRows = int(lines[0].split('=')[1])
        self.numCols = int(lines[1].split('=')[1])
        
        for line in lines[2:]:
            line = line.strip()
            if line:
                if line[0] != '(' or line[-1] != ')':
                    raise ValueError("Input file has wrong format")
                
                parts = line[1:-1].split(',')
                if len(parts) != 3:
                    raise ValueError("Input file has wrong format")
                
                try:
                    row, col, value = int(parts[0]), int(parts[1]), int(parts[2])
                except ValueError:
                    raise ValueError("Input file has wrong format")
                
                self.set_element(row, col, value)
    
    def get_element(self, currRow, currCol):
        return self.elements.get((currRow, currCol), 0)
    
    def set_element(self, currRow, currCol, value):
        if value != 0:
            self.elements[(currRow, currCol)] = value
        elif (currRow, currCol) in self.elements:
            del self.elements[(currRow, currCol)]

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must be the same for addition")

        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value + other.get_element(row, col))
        
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, value)
        
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must be the same for subtraction")

        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value - other.get_element(row, col))
        
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, -value)
        
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions are not suitable for multiplication")

        result = SparseMatrix(self.numRows, other.numCols)
        for (row1, col1), value1 in self.elements.items():
            for col2 in range(other.numCols):
                value2 = other.get_element(col1, col2)
                if value2 != 0:
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)
        
        return result

    def to_file(self, filePath):
        with open(filePath, 'w') as file:
            file.write("rows={}\n".format(self.numRows))
            file.write("cols={}\n".format(self.numCols))
            for (row, col), value in self.elements.items():
                file.write("({}, {}, {})\n".format(row, col, value))

def main(matrix1_path, matrix2_path, result_dir):
    try:
        matrix1 = SparseMatrix(matrixFilePath=matrix1_path)
        matrix2 = SparseMatrix(matrixFilePath=matrix2_path)
    except Exception as e:
        print("Error loading matrices: {}".format(e))
        return

    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ").strip()
        
        if choice == '1':
            result = matrix1.add(matrix2)
            result_path = os.path.join(result_dir, 'sum.txt')
            result.to_file(result_path)
            print("Addition result saved to {}".format(result_path))
        elif choice == '2':
            result = matrix1.subtract(matrix2)
            result_path = os.path.join(result_dir, 'difference.txt')
            result.to_file(result_path)
            print("Subtraction result saved to {}".format(result_path))
        elif choice == '3':
            result = matrix1.multiply(matrix2)
            result_path = os.path.join(result_dir, 'product.txt')
            result.to_file(result_path)
            print("Multiplication result saved to {}".format(result_path))
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <matrix1_file_path> <matrix2_file_path> <result_directory>")
        sys.exit(1)
    
    matrix1_path = sys.argv[1]
    matrix2_path = sys.argv[2]
    result_dir = sys.argv[3]
    
    if not os.path.isdir(result_dir):
        print("Error: {} is not a directory or does not exist.".format(result_dir))
        sys.exit(1)
    
    main(matrix1_path, matrix2_path, result_dir)
