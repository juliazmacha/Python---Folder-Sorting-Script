# Folder Sorting Script

## Opis zadania
Wielu z nas posiada na pulpicie folder o nazwie "Do przejrzenia", gdzie gromadzimy różne pliki, ale niestety nigdy nie znajdujemy czasu, aby porządkować te chaos. Ten skrypt pomoże w uporządkowaniu tego folderu. Skrypt przyjmuje nazwę folderu jako argument wejściowy i sortuje pliki zgodnie z ich rozszerzeniami, umieszczając je w odpowiednich kategoriach.

## Instrukcje użytkowania
Aby skorzystać ze skryptu, uruchom go za pomocą polecenia:
```bash
python sort.py /ścieżka/do/folderu
```
Gdzie `/ścieżka/do/folderu` to ścieżka do folderu, który chcesz posortować.

## Funkcje skryptu
1. **Sortowanie plików:** Skrypt przegląda wszystkie pliki w podanym folderze, a następnie sortuje je według następujących kategorii:
   - Obrazy: JPEG, PNG, JPG, SVG (umieszczone w folderze "images")
   - Filmy: AVI, MP4, MOV, MKV (umieszczone w folderze "video")
   - Dokumenty: DOC, DOCX, TXT, PDF, XLSX, PPTX (umieszczone w folderze "documents")
   - Muzyka: MP3, OGG, WAV, AMR (umieszczone w folderze "audio")
   - Archiwa: ZIP, GZ, TAR (umieszczone w folderze "archives")
   - Nieznane rozszerzenia (pozostają w folderze głównym)

2. **Normalizacja nazw:** Skrypt zmienia nazwy wszystkich plików i folderów, usuwając znaki specjalne oraz transliterując polskie litery na ich odpowiedniki.

3. **Przetwarzanie folderów:** Skrypt rekurencyjnie przetwarza zagnieżdżone foldery, aby obejmować wszystkie poziomy katalogów.

4. **Usuwanie pustych folderów:** Puste foldery są automatycznie usuwane.

5. **Obsługa archiwów:** Zawartość archiwów po rozpakowaniu jest przenoszona do folderu o takiej samej nazwie (bez rozszerzenia) w folderze "archives".

## Funkcja normalize
Funkcja `normalize` jest odpowiedzialna za zmianę polskich liter na znaki podstawowe, zamianę innych liter na znak '_' oraz zachowanie wielkości liter po transliteracji.

## Kryteria akceptacji
- Nazwy wszystkich plików i folderów są zmieniane przy użyciu funkcji `normalize`.
- Rozszerzenia plików pozostają bez zmian.
- Puste foldery są usuwane.
- Skrypt ignoruje foldery "archives", "video", "audio", "documents", "images".
- Zawartość rozpakowanego archiwum jest przenoszona do podfolderu o tej samej nazwie w folderze "archives".
- Pliki o nieznanych rozszerzeniach pozostają bez zmian.

# Folder Sorting Script

## Task Description
Many of us have a folder on our desktop named "To Review," where we casually toss random files, never finding the time to finally organize it. This script aims to bring order to that chaos. It sorts files based on their extensions, placing them into specific categories. You can customize the script to fit your needs and scenarios.

## Usage Instructions
To use the script, run it with the following command:
```bash
python sort.py /path/to/folder
```
Where `/path/to/folder` is the path to the folder you want to organize.

## Script Features
1. **File Sorting:** The script scans all files in the specified folder and categorizes them into the following groups:
   - Images: JPEG, PNG, JPG, SVG (placed in the "images" folder)
   - Videos: AVI, MP4, MOV, MKV (placed in the "video" folder)
   - Documents: DOC, DOCX, TXT, PDF, XLSX, PPTX (placed in the "documents" folder)
   - Music: MP3, OGG, WAV, AMR (placed in the "audio" folder)
   - Archives: ZIP, GZ, TAR (placed in the "archives" folder)
   - Unknown extensions (remain in the main folder)

2. **Name Normalization:** The script changes the names of all files and folders, removing special characters and transliterating Polish letters to their counterparts.

3. **Folder Processing:** The script recursively processes nested folders to cover all directory levels.

4. **Removal of Empty Folders:** Empty folders are automatically removed.

5. **Archives Handling:** The contents of archives, when unpacked, are moved to a folder with the same name (without an extension) in the "archives" directory.

## `normalize` Function
The `normalize` function is responsible for changing Polish letters to basic characters, replacing other letters with '_', and maintaining letter case after transliteration.

## Acceptance Criteria
- Names of all files and folders are changed using the `normalize` function.
- File extensions remain unchanged.
- Empty folders are removed.
- The script ignores folders named "archives," "video," "audio," "documents," "images."
- The contents of unpacked archives are moved to a subfolder with the same name in the "archives" folder.
- Files with unknown extensions remain unchanged.
