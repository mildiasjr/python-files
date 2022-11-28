import random, time
flag_ = True
flag_pedra = True
pedras_cantadas = []
pedra = 0

print("*** B  I  N  G  O ***\n")
inicia = input("Posso começar a chacoalhar o saco? (S/N): ")
print('\n')
inicia = inicia.upper()
if inicia == 'S':
    while flag_ == True:
        time.sleep(1)
        
        while flag_pedra == True:
            
            pedra = random.randint(1,99)
            
            if pedra in pedras_cantadas:
                pass
            else:
                flag_pedra = False
                pedras_cantadas.append(pedra)
                if pedra > 0 and pedra < 20:
                    print("Pedra: B", pedra,'\n')
                if pedra >= 20 and pedra < 40:
                    print("Pedra: I", pedra,'\n')
                if pedra >= 40 and pedra < 60:
                    print("Pedra: N", pedra,'\n')
                if pedra >= 60 and pedra < 80:
                    print("Pedra: G", pedra,'\n')
                if pedra >= 80 and pedra < 100:
                    print("Pedra: O", pedra,'\n')                
        cont = input("1 - Mais uma pedra  ::  2-Pedras já cantadas :: 3-Lista ordenada de pedras  :: 4-Sair ")
        if cont == '1':
            flag_pedra = True
        if cont == '2':
            print(pedras_cantadas,"\n")
            flag_pedra = False    
        if cont == '3':
            print(sorted(pedras_cantadas),"\n")
        if cont == '4':
            flag_ = False
        
