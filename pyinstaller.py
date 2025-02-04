import PyInstaller.__main__

PyInstaller.__main__.run([
    'generator.py',
    '--onefile',
    '--noconsole',
    '--icon=frost3.ico',
    '--name=Frostdev Recipe Generator',
    '--optimize=2',
])