import os
import sys
import youtube_dl

def changeDir(dir):
    os.chdir(dir)
    try:
        # tenta acessar o diretório
        os.chdir(dir)
        print('Path found successfully!')
    except:
        # caso não consiga acessar o diretório
        print('Path not found! :(')
        try:
            # tenta criar o diretório
            os.mkdir(dir)
            print('Path created successfully!')
        except:
            # caso não consiga criar o diretório
            print('ERROR: Check the path.')
            return sys.exit()
    return dir

def createList():
    lista_de_links = []
    while True:
        link = str(input('Insert a new link or 0 to continue:\n'))
        if (link == '0') | (link == 'sair') | (link == 'exit'):
            return lista_de_links
        lista_de_links.append(link)

def download(link):
    video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
    filename = f"{video_info['title']}.mp3".replace(' ', '_')
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))

if __name__ == "__main__":
    path = r'C:\Users\name\Music\Downloads'
    diretorio = changeDir(path)
    lista_de_links = createList()
    for link in lista_de_links:
        download(link)