import subprocess


def open_app(app_name):

    try:

        subprocess.Popen([app_name])

        return f"Opened {app_name}"

    except Exception as e:

        return f"Error: {e}"
