def gera_token():
    from random import sample
    alfanuma = "ABCDEFGHIJKLM123456789NOPQRSTUVWXYZ" # Zero's been excluded to avoid confusion
    tokenl = []
    for x in range(5):              # Generates five blocks of 5 characters
        alfan5 = sample(alfanuma,5) # Generates list of 5 random characters from alfanuma string
        x = ''.join(alfan5)         # Transform alfan5 list in x string
        tokenl.append(x)            # Insert x string in tokenlist
    token = '-'.join(tokenl)        # Transform tokenlist in a string separated by '-' >> the final token
    return token

if __name__ == '__main__':
    token = gera_token()
    print(token)