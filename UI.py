import sys
import os
from APIs.paper.version import *
from APIs.paper.color import *
import subprocess
def ascii_img():
        print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ")
        print("░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  ")
        print(Color.CYAN+f"[*-*] {Color.LIGHT_WHITE}=> {Color.RED}YOUTUBE : {Color .LIGHT_WHITE}https://www.youtube.com/@wne9838"+ Color.END)                                                  
        print(Color.CYAN+f"[*-*] {Color.LIGHT_WHITE}=> {Color.BLUE}FB : https://www.facebook.com/accngunghoatdongreal0"+ Color.END)  
def main():
        os.system("cls" if os.name == "nt" else "clear")
        ascii_img()
        print(f"<====================={Color.BLUE}[{Color.LIGHT_WHITE}Project{Color.BLUE}]{Color.END}========================>")
        Project = project_server()
        if(not Project):
            sys.exit(0)
        for i in range(len(Project)):
            print(f"[{Color.GREEN}PROJECT{Color.END}]{Color.LIGHT_WHITE} => {Color.END}{i+1} : {Color.LIGHT_WHITE}{Project[i]}")
        while True:
            try:
                Project_choose = int(input(f"[{Color.RED}+_+{Color.END}] => {Color.LIGHT_CYAN}Nhâp STT Của ProJect : {Color.END}"))
                if(Project_choose>0 and Project_choose < len(Project)+1):
                     break
            except KeyboardInterrupt:
                 sys.exit(0)
            except:
                pass
        os.system("cls" if os.name == "nt" else "clear")   
        ascii_img()
        print(f"<====================={Color.BLUE}[{Color.LIGHT_WHITE}Versions{Color.BLUE}]{Color.END}========================>")
        version_list = version_server(Project[Project_choose-1])  
        if(not version_list):
            sys.exit(0) 
        for i in range(len(version_list)):
            print(f"[{Color.GREEN}Versions{Color.END}]{Color.LIGHT_WHITE} => {Color.END}{i+1} : {Color.LIGHT_WHITE}{version_list[i]}") 
        while True:
            try:
                Version_choose = int(input(f"[{Color.RED}+_+{Color.END}] => {Color.LIGHT_CYAN}Nhâp STT Của versions : {Color.END}"))
                if(Version_choose>0 and Version_choose < len(version_list)+1):
                     break
            except KeyboardInterrupt:
                 sys.exit(0)
            except:
                pass 
        version_folder = download_version(Project[Project_choose-1],version_list[Version_choose-1])
        # jar_path = os.path.join(version_folder, "server.jar")
        if(not version_folder):
            sys.exit(0) 
        if(version_folder == "exists"):
            Java_path = input(rf"[{Color.LIGHT_CYAN}JAVA{Color.END}] {Color.LIGHT_WHITE}=> Nhập Java path (nếu dùng 2 bản Java) (Path/N) : {Color.END}")
            while True:
                try:
                    minRam = int(input(f"[{Color.RED}+_+{Color.END}] => {Color.LIGHT_CYAN}Nhâp Min Ram : {Color.END}"))
                    if(minRam>0):
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            while True:
                try:
                    maxRam = int(input(f"[{Color.RED}+_+{Color.END}] => {Color.LIGHT_CYAN}Nhâp max Ram : {Color.END}"))
                    if(maxRam>0 and maxRam>minRam):
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass    
            if Java_path == "N":
                java_exe = "java"
                try:
                    subprocess.run(['java', f'-Xms{minRam}G', f'-Xmx{maxRam}G', '-jar', 'server.jar', 'nogui'],cwd=version_folder,check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Lỗi khi chạy server: {e}")
                    sys.exit(1)
            else:
                Java_path = r"C:\Program Files\Java\jdk-21.0.2\bin"
                java_exe = os.path.join(Java_path, "java.exe")
                try:
                    subprocess.run([java_exe, f'-Xms{minRam}G', f'-Xmx{maxRam}G', '-jar', 'server.jar', 'nogui'],cwd=version_folder,check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Lỗi khi chạy server: {e}")
                    sys.exit(1)
        else:
            Java_path = input(rf"[{Color.LIGHT_CYAN}JAVA{Color.END}] {Color.LIGHT_WHITE}=> Nhập Java path (nếu dùng 2 bản Java) (Path/N) : {Color.END}")
            while True:
                try:
                    minRam = int(input(f"[{Color.RED}+_+{Color.END}] => {Color.LIGHT_CYAN}Nhâp Min Ram : {Color.END}"))
                    if(minRam>0):
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            while True:
                try:
                    maxRam = int(input(f"[{Color.RED}+_+{Color.END}] => {Color.LIGHT_CYAN}Nhâp max Ram : {Color.END}"))
                    if(maxRam>0 and maxRam>minRam):
                        break
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass    
            if Java_path == "N":
                java_exe = "java"
                try:
                    subprocess.run(['java', f'-Xms{minRam}G', f'-Xmx{maxRam}G', '-jar', 'server.jar', 'nogui'],cwd=version_folder,check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Lỗi khi chạy server: {e}")
                    sys.exit(1)
            else:
                Java_path = r"C:\Program Files\Java\jdk-21.0.2\bin"
                java_exe = os.path.join(Java_path, "java.exe")
                try:
                    subprocess.run([java_exe, f'-Xms{minRam}G', f'-Xmx{maxRam}G', '-jar', 'server.jar', 'nogui'],cwd=version_folder,check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Lỗi khi chạy server: {e}")
                    sys.exit(1)
            eula_fix(version_folder)
            print(f"{Color.LIGHT_WHITE}Đã Fix eula == true")
            file_path = os.path.join(version_folder, "server.properties")
            if not os.path.exists(file_path):
                print(f"[!] File '{file_path}' không tồn tại. Hãy chạy server Minecraft một lần để tạo file server.properties.")
                return
            properties = read_properties(file_path)
            if(not properties):
                sys.exit(0) 
            print(f"<====================={Color.BLUE}[{Color.LIGHT_WHITE}properties{Color.BLUE}]{Color.END}========================>")
            for key,value in properties.items():
                print(key+"="+value)
            while True:
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
            try:
                subprocess.run([java_exe, f'-Xms{minRam}G', f'-Xmx{maxRam}G', '-jar', 'server.jar', 'nogui'],cwd=version_folder,check=True)
            except subprocess.CalledProcessError as e:
                print(f"Lỗi khi chạy server: {e}")
                sys.exit(1)
main()