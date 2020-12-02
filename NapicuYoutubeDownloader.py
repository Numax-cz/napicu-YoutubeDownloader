import pytube
from pytube import YouTube
import os
print()
url = input("Zadej url videa které chceš stáhnout: ")
print('============================================')
print('Video se načítá!')
print('Prosím počkejte...')
print('============================================')
try: 
    YTvideo = pytube.YouTube(url)
    print('============================================')
    print(YTvideo.title)
    print('============================================')
except:
    print()
    print('============================================')
    print('Video nenačteno :(')
    print('============================================')
    os.system('pause')
    exit()
pov = 0o755
slozka = "NapicuDownloader"
try:
    os.mkdir(slozka, pov)
except FileExistsError:
    print('Složka "NapicuDownloader" již existuje! ')
except:
    print('Při vytváření složky došlo k chybě')
else:
    print('Složka "NapicuDownloader" byla vytvořena!')
print()
rozliseni = input("Zadej rozlišení videa 720p/1080p: ")
if rozliseni ==('720p') or rozliseni == ('720'):
    tag = 22
elif rozliseni ==('1080p') or rozliseni == ('1080'):
    tag = 137
else:
    rozliseni = input("Zadej rozlišení videa 720p/1080p: ")
    if rozliseni ==('720p') or rozliseni == ('720'):
        tag = 22
    elif rozliseni ==('1080p') or rozliseni == ('1080'):
        tag = 137
    else:
        rozliseni = input("Zadej rozlišení videa 720p/1080p: ")
        if rozliseni ==('720p') or rozliseni == ('720'):
            tag = 22
        elif rozliseni ==('1080p') or rozliseni == ('1080'):
            tag = 137
jmenoSouboru = input('Jak chcete pojmenovat video?: ')
print('============================================')
try:
    dw = YTvideo.streams.get_by_itag(tag)
except:
    print('Špatný tag')
print('Video se stahuje.....')
try:
    dw.download(filename=jmenoSouboru)
except:
    print('============================================')
    print('Chyba')
    print('============================================')
    os.system('pause')
    exit()
finally:
    print()
    print('Video bylo staženo!')
    os.system('pause')
    exit()