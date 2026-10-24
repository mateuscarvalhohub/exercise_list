# 5. Tradutor de Códigos de Erro (Dict)
# Crie um dicionário fixo com 5 códigos de erro de servidor (ex: 404: "Not Found", 500:
# "Internal Server Error", etc.).
# ● Peça ao usuário um código.
# ● Se o código existir, exiba a mensagem.
# ● Se não existir, use um método do dicionário para retornar "Código de erro desconhecido" e
# adicione esse novo código ao dicionário com uma mensagem padrão definida pelo usuário.

error_codes = {
    404: "Not found",
    500: "Internal Server Error",
    401: "Unauthorized",
    503: "Service Unavailable",
    504: "Gateway Timeout"
}

while True:
    try:
        user_code = (input("Please, enter a code number: "))

        if "." in user_code or "," in user_code: 
            user_code = user_code.replace(".", "")                     
            user_code = user_code.replace(",", "")
        
        code = int(user_code)

        if code in error_codes:
            print(code, error_codes[code])
        else:
            default_unknow_code = error_codes.setdefault(code,"Unknown error code")

            print(default_unknow_code)

    except ValueError:
            print("Please, enter integer numbers only.")
    continue