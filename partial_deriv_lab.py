def three_x_y_at_one(x):
    return 3*x
def three_x_y_at_three(x):
    return 9*x

def three_x_y_at_six(x):
    return 18*x

def three_x_y_at_nine(x):
    return 27*x
print(three_x_y_at_one(3)) # 9
print(three_x_y_at_three(3))# 27
print(three_x_y_at_six(1)) # 18
print(three_x_y_at_six(2)) #36  
zero_to_ten = list(range(0, 11))
zero_to_four = list(range(0, 5))
def y_values_for_at_one(x_values):
    y_values=[]
    for x_value in x_values:
        y_value=x_value*3
        y_values.append(y_value)
    return y_values
def y_values_for_at_three(x_values):
    y_values=[]
    for x_value in x_values:
        y_value=x_value*9
        y_values.append(y_value)
    return y_values
def y_values_for_at_six(x_values):
    y_values=[]
    for x_value in x_values:
        y_value=x_value*18
        y_values.append(y_value)
    return y_values
def y_values_for_at_nine(x_values):
    y_values=[]
    for x_value in x_values:
        y_value=x_value*27
        y_values.append(y_value)
    return y_values
print(y_values_for_at_one(zero_to_four))
print(y_values_for_at_one(zero_to_ten))
print(y_values_for_at_three(zero_to_four)) # [0, 9, 18, 27, 36]
print(y_values_for_at_three(zero_to_ten)) # [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]

print(y_values_for_at_six(zero_to_four)) # [0, 18, 36, 54, 72]
print(y_values_for_at_six(zero_to_ten)) # [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180]

print(y_values_for_at_nine(zero_to_four)) # [0, 27, 54, 81, 108]
print(y_values_for_at_nine(zero_to_ten)) #[0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270]
def multivariable_output_at(list_of_terms, x_value, y_value):
    output = []
    for term in list_of_terms:
        constant = term[0]
        x_exponent = term[1]
        y_exponent = term[2]
        term_output = constant*x_value**x_exponent*y_value**y_exponent
        output.append(term_output)
    return sum(output)
four_x_squared_y_plus_three_x_plus_y = [(4, 2, 1), (3, 1, 0), (1, 0, 1)]
print(multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 2, 2))
print(multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 1, 1))
def term_df_dx(term):
    constant = term[0]*term[1]
    exponent = term[1] - 1
    return (constant, exponent,term[2]
def df_dx(list_of_terms):
    derivative_terms = list(map(lambda function_term: term_df_dx(function_term),list_of_terms))
    return list(filter(lambda derivative_term: derivative_term[0] != 0, derivative_terms))
def term_df_dy(term):
    constant = term[0]*term[2]
    exponent = term[2] - 1
    return (constant, term[1], exponent)
def df_dy(list_of_terms):
    derivative_terms = list(map(lambda function_term: term_df_dy(function_term),list_of_terms))
    return list(filter(lambda derivative_term: derivative_term[0] != 0, derivative_terms))   
two_x_cubed_y_plus_three_y_x_plus_x = [(2, 3, 1), (3, 1, 1), (1, 1, 0)]
df_dy(two_x_cubed_y_plus_three_y_x_plus_x) # [(2, 3, 0), (3, 1, 0)] 
