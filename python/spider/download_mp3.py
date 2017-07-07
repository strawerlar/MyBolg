import urllib.request

no = 480
response = urllib.request.urlopen("http://www.ishuyin.com/player.php?mov_id=12204&look_id="+ str(no)+"&player=mp")

mp3 = response.read()

with open('480.mp3','wb') as f:
    f.write(mp3)
