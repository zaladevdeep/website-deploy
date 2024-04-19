def check_update():

    # GETTING LATEST VERSION FROM GITHUB
    url = 'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    owner = 'zaladevdeep'
    repo = 'ipo_allotment'
    path = 'version.txt'
    params = {'ref': 'main'}

    # Send the GET request to retrieve the file content
    response = requests.get(url.format(owner=owner, repo=repo, path=path), params=params)
    content = json.loads(response.content)

    # Decode the base64-encoded content of the file
    file_content = base64.b64decode(content['content']).decode('utf-8')
    print(file_content)

    if ver.version == file_content:
        print("Latest Version")
    else:
        response = messagebox.askyesno('Update Available', 'An update is available. Do you want to download and install it?')
        if response == tk.YES:
            url1 = 'https://api.github.com/repos/{owner}/{repo}/releases/latest'
            # owner = 'zaladevdeep'
            # repo = 'hello_app'

            # Send the GET request to retrieve the release information
            response = requests.get(url1.format(owner=owner, repo=repo))
            release_info = json.loads(response.content)

            new_dialog = tk.Toplevel()
            new_dialog.geometry("300x100")
            new_dialog.title("Update Downloading")

            # Add a progress bar to the new dialog box
            progress_bar = tk.ttk.Progressbar(new_dialog, orient="horizontal", length=200, mode="determinate")
            progress_bar.pack(pady=20)

            # Add a label to show the progress percentage
            progress_label = tk.Label(new_dialog, text="Downloading update (0%)")
            progress_label.pack()

            # Download the release assets
            r = requests.get(release_info['zipball_url'], stream=True)
            zipfile_bytes = io.BytesIO()
            total_size = int(r.headers.get('Content-Length', sys.maxsize)) # Set an arbitrary large value if Content-Length is not provided
            # chunk_size = 2048 # 2 kB
            chunk_size = 4194304 # 4 MB
            downloaded_size = 0
            if(os.path.exists("update.zip")):
                os.remove("update.zip")
            with open("update.zip", "wb") as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        zipfile_bytes.write(chunk)
                        print("Downloaded size: ", downloaded_size)
                        print("CHUNK SIZE: ", len(chunk))
                        print("TOTAL SIZE: ", total_size)
                        downloaded_size += len(chunk)
                        progress_pct = int(downloaded_size / total_size * 100)
                        progress_bar['value'] = progress_pct
                        progress_label.config(text=f"Downloading update ({progress_pct}%)")
                        print(f"Downloading update ({progress_pct}%")
                        new_dialog.update()

            #Remove ZIP file
            os.remove("update.zip")
            new_dialog.destroy()

            if(os.path.exists("update.exe")):
                os.remove("update.exe")

            # Extract the exe file from the release assets
            with zipfile.ZipFile(zipfile_bytes) as z:
                for filename in z.namelist():
                    if filename.endswith('.exe'):
                        with open("update.exe", 'wb') as f:
                            f.write(z.read(filename))
                        break

            with open('run_update.bat', 'w') as f:
                f.write('start update.exe')

            # run batch file
            subprocess.call('run_update.bat', shell=True)

            os.remove("run_update.bat")
            # os.remove("update.exe")

            # exit app
            sys.exit(0)
