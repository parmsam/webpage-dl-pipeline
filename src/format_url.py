from urllib.parse import urlparse

def format_url(url):
    # Parse the URL to extract domain and path
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    
    # Remove leading slash from path if present
    if path.startswith('/'):
        path = path[1:]
    
    # Replace slashes with underscores in the path
    formatted_path = path.replace('/', '_')
    
    # Combine domain and formatted path separated by a dash
    formatted_url = f"{domain}-{formatted_path}"
    
    return formatted_url

# unit test