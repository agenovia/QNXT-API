def clean_url(app_server, base_path) -> str:
    """
    Pass the FQDN of the app server and a base path for the API endpoint, returns the FQDN and base path in the proper
    string format

    Parameters
    ----------
    app_server: str, required
        FQDN of app server
    base_path: str, required
        Base path for the API endpoint

    Returns
    -------
    base_url: str
        Formatted URL string
    """
    if app_server.endswith('/'):
        base_url = f"{app_server[:-1]}{base_path}"
    else:
        base_url = f"{app_server}/{base_path}"
    return base_url
