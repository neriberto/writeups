with open('motivation!!!!!.txt', 'rb') as fp_in:
    reversed_data = fp_in.read()[::-1]
    with open('dump.png', 'wb') as fp_out:
        fp_out.write(reversed_data)
    
