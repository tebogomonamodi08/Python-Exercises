def main():
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    
    if verify_length(problems):
        formatted_problems = ''
        list_ = []
        for equation in problems:
            table = str.maketrans({" ":""})
            formatted_equation = equation.translate(table)
            operator, number_1, number_2 = find_operator(formatted_equation)
            #list_.append(find_operator(formatted_equation))
        #print(list_)
    
            if operant_verification(number_1,number_2):
                list_.append(formatter(operator,number_1,number_2))
        

                
            else:
                print('Error: Numbers cannot be more than four digits.')
    else:
        print('Error: Too many problems.')
    print(formatted_problems)





def verify_length(problems):
    return len(problems)<=5

def find_operator(equation):
    '''Finds the operator in an equation and the operants, output: tuple'''
    if equation.find('+')!=-1:
        operator_index = equation.find('+')
        operator = '+'
    elif equation.find('-')!=-1:
        operator_index = equation.find('-')
        operator = '-'
    else:
        operator='Error: Operator must be '+' or '-'.'

    number_1 = equation[0:operator_index:]
    number_2 = equation[operator_index+1::]
    
    return operator, number_1, number_2

def operant_verification(number_1,number_2):
    return (len(number_1)<4 or len(number_2)<4) and (number_1.isdigit() and number_2.isdigit())

def answer(operator, number_1, number_2):

    if operator=="+":
        return int(number_1)+int(number_2)
    else:
        return int(number_1)-int(number_2)
        
    

def formatter(operator,number_1,number_2):
    return f'{number_1:>5}\n{operator}{number_2:>4}\n-----'

def formatter_ans(operator,number_1,number_2):
    return f'{number_1:>5}\n{operator}{number_2:>4}\n-----\n{answer(operator,number_1,number_2):>5}'


    
    

if __name__ == '__main__':
    main()
