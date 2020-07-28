one_x_cubed = (1, 3)
two_x_squared = (2, 2)
def find_term_derivative(term):
    result=(term[0]*term[1],term[1]-1)
    return result
print(find_term_derivative(one_x_cubed))
print(find_term_derivative(two_x_squared))
four_x_cubed_minus_three_x = [(4, 3), (-3, 1)]
def find_derivative(function_terms):
    res=list(map(lambda function_term: find_term_derivative(function_term),function_terms))
    return list(filter(lambda res:res[0]!=0,res))
print(find_derivative(four_x_cubed_minus_three_x))
three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
print(find_derivative(three_x_squared_minus_eleven))
def derivative_at(terms, x):
    derivative_fn = find_derivative(terms)
    total = 0
    for term in derivative_fn:
        total += term[0]*x**term[1]
    return total
print(derivative_at(three_x_squared_minus_eleven,2))
#def tangent_line(function_terms, x_value, line_length = 4):
    #x_minus = x_value - line_length
    x_plus = x_value + line_length
    y = output_at(function_terms, x_value)
    ## here, we are using your function
    deriv = derivative_at(function_terms, x_value)
    y_minus = y - deriv * line_length
    y_plus = y + deriv * line_length
    return {'x': [x_minus, x_value, x_plus], 'y': [y_minus, y, y_plus]}
from graph import plot
from plotly.offline import iplot, init_notebook_mode

from calculus import derivative_trace, function_values_trace

init_notebook_mode(connected=True)


tangent_at_five_trace = tangent_line(three_x_squared_minus_eleven, 5, line_length = 4)
three_x_squared_minus_eleven_trace = function_values_trace(three_x_squared_minus_eleven, list(range(-10, 10)))
plot([three_x_squared_minus_eleven_trace, tangent_at_five_trace])