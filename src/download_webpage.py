from pywebcopy import save_webpage

# Function to download a single webpage
def download_webpage(url, download_folder):
    kwargs = {
        'bypass_robots': True,
        'project_name': "local_copy"
    }
    save_webpage(
        url,
        download_folder,
        **kwargs
    )


