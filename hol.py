from PIL import Image
import os,sys,glob
import subprocess,random
import progressbar
import time

random.seed()
r=random.randint(1,100)
name = sys.argv[1]
papka = os.getcwd()
os.mkdir(papka+'/tmp15')
tmp15=papka+'/tmp15'

proc = subprocess.call("ffmpeg -i "+name+" "+tmp15+"/image%d.jpg", shell=True, stdout=subprocess.PIPE)
print('Succes read video.')

bar = progressbar.ProgressBar().start()
l=0
for i in os.listdir(tmp15):
	l+=1
t=0
j=''
f=''
f2=''
for i in glob.glob(tmp15+'/*.jpg'):
	
	kart_v = Image.open(i)

	x= kart_v.size[0]
	y= kart_v.size[1]

	bg = Image.new("RGB", (x+2*y,x+2*y))

	kart_l = kart_v.rotate(90)
	kart_p = kart_v.rotate(270)
	kart_n = kart_v.rotate(180)

	bg.paste(kart_v, (y,0,y+x,y), None)
	bg.paste(kart_l, (0,y,y,y+x), None)
	bg.paste(kart_p, (x+y,y,x+2*y,y+x), None)
	bg.paste(kart_n, (y,y+x,y+x,x+2*y), None)

	if bg.size[0]>1280:
		bg = bg.resize((1280,1280))#,Image.BICUBIC)

	f=i.split(tmp15+'/image')
	j=f[1]
	bg.save(papka+'/'+j)
	os.remove(i)
	bar.update(t*100/l)
	t+=1
	
bar.finish()
proc1 = subprocess.call("avconv -f image2 -i %d.jpg "+papka+'/'+str(r)+name.split('.')[0]+'.avi', shell=True, stdout=subprocess.PIPE)
print('Succes create video.')
for i in glob.glob(papka+'/*.jpg'):
	os.remove(i)
os.rmdir(tmp15)

#bg.show()