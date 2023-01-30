from requests import Session, get, exceptions
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                  "Safari/537.36 Edg/108.0.1462.76",
    "cookie": "__yjs_duid=1_8fe170d58bb1cce8148c55b8838474521665320641946; "
              "__gads=ID=5cae04fc85758d70-221c879f12d900a5:T=1672221946:RT=1672221946:S"
              "=ALNI_MbQDpHVzrh6CPVcD8lhdGd0SM9DXA; _ga=GA1.2.1757766294.1672221945; "
              "MCMOD_SEED=57p7jlu8kp70cftk2bqmoir7l4; "
              "__gpi=UID=00000b99e3535bf5:T=1672221946:RT=1673533059:S=ALNI_MbxYjDRWcykn80PP9RXBYhAIZ9Qzg; "
              "_gid=GA1.2.308316616.1673533064; _gat_gtag_UA_8762822_1=1",
}


def get_htmltext_mcmod(url):
    """
    根据url获取html文本 | Get html text according to the url

    :param url: 网页地址 | web page address
    :return response.text: 如果请求成功，返回html文本。否则返回错误信息。| If the request is successful, return the html text.
    Otherwise, return the error message.
            e: 错误 | error
    """

    # 使用Session()来设置重试次数 | Use Session() to set the number of retries
    session = Session()
    retry = Retry(total=5,
                  backoff_factor=0.1,
                  status_forcelist=[ 500, 502, 503, 504 ])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        # 发送请求 | Send request
        response = get(url, headers=headers, timeout=5)
        # 检查请求状态 | Check request status
        response.raise_for_status()
        # 返回html文本 | Return html text
        return response.text, None

    except exceptions.ConnectionError as e:
        # print("Error: ", e)
        return None, "\nAError: " + str(e) + "\nTime out!\nYou need a proxy server to access websites in mainland China"
    except exceptions.Timeout as e:
        # print("Error: Timeout")
        return None, "\nBError: Timeout, " + str(e)
    except exceptions.HTTPError as e:
        # print("Error: ", e)
        return None, "\nCError: " + str(e)
    except exceptions.TooManyRedirects as e:
        # print("Error: Too many redirects")
        return None, "\nDError: Too many redirects" + str(e)
    except (exceptions.SSLError, exceptions.ConnectionError) as e:
        # print("Error: SSL error")
        return None, "\nEError: SSL error" + str(e)
    except exceptions.RequestException as e:
        # print("Error: ", e)
        return None, "\nFError: " + str(e)


def get_urlname_mcmod(html_str, urlbasic_str):
    """
    input a string of html and a base url,
    returns a dictionary of mods names and their corresponding urls.
    get Mods names and URLs from the input html string,
    search for 'a' tags with specific attributes.
    这个函数接受一个html字符串和一个基础url作为输入，并返回一个mods名称和它们对应的url的字典。
    mods和url是通过搜索具有特定属性的“a”标签从输入html字符串中提取出来的。

    :param html_str: html字符串 | html string
    :param urlbasic_str:  mcmod网站的url | mcmod website`s url
    :return mods_dict: Mods名称和它们对应的URL的字典 | A dictionary of mod names and their corresponding urls
    """
    try:
        soup = BeautifulSoup(html_str, 'html.parser')
        mods_dict = {}

        for a_tag in soup.find_all('a', attrs={'data-toggle': 'tooltip', 'target': '_blank'}):
            if 'data-original-title' in a_tag.attrs:
                if not a_tag['data-original-title'].replace(".", "").isdigit():  # 不是浮点数字符串
                    if 'class' not in a_tag.attrs:
                        if a_tag.text:
                            url_str = a_tag['href']
                            name_str = a_tag.text
                            mods_dict[name_str] = urlbasic_str + url_str
        return mods_dict

    except Exception as e:
        print("Error: ", e)
        return None


if __name__ == '__main__':
    url1 = "https://www.mcmod.cn/modpack/253.html"
    resp_text1, *resp_error = get_htmltext_mcmod(url1)
    # print()
    print(resp_text1, *resp_error)

    urlbasic_str1 = "https://www.mcmod.cn"
    mods_dict1 = get_urlname_mcmod(resp_text1, urlbasic_str1)
    print(mods_dict1)
