# Matrix-Operations


This project implements a `SparseMatrix` class in Python, which provides functionalities to load sparse matrices from files, perform matrix operations (addition, subtraction, multiplication), and save the results to files. The matrices are represented in a space-efficient manner by storing only the non-zero elements.

## Features

- **Load Matrices Operations from File**: The `Matrix-Operations` class can load matrices from a file with a specific format.
- **Perform Matrix Operations**: Support for addition, subtraction, and multiplication of sparse matrices.
- **Save Results to File**: The results of matrix operations can be saved to a file in a readable format.

## Innovations and Unique Features

1. **Error Handling and Validation**
   The class includes comprehensive error handling and validation to ensure the input file format is correct, which helps in preventing runtime errors and ensures robust operation.
2. **Efficient Storage**
    Only non-zero elements are stored, which saves memory and makes operations more efficient, particularly for large sparse matrices.
3. **Modular and Reusable Code**
    The implementation is designed to be modular, making it easy to extend and reuse the code in other projects.
4. **Interactive Command-Line Interface**
    The script provides an interactive command-line interface for performing operations, making it user-friendly and easy to use.

## File Format

The input matrix files should follow this format:
rows=<number of rows>
cols=<number of columns>
(row, col, value)

rows= 3
cols= 3

(0, 0, 1)
(0, 1, 2)
(0, 2, 3)
(1, 0, 4)
(1, 1, 5)
(1, 2, 6)
(2, 0, 7)
(2, 1, 8)
(2, 2, 9)


## Usage

### Running the Script

To use the script, run the following command:

python script.py <matrix1_file_path> <matrix2_file_path> <result_directory>

# Interactive Operations

After running the script, you will be prompted to choose an operation:

1. Add
2. Subtract
3. Multiply
4. Exit
Enter choice (1/2/3/4):

Enter the number corresponding to the desired operation. The result will be saved in the specified result_directory with a filename corresponding to the operation (sum.txt, difference.txt, or product.txt).

# Installation
    1. Clone the Repository
    git clone https://github.com/your-username/Matrix-Operations.git
     cd Matrix-Operations

     2. Ensure Python is Installed
       Make sure you have Python 3 installed on your system.

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

This `README.md` provides a detailed overview of your project, instructions for using it, and highlights the innovations and unique features of your implementation.

# Author
# Vanessa UWONKUNDA

