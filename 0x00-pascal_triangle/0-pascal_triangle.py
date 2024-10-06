def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        prev_row = triangle[-1]  # Last row in the triangle
        new_row = [1]  # First element of the new row is always 1
        
        # Generating the middle elements of the new row
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        new_row.append(1)  # Last element of the new row is always 1
        triangle.append(new_row)  # Add the new row to the triangle
    
    return triangle


