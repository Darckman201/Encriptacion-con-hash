import hashlib
def encriptar(metodo, texto):
    if metodo == '1':
        return hashlib.blake2b(texto.encode()).hexdigest()
    elif metodo == '2':
        return hashlib.blake2s(texto.encode()).hexdigest()
    elif metodo == '3':
        return hashlib.md5(texto.encode()).hexdigest()
    elif metodo == '4':
        return hashlib.sha1(texto.encode()).hexdigest()
    elif metodo == '5':
        return hashlib.sha224(texto.encode()).hexdigest()
    elif metodo == '6':
        return hashlib.sha256(texto.encode()).hexdigest()
    elif metodo == '7':
        return hashlib.sha384(texto.encode()).hexdigest()
    elif metodo == '8':
        return hashlib.sha3_224(texto.encode()).hexdigest()
    elif metodo == '9':
        return hashlib.sha3_256(texto.encode()).hexdigest()
    elif metodo == '10':
        return hashlib.sha3_384(texto.encode()).hexdigest()
    elif metodo == '11':
        return hashlib.sha3_512(texto.encode()).hexdigest()
    elif metodo == '12':
        return hashlib.sha512(texto.encode()).hexdigest()
    elif metodo == '13':
        d = int(input("Ingrese numero de bits para encriptar: "))
        return hashlib.shake_128(texto.encode()).hexdigest(d)
    elif metodo == '14':
        d = int(input("Ingrese numero de bits para encriptar: "))
        return hashlib.shake_256(texto.encode()).hexdigest(d)

def main():
    print('1.-blake2b'
        '\n','2.-blake2s' 
        '\n','3.-md5' 
        '\n','4.-shal' 
        '\n','5.-sha224' 
        '\n','6.-sha256' 
        '\n','7.-sha384' 
        '\n','8.-sha3_224'
        '\n','9.-sha3_256' 
        '\n','10.-sha3_384' 
        '\n','11.-sha3_512' 
        '\n','12.-sha512' 
        '\n','13.-shake_128' 
        '\n','14.-shake_256')
    metodo = input("Digite o metodo de encriptacion: ")
    texto = input("Ingrese un texto: ")
    encriptado = encriptar(metodo, texto)
    print("El texto encriptado es: ", encriptado)

if __name__ == "__main__":
    main()