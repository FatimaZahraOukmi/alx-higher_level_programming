def matrix_mul(m_a, m_b):
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_columns_a = 0
    num_rows_b = 0

    # Check requirements for matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row_a in m_a:
        if type(row_a) != list:
            raise TypeError("m_a must be a list of lists")
        len_a = len(m_a[0])
        if row_a == []:
            raise ValueError("m_a can't be empty")
        if len_a != len(row_a):
            raise TypeError("each row of m_a must be of the same size")
        num_columns_a = len(row_a)
        for column_a in row_a:
            if type(column_a) != int and type(column_a) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row_b in m_b:
        if type(row_b) != list:
            raise TypeError("m_b must be a list of lists")
        len_b = len(m_b[0])
        if row_b == []:
            raise ValueError("m_b can't be empty")
        if len_b != len(row_b):
            raise TypeError("each row of m_b must be of the same size")
        num_rows_b += 1
        for column_b in row_b:
            if type(column_b) != int and type(column_b) != float:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is possible
    if num_columns_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_a in m_a:
        current_row = []
        for j in range(len(m_b[0])):
            result = 0
            for i in range(len(row_a)):
                result += row_a[i] * m_b[i][j]
            current_row.append(result)
        mul_matrix.append(current_row)

    return mul_matrix
