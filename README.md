## --EN--



# SkubnijLinka
### Final Project for CS50P
#### Description:

**Introduction and Project Objective**
My project is a Python-based application designed to download videos from YouTube in selected formats (MP3 or MP4). I created it to make downloading video materials easier for users
for educational purposes and to provide a secure tool for this purpose.

**File Structure and Functionality**
* **`project.py`**: The main program file. It contains the logic for validating user input (either via CLI arguments or interactive mode).
* **`test_project.py`**: A file containing unit tests written using the `pytest` library. It tests the correctness of every function in `project.py`.
* **`requirements.txt`**: Contains a list of required external libraries to install.
* **`cookies.txt`**: A file with browser session cookies that helps authorize requests to YouTube.

**How to prepare cookies?**
1. Install a browser extension for downloading cookies (I recommend: "Get cookies.txt LOCALLY").
2. Export cookies for YouTube to a file.
3. Save the file named `cookies.txt` in the program's root directory.

**Design Decisions**
During the program creation, I decided to separate link validation logic (`validate_url`) from input format checking logic (`validate_format`). This makes the code more readable and much easier to test using `pytest`. Using `monkeypatch` in CLI tests allowed for simulating command-line arguments without physically executing the script externally.

**System Requirements**
Before running the program, ensure that the following are installed on your system:
* Python (version 3.x)
* **FFmpeg** (required by `yt-dlp` to merge video and audio formats)
* **Node.js** (required to handle YouTube security scripts)

**How ​​to install (e.g., on Linux):**
* sudo apt update
* sudo apt install -y ffmpeg
* sudo apt install -y nodejs

**Installation**
1. Clone or download the project repository.
2. Install the required dependencies using the command:
   ```bash
   pip install -r requirements.txt
   ```

**Example Input:**
1. python project.py "https://www.youtube.com/watch?v=..." {mp3 or mp4} – remember to enclose the link in quotation marks
2. python project.py (arguments are entered while the program is running)

**Note**
* This project was created for educational purposes. The tool demonstrates how to download multimedia using Python. The user bears full responsibility for any failure to comply with copyright laws and YouTube's terms of service.



## --PL--



# SkubnijLinka
### Final Project for CS50P
#### Opis:

**Wstęp i Cel Projektu**
Mój projekt to aplikacja napisana w języku Python, służąca do pobierania filmów z YouTube w wybranych formatach (MP3 lub MP4). Stworzyłem ją po to, aby ułatwić użytkownikom pobieranie materiałów wideo w celach edukacyjnych oraz zapewnić im bezpieczne narzędzie do tego celu.

**Struktura Plików i Działanie**
* **`project.py`**: Główny plik programu. Zawiera logikę odpowiedzialną za walidację wejścia od użytkownika (można przekazać argumenty przez CLI lub korzystać z trybu interaktywnego).
* **`test_project.py`**: Plik zawierający testy jednostkowe napisane przy użyciu biblioteki `pytest`. Testuje on poprawność działania każdej funkcji zawartej w pliku `project.py`.
* **`requirements.txt`**: Zawiera listę wymaganych bibliotek zewnętrznych do zainstalowania.
* **`cookies.txt`**: Plik z ciasteczkami sesji przeglądarki, który pomaga w autoryzacji zapytań do YouTube.

**Jak przygotować ciasteczka?**
1. Zainstaluj w przeglądarce rozszerzenie do pobierania ciasteczek (polecam: "Get cookies.txt LOCALLY").
2. Wyeksportuj ciasteczka dla serwisu YouTube do pliku.
3. Zapisz plik pod nazwą `cookies.txt` w folderze głównym programu.

**Decyzje Projektowe**
Podczas tworzenia programu zdecydowałem się na rozdzielenie logiki walidacji linków (`validate_url`) od logiki sprawdzania formatu wejściowego (`validate_format`). Dzięki temu kod jest bardziej czytelny i znacznie łatwiejszy do przetestowania za pomocą `pytest`. Zastosowanie `monkeypatch` w testach CLI pozwoliło na symulowanie argumentów przekazywanych w terminalu, bez konieczności fizycznego wywoływania skryptu z zewnątrz.

**Wymagania Systemowe**
Zanim uruchomisz program, upewnij się, że w Twoim systemie zainstalowane są:
* Python (wersja 3.x)
* **FFmpeg** (wymagane przez `yt-dlp` do łączenia formatów wideo i audio)
* **Node.js** (wymagane do obsługi skryptów zabezpieczających YouTube)

**Jak zainstalować(np.w systemie linux):**
* sudo apt update
* sudo apt install -y ffmpeg
* sudo apt install -y nodejs

**Instalacja**
1. Sklonuj lub pobierz repozytorium projektu.
2. Zainstaluj wymagane zależności za pomocą polecenia:
   ```bash
   pip install -r requirements.txt
   ```

**Przykładowe Wejście:**
1. python project.py "https://www.youtube.com/watch?v=..." {mp3 lub mp4} - pamiętaj o objęciu linka cudzysłowiem
2. python project.py (argumenty podajesz w trakcie działania programu)

**Notatka**
* Projekt ten powstał w celach edukacyjnych. Narzędzie to pokazuje, jak pobierać materiały multimedialne przy użyciu języka Python. Użytkownik ponosi pełną odpowiedzialność za wszelkie przypadki naruszenia prawa autorskiego oraz regulaminu serwisu YouTube.
