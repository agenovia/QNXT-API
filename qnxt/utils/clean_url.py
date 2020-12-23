def clean_url(app_server, base_path):
    if app_server.endswith('/'):
        base_uri = f"{app_server[:-1]}{base_path}"
    else:
        base_uri = f"{app_server}/{base_path}"
    return base_uri
