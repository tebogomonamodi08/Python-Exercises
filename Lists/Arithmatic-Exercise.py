string = ' 43+ 354'
#TODO: extract number 1, operator, number 2 plus input correction
translate_object = str.maketrans({' ':''})
translated_string = string.translate(translate_object)

if string.find('+')!=-1:
    operator_index = string.find('+')
    operator = '+'
elif string.find('-')!=-1:
    operator_index = string.find('-')
    operator = '-'
else:
    print('Error: Operator must be '+' or '-'.')

number_1 = translated_string[0:operator_index-1:]
if len(number_1)==0:
    number_1=0
elif len(number_1)>4:
    print('Numbers cannot be more than four digits.')


number_2 = translated_string[operator_index:]
if len(number_2)==0:
    number_2=0
elif len(number_2)>4:
    print('Numbers cannot be more than four digits.')


#convert and return an answer.
if operator=='+':
    result=int(number_1)+int(number_2)
elif operator=='-':
    result=int(number_1)-int(number_2)
else:
    print('Error: Operator must be '+' or '-'.')
    
#diplay formatted text
print(f'{number_1:>6}\n{operator:>1}{number_2:>5}')
print('------')
print(f'{result:>6}')