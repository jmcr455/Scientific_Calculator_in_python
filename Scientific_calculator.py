import re
import math
import decimal

def calculator(expression):
    
    try:    
        # divede the expression in chuncks for avoind erros
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()^sS!]', expression)
        if not tokens:
            return "empty expression or invalid characters"
        
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
        def executing_operation(current_token, first_number, last_number=None):

            if current_token == "!": return (math.factorial(int(first_number)))

            if current_token.upper() == "S": return first_number ** decimal.Decimal(1/last_number)

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


            else:
                # Correct operator precedence check
                p = precedence_operation(current_token)
                if p > 0:
                    while (operator_stack and operator_stack[-1] != "(" and precedence_operation(operator_stack[-1]) >= p):
                        output_queue.append(operator_stack.pop())
                    operator_stack.append(current_token)


        # Move any remaining operators to the output
        while operator_stack: 

            output_queue.append(operator_stack.pop())

        # add the numbers to eval_stack.
        for current_token in output_queue:
            if current_token.replace('.', '', 1).isdigit():
                eval_stack.append(decimal.Decimal(current_token))


            else:


                if current_token != "!":
                    last_number = eval_stack.pop()
                    first_number = eval_stack.pop()
                    eval_stack.append(executing_operation(current_token, first_number, last_number))

                else:
                    number = eval_stack.pop()
                    eval_stack.append(executing_operation(current_token, number))
                

        answer = eval_stack[0]
        
        # Remove trailing decimals if it's a whole number
        if answer % 1 == 0:
            answer = int(answer)
        else:
            # Normalize to drop trailing zeros while keeping decimals if needed
            answer = answer.normalize()
            
        return answer
    
    except ValueError: return "you use a invalide character"
    
    except ZeroDivisionError: return "it is imposible divide by zero"

    except IndexError:   return "it is imposible acess a number that does not exist"
