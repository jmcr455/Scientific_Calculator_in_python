import re
import math
import decimal

# Return operator priority level
def precedence_operation(current_token):
    if current_token == "!" or current_token.upper() in ("U", "P"): 
        return 4
    
    elif current_token == "^" or current_token.upper() in ("√", "R"): 
        return 3
    
    elif current_token == "*" or current_token == "/": 
        return 2
    
    elif current_token == "+" or current_token == "-": 
        return 1
    
    else: 
        return 0

# Return binary operation answer
def executing_operation(current_token, first_number, last_number):

    if  current_token.upper() == "R" or current_token =="√" : 
        if first_number == 0:
            return "root index cannot be zero"
        
        if last_number < 0:
            if first_number % 2 == 0:
                return "even roots don't support negative numbers"
            
        return last_number ** decimal.Decimal(decimal.Decimal(1) / first_number)
    
    elif current_token == "^": 
        return first_number ** last_number
    
    elif current_token == "*": 
        return first_number * last_number
    
    elif current_token == "/": 
        return first_number / last_number
    
    elif current_token == "-": 
        return first_number - last_number
    
    elif current_token == "+": 
        return first_number + last_number
    
    else: 
        return 0

# Return unary operation answer
def unary_operation(current_token, number):
    if current_token == "!": 
        if number < 0:
            return "factorial don't support negative numbers"
        
        return math.factorial(int(number))
    elif current_token.upper() == "U": 
        return -number
    elif current_token.upper() == "P": 
        return number

def calculator(expression):
    try:    
        clean_expr = expression.replace(" ", "")
        # Divide the expression into chunks (tokens) to avoid errors
        tokens = re.findall(r"\d+\.?\d*|[+\-*/()^rRUpP!√']", clean_expr)
        
        fixed_tokens = []
        for i, current_token in enumerate(tokens):
            if current_token.upper() in ("√", "R"):
                
                if i == 0 or not tokens[i - 1].replace('.', '', 1).isdigit():
                    fixed_tokens.append("2")
            fixed_tokens.append(current_token)

        tokens = fixed_tokens

        if not tokens:
            return "empty expression"

        # Correct identification of unary minus and plus without negative index error
        for i, current_token in enumerate(tokens):

            if current_token == "-":
                if i == 0 or tokens[i - 1] in "+-*/^rRUUP(√":
                    tokens[i] = "U"
                    
            elif current_token == "+":
                if i == 0 or tokens[i - 1] in "+-*/^rRUUP(√":
                    tokens[i] = "P"

        output_queue = []
        operator_stack = []
        eval_stack = []

        for current_token in tokens:
            # Send numbers straight to output queue
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

            # Operator verification
            else:
                p = precedence_operation(current_token)
                if p > 0:
                    while (operator_stack and operator_stack[-1] != "(" and 
                           precedence_operation(operator_stack[-1]) > p):
                        output_queue.append(operator_stack.pop())
                    operator_stack.append(current_token)

        # Move any remaining operators to the output
        while operator_stack: 
            output_queue.append(operator_stack.pop())

        # Add numbers to eval_stack and evaluate (RPN)
        for current_token in output_queue:
            if current_token.replace('.', '', 1).isdigit():
                eval_stack.append(decimal.Decimal(current_token))
            else:
                if current_token.upper() in ("!", "U", "P"):
                    number = eval_stack.pop()
                    eval_stack.append(unary_operation(current_token, number))
                else:
                    if len(eval_stack) < 2:
                        return "Invalid expression"
                    last_number = eval_stack.pop()  
                    first_number = eval_stack.pop()  
                    eval_stack.append(executing_operation(current_token, first_number, last_number))

        if not eval_stack:
            return "Invalid expression"

        answer = eval_stack[0]
        
        # Remove trailing decimals if it's a whole number
        if answer % 1 == 0:
            answer = int(answer)
        else:
            # Normalize to drop trailing zeros while keeping decimals if needed
            answer = answer.normalize()
            
        return answer
    
    except ValueError: 
        return "Invalid character"
    except ZeroDivisionError:
        return "it is impossible to divide by zero"
    except IndexError:
        return "Invalid expression"