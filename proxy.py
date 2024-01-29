import requests
from colorama import Fore, Style
from datetime import datetime

def download_proxies(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f'Hata oluştu: {e}')

def main():
    print(Fore.YELLOW + Style.BRIGHT + '''
    ╦ ╦┌─┐╔═╗╦╔═┌─┐╔╦╗  ╔╗ ┬ ┬  ╔═╗┌─┐╔═╗┌─┐╔═╗┬ ┬╔═╗
    ╠═╣├─┤║  ╠╩╗├┤  ║║  ╠╩╗└┬┘  ╠═╝├┤ ║ ╦├─┤╚═╗│ │╚═╗
    ╩ ╩┴ ┴╚═╝╩ ╩└─┘═╩╝  ╚═╝ ┴   ╩  └─┘╚═╝┴ ┴╚═╝└─┘╚═╝
    ''' + Fore.WHITE + Style.NORMAL)

    print(Fore.CYAN + 'Proxy Listesi İndiriliyor...' + Fore.RESET)
    
# HTTP Proxy Listesi
    download_proxies('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http', 'http_proxies.txt')
    download_proxies('https://openproxy.space/list/http', 'http_proxies.txt')
    download_proxies('https://openproxylist.xyz/http.txt', 'http_proxies.txt')
    download_proxies('https://openproxylist.xyz/all.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt', 'http_proxies.txt')
    download_proxies('https://proxyscan.io/download?type=http', 'http_proxies.txt')
    download_proxies('https://proxyspace.pro/http.txt', 'http_proxies.txt')
    download_proxies('https://proxyspace.pro/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/almroot/proxylist/master/list.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt', 'http_proxies.txt')
    download_proxies('https://www.proxyscan.io/download?type=https', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt', 'http_proxies.txt')
    download_proxies('https://www.proxy-list.download/api/v1/get?type=http', 'http_proxies.txt')
    download_proxies('https://www.proxyscan.io/download?type=http', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt', 'http_proxies.txt')
    download_proxies('https://api.openproxylist.xyz/http.txt', 'http_proxies.txt')
    download_proxies('https://cyber-hub.pw/statics/proxy.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/almroot/proxylist/master/list.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt', 'http_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt', 'http_proxies.txt')
    download_proxies('https://rootjazz.com/proxies/proxies.txt', 'http_proxies.txt')
    download_proxies('https://www.proxy-list.download/api/v1/get?type=http', 'http_proxies.txt')
    # Diğer HTTP proxy listelerini ekleyebilirsiniz...


    # SOCKS4 Proxy Listesi
    download_proxies('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4', 'socks4_proxies.txt')
    download_proxies('https://openproxy.space/list/socks4', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://openproxylist.xyz/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://proxyscan.io/download?type=socks4', 'socks4_proxies.txt')
    download_proxies('https://proxyspace.pro/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/proxylist-to/proxy-list/main/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt', 'socks4_proxies.txt')
    download_proxies('https://www.proxy-list.download/api/v1/get?type=socks4', 'socks4_proxies.txt')
    download_proxies('https://www.proxyscan.io/download?type=socks4', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://api.openproxylist.xyz/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt', 'socks4_proxies.txt')
    download_proxies('https://www.proxy-list.download/api/v1/get?type=socks4', 'socks4_proxies.txt')
    # Diğer SOCKS4 proxy listelerini ekleyebilirsiniz...


    # SOCKS5 Proxy Listesi
    download_proxies('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5', 'socks5_proxies.txt')
    download_proxies('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt', 'socks5_proxies.txt')
    download_proxies('https://openproxylist.xyz/socks5.txt', 'socks5_proxies.txt')
    # Diğer SOCKS5 proxy listelerini ekleyebilirsiniz...

    print(Fore.GREEN + 'Proxy Listesi Başarıyla İndirildi.' + Fore.RESET)

if __name__ == "__main__":
    main()
