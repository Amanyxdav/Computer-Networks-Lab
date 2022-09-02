def crc(msg, div, code='000'):

    msg = msg + code

    # Convert msg and div into list form for easier handling
    msg = list(msg)
    div = list(div)

    # Loop over every message bit (minus the appended code)
    for i in range(len(msg)-len(code)):
        # If that messsage bit is 1, perform modulo 2 multiplication
        if msg[i] == '1':
            for j in range(len(div)):
                # Perform modulo 2 multiplication on each index of the divisor
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)

    # Output the last error-checking code portion of the message generated
    return ''.join(msg[-len(code):])


# TEST 1 ####################################################################
print('Test 1 ---------------------------')
# Use a divisor that simulates: x^3 + x + 1
div = '1011'
msg = '11010011101100'

print('Input message:', msg)
print('Divisor:', div)

# Enter the message and divisor to calculate the error-checking code
code = crc(msg, div)

print('Output code:', code)

# Perform a test to check that the code, when run back through, returns an
# output code of '000' proving that the function worked correctly
print('Success:', crc(msg, div, code) == '000')


# TEST 2 ####################################################################
print('Test 2 ---------------------------')
# Use a divisor that simulates: x^2 + 1
div = '0101'
msg = '00101111011101'

print('Input message:', msg)
print('Divisor:', div)

# Enter the message and divisor to calculate the error-checking code
code = crc(msg, div)

print('Output code:', code)

# Perform a test to check that the code, when run back through, returns an
# output code of '000' proving that the function worked correctly
print('Success:', crc(msg, div, code) == '000')