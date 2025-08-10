 # -- "os" module that works with operating systems 
 # --cases for "os" os.path.join()-->join path together, os.path.split()--> break file in two parts, os.path.exists() -->func that cheaks if directory exsits
import os
import requests
import time

class AntiVirus():

    API_KEY = "6475c610a65a96d2812d3fcf6a8253f702aab41f729aa6c8e6da00620c62a825"

    def __init__(self):
        pass
    
    # The recursion function that pass for each file 
    def iterate_files(self,folder_path, append_text_func,exclude_folders):

       
            print(f"Processing this: {folder_path}")

            if folder_path in exclude_folders:
                append_text_func(f"Skipping users private folder: {folder_path}")
                return
            try:
                # array that pass for file that was given
                for filename in os.listdir(folder_path):
                    # full_path conteins the folder name and the folder content
                    full_path = os.path.join(folder_path, filename)
                    print(f"found file: {full_path}")
                    # function " isdir" that checks if a given path is a directory
                    # if "yes" then the recursion go until the end of the directory
                    if os.path.isdir(full_path):
                        print(f"Recursion is running in the folder: {full_path}")
                        self.iterate_files(full_path, append_text_func, exclude_folders)
                    # if "not" then scan the file
                    else:
                        print(f"Scanning: {full_path}")
                        self.scan_file(full_path, append_text_func)
             #"except" - If the program can't access a folder 
             except PermissionError:
                 append_text_func(f"Access denied: {folder_path}")
                 print(f"Access denied: {folder_path}")
             # any other erorr
             except Exception as e:
                 append_text_func(f"Error occurred: {folder_path} - {str(e)}")
                 print(f"Error occurred: {folder_path} - {str(e)}")
        
                
    # function that scan the directory for availability of virus
    def scan_file(self,file_path, append_text_func):
        response = self.upload_file(file_path)
        scan_id = response.get('scan_id')
        if scan_id:
            is_virus = self.get_report(scan_id, append_text_func)
            if is_virus:
                append_text_func("VIRUS DETECTED!!! Filepath: " + file_path)
            else:
                append_text_func("{} is not virus".format(file_path))
        else:
            append_text_func("Unexpected response, no scan id found for file: ", file_path)

    # function that moves data from one location to another
    def upload_file(self,file_path):
        url = "https://www.virustotal.com/vtapi/v2/file/scan"

        params = {'apikey': self.API_KEY}
        # function "open -(rb)": open the file in the read mode
        file_content = open(file_path, 'rb')
        # returns the file name from a given file path
        filename = os.path.basename(file_path)
        files = {'file': (filename, file_content)}
        # 1. sends a POST request, 2. uploads file(s), 3. receives the apkeys
        response = requests.post(url, files=files, params=params)
        return response.json()
    

    def get_report(self,scan_id, append_text_func):
        append_text_func("getting report for scan id: " + scan_id)
        url = "https://www.virustotal.com/vtapi/v2/file/report"

        params = {'apikey': self.API_KEY, 'resource': scan_id}

        response = requests.get(url, params=params)
        if not response:
            raise Exception("Unexecpred Error in response")
        
        # Received good response
        if response.status_code == 200:
            response = response.json()
            # Scan not completed
            if response.get('response_code') != 1: 
                append_text_func("Scan not completed...")
                # the time that function need to scan files
                time.sleep(5)
                self.get_report(scan_id, append_text_func)
            else:
                return response.get("positives") > 0
            
        # Received response without content
        elif response.status_code == 204: 
            append_text_func("Empty response...")
            time.sleep(5)
            self.get_report(scan_id, append_text_func)
        # Received unexecpted response
        else: 
            
            append_text_func("Received unexpected response with status code:", response.status_code)
            return False


# call to the recursion function to pass for specific derectiry
def main():
    obg = AntiVirus()
    # obg.iterate_files("C://Users//nastk//chat")
    

if __name__ == "__main__":
    main()





   


