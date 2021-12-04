import numpy as np

arr = np.array([[1,2,3,14],
                [4,5,6,15],
                [7,8,9,16]])

class solution:
    def rotate(self, matrix):
        new_matrix = np.zeros((matrix.shape[1], matrix.shape[0]))
        height, width = matrix.shape
        for row in range(height):
            for col in range(width):
                new_matrix[col,height-row-1] = matrix[row,col]
        return new_matrix

if __name__ == "__main__":
    s = solution()
    new_matrix = s.rotate(arr)
    print("顺时针旋转90度后的矩阵为:")
    print(new_matrix)
