neighbors = [{'name': 'Fred', 'avenue': 4, 'street': 8}, {'name': 'Suzie', 'avenue': 1, 'street': 11},{'name': 'Bob', 'avenue': 5, 'street': 8}, {'name': 'Edgar', 'avenue': 6, 'street': 13}]
A=list(filter(lambda neighbor: neighbor['name']!='Fred',neighbors))
B=list(map(lambda neighbor: neighbor["avenue"] <=5,A))
print(A,B)
def term_ouput(term,input_value):
    return term[0]*input_value**term[1]
print(term_ouput((3,2),2))
def output_at(list_of_terms,x_value):
    res=list(map(lambda term:term_ouput(term,x_value),list_of_terms))
    return sum(res)
three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
print(output_at(three_x_squared_minus_eleven, 2)) 
print(output_at(three_x_squared_minus_eleven, 3))
def delta_f(list_of_terms,x_value,delta_x):
    result=output_at(list_of_terms,(x_value+delta_x))-output_at(list_of_terms,x_value)
    return result
four_x_plus_fifteen = [(4, 1), (15, 0)]
print(delta_f(four_x_plus_fifteen,2,1))