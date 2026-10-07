import re
import math
expression = input("Write your mathematical expression: ")

# divede the expression in chuncks for avoind erros
tokens = re.findall(r'\d+\.?\d*|[+\-*/()^sS!]', expression)
output_queue = []
operator_stack = []
eval_stack = []


# Return operator priority level
def precedence_operation(current_token):

    if current_token == "!": return 4

    elif current_token == "^"  or current_token.upper() == "S": return 3

    elif current_token == "*" or current_token == "/": return 2

    elif current_token == "+" or current_token == "-": return 1

    else: return 0

# Return operation answer
def executing_operation(current_token, first_number, last_number):

    if current_token == "^": return first_number ** last_number

    elif current_token == "*": return first_number * last_number

    elif current_token == "/": return first_number / last_number

    elif current_token == "-": return first_number - last_number

    elif current_token == "+": return first_number + last_number

    else: return 0



for current_token in tokens:


# Send numbers straight to output
# temporarily remove the decimal point to verify float numbers
    if current_token.replace('.', '', 1).isdigit():

        output_queue.append(current_token)


    elif current_token == "(":

        operator_stack.append(current_token)

# Pop until matching open parenthesis is found

    elif current_token == ")":

        while operator_stack and operator_stack[-1] != "(":

            output_queue.append(operator_stack.pop())

        if operator_stack and operator_stack[-1] == "(": 

            operator_stack.pop()


#operator verification 


    elif precedence_operation(current_token) != 0: 

        while( operator_stack and precedence_operation(operator_stack[-1]) >= precedence_operation(current_token)):

            output_queue.append(operator_stack.pop())

        operator_stack.append(current_token)


# Move any remaining operators to the output
while operator_stack: 

    output_queue.append(operator_stack.pop())

# add the numbers to eval_stack.
for current_token in output_queue:
    if current_token.replace('.', '', 1).isdigit():
        eval_stack.append(float(current_token))

# Square root and factorial only need one number to work, so it's not necessary to call the function.    elif current_token.upper() == "S":
       
    elif current_token.upper() == "S":
        number = eval_stack.pop()
        eval_stack.append(math.sqrt(number))

    elif current_token == "!":
        number = eval_stack.pop()
        eval_stack.append((math.factorial(int(number))))

    else:
        last_number = eval_stack.pop()
        first_number = eval_stack.pop()

        eval_stack.append(executing_operation(current_token, first_number, last_number))

answer = eval_stack[0]
print(answer)