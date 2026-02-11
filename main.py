import os
import shutil

def organize_files(main_folder):
    
    """
    Mengatur file di dalam folder utama berdasarkan ekstensinya.
    File akan dipindahkan ke subfolder yang sesuai.
    """
    
    # Mendefinisikan pemetaan folder dan mengenal target untuk setiap ekstensi file
    extension_folders = {
        '.gif': 'Images',
        '.jpeg': 'Images',
        '.jpg': 'Images',
        '.png': 'Images',
        '.bmp': 'Images',
        '.mp4': 'Video',
        '.MOV': 'Video',
        '.AVI': 'Video',
        '.zip': 'Compressed',
        '.rar': 'Compressed',
        '.mp3': 'Music',
        '.wav': 'Music',
        '.m4a': 'Music',
        '.pdf': 'Documents',
        '.pptx': 'Documents',
        '.ppt': 'Documents',
        '.xlsx': 'Documents',
        '.xlsm': 'Documents',
        '.docx': 'Documents',
        '.csv': 'Documents',
        '.exe': 'Programs',
        '.json': 'Programs',
        '.ini': 'System Files',
        '.cfg': 'System Files',
        '.msi': 'System Files',
        '.icc': 'System Files',
    }
    
    existing_folders = [folder.lower() for folder in os.listdir(main_folder) 
                        if os.path.isdir(os.path.join(main_folder, folder))]
    
    for item in os.listdir(main_folder):
        item_path = os.path.join(main_folder, item)
        
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            
            if ext in extension_folders:
                target_folder_name = extension_folders[ext]
                target_folder_path = os.path.join(main_folder, target_folder_name)
                
                if target_folder_name.lower() not in existing_folders:
                    os.makedirs(target_folder_path, exist_ok=True)
                    existing_folders.append(target_folder_name.lower())
                
                # Memindahkan file ke folder yang sesuai
                shutil.move(item_path, target_folder_path)
                print(f"Moved: '{item}' -> '{target_folder_name}'")
            else:
                print(f"Skipping: '{item}' (no folder mapping)")

main_folder_path = r"C:\Users\lenovo\OneDrive\Documents\Pictures\Screenshots" # Masukkan path folder utama di sini...

# Panggil fungsi untuk memulai pengorganisasian
organize_files(main_folder_path)