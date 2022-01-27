import pyqrcode
import png
from pyqrcode import QRCode
TWITTER = "https://twitter.com/ABDOU_DZB"
url = pyqrcode.create(TWITTER)
url.png("TWITTER.png",scale=6)