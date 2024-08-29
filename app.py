import os
import shutil
directory = os.path.join(os.path.expanduser("~"), "C:\Users\Hp")
extensions ={
    ".jpg":"Images",
    ".png":"Images",
    ".gif":"Images",
    ".svg":"Images",
    ".pptx":"MSPowerPoints",
    ".mp4":"Videos",
    ".mkv":"Videos",
    ".mov":"Videos",
    ".doc":"Documents",
    ".docx":"Documents",
    ".apk":"Applications",
    ".csv":"DataSheets",
    ".xlsx":"MSDocs",
    ".exe":"Executibles",
    ".zip":"Zips",
    
    
    
    
    ".pdf":"Documents",
    ".srt":"Documents",
    ".txt":"Documents",
    ".mp3":"Music",
    ".wav":"Music"
    
}
for filename in os.listdir(directory):
    file_path= os.path.join(directory, filename)
    if os.path.isfile(file_path):
        extension= os.path.splitext(filename)[1].lower()
        if extension in extensions:
            folder_name= extensions[extension]
            folder_path= os.path.join(directory, folder_name)
            os.makedirs(folder_path,exist_ok=True)
            
            destination_path=os.path.join(folder_path,filename)
            shutil.move(file_path,destination_path)
            
            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown File Extension.")
    else:
        print(f"Skipped {filename}.It is Directory.")

print("File Organisation Completed.")
    
    
    
