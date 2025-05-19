from curl_cffi import requests
from tqdm import tqdm
import os
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
