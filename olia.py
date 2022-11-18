import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Getting an imageof a section of the sky from SDSS')
parser.add_argument('dec', help='The declination of your site')
parser.add_argument('ra', help='The The right ascension of your site')
parser.add_argument('width', help='The image width')
parser.add_argument('height', help='The image height')
args = parser.parse_args()

# with urllib.request.urlopen(f"http://skyserver.sdss.org/dr14/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra={args.ra}&dec={args.dec}&scale=0.5&width={args.width}&height={args.height}&opt=G") as way: image = way.read()


resource = urllib.request.urlopen(f"http://skyserver.sdss.org/dr14/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra={args.ra}&dec={args.dec}&scale=0.5&width={args.width}&height={args.height}&opt=G", _DataType= pic.jpeg)
out = open("pic_img.jpg", 'wb')
out.write(resource.read())
out.close()


# p = url.get(img)
# out = open("picimg.jpg", "wb")
# out.write(p.content)
# out.close()