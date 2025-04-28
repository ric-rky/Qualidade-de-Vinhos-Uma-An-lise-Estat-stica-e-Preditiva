import os
import requests
import zipfile

def get_file(url: str, directory: str = "", unzip: bool = True, overwrite: bool = False):
    """
    Baixa um arquivo a partir de uma URL e opcionalmente descompacta se for um .zip.

    Parâmetros:
    - url (str): URL do arquivo a ser baixado.
    - directory (str): Caminho do diretório onde o arquivo será salvo.
    - unzip (bool): Se True, descompacta o arquivo caso seja um .zip.
    - overwrite (bool): Se True, baixa novamente mesmo que o arquivo já exista.

    Retorna:
    - str: Caminho do arquivo salvo.
    """
    try:
        os.makedirs(directory, exist_ok = True)
        file_name = url.split("/")[- 1]
        file_path = os.path.join(directory, file_name)

        if os.path.exists(file_path) and not overwrite:
            print(f"[INFO] Arquivo já existe: {file_path}.")
        else:
            print(f"[INFO] Baixando arquivo de: {url}.")
            response = requests.get(url)
            response.raise_for_status()  # Erro caso a resposta não seja 200
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Arquivo salvo em: {file_path}.")

        if unzip and file_name.endswith(".zip"):
            print("Extraindo arquivo zip...")
            with zipfile.ZipFile(file_path, 'r') as my_zip:
                my_zip.extractall(directory)
            print(f"Arquivos extraídos para: {directory}.")

        return file_path

    except Exception as e:
        print(f"[ERRO] Falha ao baixar ou extrair arquivo: {e}.")
        return None
