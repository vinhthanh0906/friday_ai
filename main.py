import eel
import subprocess
import platform
import os

eel.init('www')
url = 'http://localhost:8000/index.html'

if platform.system() == 'Darwin':  # macOS
    subprocess.Popen(['open', '-a', 'Google Chrome', '--args', f'--app={url}'])
else:
    # Windows/Linux fallback
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
