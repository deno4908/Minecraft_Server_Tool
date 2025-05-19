from curl_cffi import requests
from tqdm import tqdm
import os
import shutil
class Color():
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

def project_server():
    try:
        server_api = requests.get("https://api.papermc.io/v2/projects/").json()
        return server_api['projects']
    except Exception as e:
        print(e)
def version_server(project):
    try:
        server_api = requests.get(f"https://api.papermc.io/v2/projects/{project}").json()
        return server_api['versions']
    except Exception as e:
        print(e)
def download_version(project,version):
    try:
        GET_BUILD = requests.get(f"https://api.papermc.io/v2/projects/{project}/versions/{version}/builds").json()
        default_builds = [build["build"] for build in GET_BUILD["builds"] if build.get("channel") == "default"]
        LATEST_BUILD = default_builds[-1] if default_builds else None
        if LATEST_BUILD: 
            JAR_NAME = f"{project}-{version}-{LATEST_BUILD}.jar"
            version_folder = f"{project}-{version}-{LATEST_BUILD}"
            if os.path.exists(version_folder):
                print(f"[{Color.RED}!{Color.END}] {Color.LIGHT_WHITE}=> Thư mục '{version_folder}' đã tồn tại.{Color.END}")
                print(f"[{Color.YELLOW}1{Color.END}]{Color.LIGHT_WHITE} => Chạy server cũ{Color.END}")
                print(f"[{Color.YELLOW}2{Color.END}]{Color.LIGHT_WHITE} => Xóa server cũ chạy mới{Color.END}")
                while True:
                    choose = int(input(f"[{Color.GREEN}->-{Color.END}] {Color.LIGHT_WHITE}=> Nhập lựa chọn của bạn : {Color.END}"))
                    if(choose >0 and choose<=2):
                        break
                if(choose == 1):
                    return version_folder
                else:
                    shutil.rmtree(version_folder)
                    os.makedirs(version_folder, exist_ok=True)
                    save_path = os.path.join(version_folder, "server.jar")
                    server_api = requests.get(f"https://api.papermc.io/v2/projects/{project}/versions/{version}/builds/{LATEST_BUILD}/downloads/{JAR_NAME}",stream=True)
                    server_api.raise_for_status()
                    total = int(server_api.headers.get('content-length', 0))
                    with open(save_path, "wb") as f, tqdm(
                        desc="Tiến độ tải",
                        total=total,
                        unit='B',
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in server_api.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                bar.update(len(chunk))

                    print("✅ Tải hoàn tất!")
                    print("Kích thước file tải về:", os.path.getsize(save_path), "bytes")
                    return version_folder
               
                    
            else:
                os.makedirs(version_folder, exist_ok=True)
                save_path = os.path.join(version_folder, "server.jar")
                server_api = requests.get(f"https://api.papermc.io/v2/projects/{project}/versions/{version}/builds/{LATEST_BUILD}/downloads/{JAR_NAME}",stream=True)
                server_api.raise_for_status()
                total = int(server_api.headers.get('content-length', 0))
                with open(save_path, "wb") as f, tqdm(
                    desc="Tiến độ tải",
                    total=total,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for chunk in server_api.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            bar.update(len(chunk))

                print("✅ Tải hoàn tất!")
                print("Kích thước file tải về:", os.path.getsize(save_path), "bytes")
                return version_folder
        else:
            print("Không tìm thấy bản build ! ")
    except Exception as e:
        print(e)

def eula_fix(path):
    file_path = os.path.join(path, "eula.txt")
    if not os.path.exists(file_path):
        print(f"[!] File '{file_path}' không tồn tại. Hãy chạy server Minecraft một lần để tạo file eula.txt.")
        return
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if "eula=false" in line.lower():
                file.write("eula=true\n")
            else:
                file.write(line)
def read_properties(file_path):
    properties = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                properties[key.strip()] = value.strip()
    return properties 
def write_properties(file_path, properties):
    with open(file_path, "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")   
def display_properties(file_path):
    properties = read_properties(file_path)
    while True:
        print("\nCác thiết lập hiện tại:")
        for key, value in properties.items():
            print(f"{key} = {value}")
        print("\nBạn muốn sửa mục nào? (Nhập 'exit' để thoát)")
        key_to_edit = input("Key: ").strip()
        if key_to_edit.lower() == "exit":
            break
        if key_to_edit not in properties:
            print("Key không tồn tại. Vui lòng thử lại.")
            continue
        new_value = input(f"Nhập giá trị mới cho '{key_to_edit}': ").strip()
        properties[key_to_edit] = new_value
        print(f"Đã cập nhật {key_to_edit} = {new_value}")
    write_properties(file_path, properties)
    print(f"\nĐã lưu thay đổi vào '{file_path}'.")
