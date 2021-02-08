from fastapi import APIRouter
import urllib.request

from app_01.model import LinkIn, LinkOut
import pdfkit

router_l2p = APIRouter()


@router_l2p.post("/link2pdf/")
async def link2pdf(item: LinkIn):
    fp = urllib.request.urlopen(item.url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    pdfkit.from_url(item.url, 'out_file.pdf')

    return LinkOut(link=item.url, html=mystr)
