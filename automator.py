import os 
import shutil           # shutil was more intuitive to understand compared to the otehr 2 packages







source_folder = '/Users/harinivasanchandrasekaran/Downloads'


def get_unique_filename(filename, destination_folder, extension):
    

    base_filename, _ = os.path.splitext(filename)  # Separate filename and extension
    counter = 1
    while os.path.exists(os.path.join(destination_folder, f"{base_filename} ({counter}){extension}")):
        counter += 1
    return os.path.join(destination_folder, f"{base_filename} ({counter}){extension}")


def handle_file_move(file_type, source_path, destination_folder, extensions):
    

    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        file_list = [
            pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(extensions)
        ]

        no_files = 0
        for file in file_list:
            source_file_path = os.path.join(source_folder, file)
            destination_file_path = get_unique_filename(file, destination_folder, os.path.splitext(file)[1])
            shutil.move(source_file_path, destination_file_path)
            no_files += 1

        print(f"Total {file_type.capitalize()} Files Automated: {no_files}")

    except OSError as e:
        print(f"There were some issues when creating directories or moving files: {e}")


def image_class():
    image_folder = os.path.join(source_folder, 'Automated/Images')
    image_extensions = ('.jpeg', '.jpg', '.heic', '.png', '.bmp', '.tif', '.tiff', '.svg', '.webp', '.heif', '.psd', '.raw', '.gif')
    handle_file_move('image', source_folder, image_folder, image_extensions)
    
def video_class():
    video_folder = os.path.join(source_folder, 'Automated/Videos')
    video_extensions = ('.mp4', '.mov', '.wmv', '.avi', '.mkv', '.webm', '.flv', '.avchd', '.3gp', '.mpeg', '.mts', '.m2ts', '.ogg', '.ts', '.mxf')
    handle_file_move('video', source_folder, video_folder, video_extensions)


def document_class():
    document_folder = os.path.join(source_folder, 'Automated/Documents')
    document_extensions = ('.pdf', '.txt', '.word', '.rtf', '.docx', '.doc', '.xlsx', '.pptx', '.pages', '.numbers', '.key', '.csv', '.ini', '.iso', '.xml', '.html', '.json', '.cfg', 'epub', 'exml', 'ics', '.md','.odt','.tex','eml')
    handle_file_move('document', source_folder, document_folder, document_extensions)
    

def code_class():
    code_folder = os.path.join(source_folder, 'Automated/Codes')
    code_extensions = ('.py','ipynb','.js','.html','.css','.java','.gitignore','.rs','.sql','.sh','.swift','.db','.pt')
    handle_file_move('code', source_folder, code_folder, code_extensions)
    
def compressed_class():
    compressed_folder = os.path.join(source_folder, 'Automated/Compressed')
    compressed_extensions = ('.zip','.rar','.7z','.tar','.gz','.z')
    handle_file_move('compressed', source_folder, compressed_folder, compressed_extensions)
    
def application_class():
    application_folder = os.path.join(source_folder, 'Automated/Applications')
    application_extensions = ('.exe','.dmg','.app','.msi','.sh','.bat')
    handle_file_move('application', source_folder, application_folder, application_extensions)
    
    
def audio_class():
    audio_folder = os.path.join(source_folder, 'Automated/Audios')
    audio_extensions = ('.mp3', '.wav', '.flac', '.aac', '.m4a', '.ogg', '.wma', '.aiff', '.alac', '.dsd')
    handle_file_move('audio', source_folder, audio_folder, audio_extensions)
    




print(image_class())
print(video_class())
print(document_class())
print(code_class())
print(compressed_class())
print(application_class())
print(audio_class())







