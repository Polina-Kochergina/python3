from urllib.request import urlretrieve
import argparse

# описываем аргументы командной строки
parser = argparse.ArgumentParser() 

parser.add_argument("ra", help = "ra") 
parser.add_argument("dec", help = "dec") 
parser.add_argument("w", help = "width and high") 
parser.add_argument("h", help = "width and high") 
parser.add_argument("name", help = "name of file") 
args = parser.parse_args()

# ra = str(args.ra)
# dec = str(args.dec)
# w = str(args.w)
# h = str(args.h)
# name = str(args.name)

# используем url для доступа к серверу
site = f"http://skyserver.sdss.org/dr14/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra={args.ra}&dec={args.dec}&scale=0.5&width={args.w}&height={args.h}&opt=G"
urlretrieve(site, f"{args.name}.jpeg")