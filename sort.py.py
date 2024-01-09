import os
import shutil

# Lista rozszerzeń dla różnych kategorii
file_categories = {
    'obrazy': ('JPEG', 'PNG', 'JPG', 'SVG'),
    'pliki wideo': ('AVI', 'MP4', 'MOV', 'MKV'),
    'dokumenty': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
    'muzyka': ('MP3', 'OGG', 'WAV', 'AMR'),
    'archiwa': ('ZIP', 'GZ', 'TAR')
}

# Funkcja do transliteracji polskich liter
def normalize(text):
    text = text.replace('ą', 'a').replace('ć', 'c').replace('ę', 'e')
    text = text.replace('ł', 'l').replace('ń', 'n').replace('ó', 'o')
    text = text.replace('ś', 's').replace('ż', 'z').replace('ź', 'z')
    text = text.replace('Ą', 'A').replace('Ć', 'C').replace('Ę', 'E')
    text = text.replace('Ł', 'L').replace('Ń', 'N').replace('Ó', 'O')
    text = text.replace('Ś', 'S').replace('Ż', 'Z').replace('Ź', 'Z')
    return ''.join(char if char.isalnum() else '_' for char in text)

# Funkcja do sortowania plików
def sort_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            file_extension = file_extension.lstrip('.').upper()
            new_name = normalize(file_name) + file_extension

            if file_extension in ('', '.'):
                # Ignoruj puste rozszerzenia
                continue

            found_category = False
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    found_category = True
                    category_folder = os.path.join(root, category)
                    if not os.path.exists(category_folder):
                        os.mkdir(category_folder)
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(category_folder, new_name)
                    shutil.move(old_file_path, new_file_path)
                    break

            if not found_category:
                # Nieznane rozszerzenie, pozostaw bez zmian
                pass

    # Usuń puste foldery
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Użycie: python sort.py C:\Users\Acer\Desktop\Balagan")
    else:
        folder_path = sys.argv[1]
        sort_files(folder_path)

