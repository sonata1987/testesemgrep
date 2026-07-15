import os

# Esta função recebe o nome de um arquivo do usuário e lista suas informações.
def listar_info_arquivo(nome_arquivo):
    print(f"Buscando informações do arquivo: {nome_arquivo}...")
    
    # !!! VULNERABILIDADE AQUI !!!
    # Estamos concatenando a entrada do usuário diretamente no comando do sistema.
    # O ZAP rodaria algo como "ls -l filename.txt".
    # Mas se o usuário digitar "filename.txt; whoami", o sistema vai rodar "ls -l filename.txt" E DEPOIS o comando "whoami".
    os.system("ls -l " + nome_arquivo)

if __name__ == "__main__":
    # Simula a entrada de um usuário mal-intencionado
    # Entrada segura seria apenas: arquivo_usuario = "meu_documento.txt"
    arquivo_usuario = "vulneravel.py; whoami; cat /etc/passwd" 
    
    listar_info_arquivo(arquivo_usuario)
