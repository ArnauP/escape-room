# -*- mode: python -*-

block_cipher = None

a = Analysis(['__main__.py'],
             pathex=['.'],
             binaries=None,
             datas=[('resources/icons', 'resources/icons'),
                     ('resources/style', 'resources/style')],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Control Panel',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
	  icon='resources\\icons\\app.ico')
