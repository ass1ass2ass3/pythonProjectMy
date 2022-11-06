# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Admin\\pythonProjectMy\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\Admin\\pythonProjectMy\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['C:\\Users\\Admin\\pythonProjectMy\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\Admin\\pythonProjectMy\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='VadApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , version='C:\\Users\\Admin\\pythonProjectMy\\target\\PyInstaller\\version_info.py', icon='C:\\Users\\Admin\\pythonProjectMy\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='VadApp')
