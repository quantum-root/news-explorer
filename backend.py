import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import webbrowser
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def haberleri_getir(site_adi):
    rss_linkler = {
        "BBC": "https://feeds.bbci.co.uk/turkce/rss.xml",
        "KARAR": "https://www.karar.com/rss",
        "INDEPENDENT": "https://www.independent.co.uk/news/rss"
    }
    
    url = rss_linkler.get(site_adi)
    haber_listesi = []

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        cevap = requests.get(url, headers=headers, timeout=10)
        
        corba = BeautifulSoup(cevap.content, "html.parser")
        
        items = corba.find_all('item')
        
        for haber in items:
            baslik = haber.title.get_text(strip=True) if haber.title else "Başlık Yok"
            baslik = baslik.replace("<![CDATA[", "").replace("]]>", "")
            

            link = ""
            if haber.link:
                link = haber.link.get_text(strip=True)
                if not link and haber.link.next_sibling:
                    link = haber.link.next_sibling.strip()

            if baslik and link and link.startswith("http"):
                if len(haber_listesi) < 10:
                    haber_listesi.append([baslik, link])
                
        return haber_listesi
    except Exception as e:
        return [[f"Hata: {str(e)}", ""]]

def siteyi_ac(url):
    if url:
        temiz_link = str(url).strip()
        webbrowser.open(temiz_link)