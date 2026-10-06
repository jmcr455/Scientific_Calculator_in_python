import re
expression = input("Write your mathematical expression: ")

# divede the expression in chuncks for avoind erros
tokens = re.findall(r'\d+\.?\d*|[+\-*/()]|[a-zA-Z]', expression)
output_queue = []
operator_stack = []


# Return operator priority level
def precedence_operation(token):

    if token == "*" or token == "/": return 2

    elif token == "+" or token == "-": return 1

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

        while( operator_stack and precedence_operation(operator_stack[-1]) >= precedence_operation(token)):

            output_queue.append(operator_stack.pop())

        operator_stack.append(current_token)


# Move any remaining operators to the output
while operator_stack: 

    output_queue.append(operator_stack.pop())

print(output_queue)
