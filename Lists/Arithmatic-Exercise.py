def verify_length(list_):
    count = 0
    for item in list_:
        count += 1
        if count > 5:
            return False
        else:
            True

def find_operants(equations):
    '''This function find operator, number 1 annd number 2'''
    for equation in equations:
        if equation.find('-')!=-1:
            operant = '-'
            operant_index =equation.find('-')
        elif equation.find('+')!=-1:
            operant = '+'
            operant_index = equation.find('+')
        else:
            print("Error: Operator must be '+' or '-'.")
            
        translate = str.maketrans({" ":""})
        translated_equation = equation.translate(translate)
        
        number_1 = translated_equation[0:operant_index:]
        number_2 = translated_equation[operant_index+1::]
        
        return number_1,operant,number_2

           
            
def main():
    equation_list = []
    while True:
        print('Enter an equation, in this format x +/ y:')
        equation = input()
        equation_list.append(equation)
        if verify_length(equation_list)==False:
            print('Error: Too many problems.')
            break
        find_operants(equations)

equations = ['5453+243', '345-45']
print(find_operants(equations))


        
        