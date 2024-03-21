import os 
import shutil           # shutil was move intuitive to understand compared to the otehr 2 packages

source_folder = '/Users/harinivasanchandrasekaran/Downloads'

#lets incorporate error handling here     
try:
    
    if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated"):
        os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated")
except OSError as e:
    print(f"There were some issues when creating this directory: {e}")
        
    
def image_class():
    try:
        
    
        if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated/Images"):
            os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated/Images")
            
    except OSError as e:
        print(f"There were some issues when creating this directory: {e}")
        
    image_folder="/Users/harinivasanchandrasekaran/Downloads/Automated/Images/"
    
    image_files = [pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(('.jpeg','.jpg','.heic','.png','.bmp','.tif','.tiff','.svg','.webp','.heif','.psd','.raw','.gif'))]
    
    
    no_files=0
    for file in image_files:
        source_path=os.path.join(source_folder,file)
        image_path=os.path.join(image_folder,file)
        shutil.move(source_path,image_path)
        no_files+=1
        
    confirmation=(f"Total Images Automated:{no_files}") 
    
    return confirmation

def document_class():
    try:
        if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated/Documents"):
            os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated/Documents")
    except OSError as e:
        print(f"There were some issues when creating this directory: {e}")
    Documents_folder="/Users/harinivasanchandrasekaran/Downloads/Automated/Documents/"
    Documents_files = [pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(('.pdf','.txt','.word','.rtf','.docx','.doc','.xlsx','.pptx','.pages','.numbers','.key','.csv','.ini','.iso','.xml','.html','.json','.cfg','epub','exml','ics','.md'))]
    
    
    no_files=0
    for file in Documents_files:
        source_path=os.path.join(source_folder,file)
        image_path=os.path.join(Documents_folder,file)
        shutil.move(source_path,Documents_folder)
        no_files+=1
        
    confirmation=(f"Total Documents Automated:{no_files}") 
    
    return confirmation
    

def code_class():
    try:
        
        if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated/Code"):
            os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated/Code")
    except OSError as e:
        print(f"There were some issues when creating this directory: {e}")
    code_folder="/Users/harinivasanchandrasekaran/Downloads/Automated/Code/"
    code_files = [pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(('.py','ipynb','.js','.html','.css','.java','.gitignore','.rs','.sql','.sh','.swift','.db'))]
    
    
    no_files=0
    for file in code_files:
        source_path=os.path.join(source_folder,file)
        code_path=os.path.join(code_folder,file)
        shutil.move(source_path,code_path)
        no_files+=1
        
    confirmation=(f"Total Code Files Automated:{no_files}") 
    
    return confirmation

def application_class():
    
    try:
        
        if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated/Applications"):
            os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated/Applications")
    except OSError as e:
        print(f"There were some issues when creating this directory: {e}")
    apps_folder="/Users/harinivasanchandrasekaran/Downloads/Automated/Applications/"
    apps_files = [pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(('.exe','.dmg','.app','.msi','.sh','.bat'))]
    
    
    no_files=0
    for file in apps_files:
        source_path=os.path.join(source_folder,file)
        apps_path=os.path.join(apps_folder,file)
        shutil.move(source_path,apps_path)
        no_files+=1
        
    confirmation=(f"Total Application Files Automated:{no_files}") 
    
    return confirmation

def video_class():
    try:
        if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated/Videos"):
            os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated/Videos")
    except OSError as e:
        print(f"There were some issues when creating this directory: {e}")
    video_folder="/Users/harinivasanchandrasekaran/Downloads/Automated/Videos/"
    video_files = [pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(('.mp4','.heif','.avi','.mov','.wmv','.m4v','.flv','.xvid','.webm','.3gp','.ogg','.ts'))]
    
    
    no_files=0
    for file in video_files:
        source_path=os.path.join(source_folder,file)
        video_path=os.path.join(video_folder,file)
        shutil.move(source_path,video_path)
        no_files+=1
        
    confirmation=(f"Total Videos Automated:{no_files}") 
    
    return confirmation

def compressed_class():
    try:
        
        if not os.path.exists("/Users/harinivasanchandrasekaran/Downloads/Automated/Compressed"):
            os.makedirs("/Users/harinivasanchandrasekaran/Downloads/Automated/Compressed")
    except OSError as e:
        print(f"There were some issues when creating this directory: {e}")
    comp_folder="/Users/harinivasanchandrasekaran/Downloads/Automated/Compressed/"
    comp_files = [pos_file for pos_file in os.listdir(source_folder) if pos_file.lower().endswith(('.zip','.rar','.7z','.tar','.gz','.z'))]
    
    
    no_files=0
    for file in comp_files:
        source_path=os.path.join(source_folder,file)
        comp_path=os.path.join(comp_folder,file)
        # shutil was move intuitive to understand compared to the otehr 2 packages
        shutil.move(source_path,comp_path)
        no_files+=1
        
    confirmation=(f"Total Compressed Files Automated:{no_files}") 
    
    return confirmation

print(image_class())
print(video_class())
print(document_class())
print(code_class())
print(compressed_class())
print(application_class())







