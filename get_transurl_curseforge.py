from bs4 import BeautifulSoup
from base64 import b64decode
from re import search
from requests import get
from binascii import Error


def get_curseforgeurl_mcmod(html_str, forge_fabric_str):
    """
    input a string of html and returns the CurseForge url of a Minecraft mod.
    searchig for 'a' tags with specific attributes,
    compare the 'data-original-title' attribute to the strings 'CurseForge' and 'Fabric',
    get 'href' attribute of the 'a' tag,
    decode the obtained CurseForge URL.

    输入一个 html 字符串并返回一个 Minecraft mod 的 CurseForge url。
    搜索具有特定属性的“a”标签，
    将“data-original-title”属性与字符串“CurseForge”和“Fabric”进行比较，
    获取“a”标签的“href”属性，
    解码获得的 CurseForge URL。

    :param forge_fabric_str: main_tkinter中，主函数（main），get_forge_fabric_others_str()函数值
    :param html_str: html字符串 | html string
    :return txt_curseforge_url: Minecraft Mods的CurseForge URL | the CurseForge url of the Minecraft mods
    """
    code_url = ''
    txt_curseforge_url = ''

    url_curseforge_soup = BeautifulSoup(html_str, 'html.parser')
    match_all = url_curseforge_soup.find_all('a', attrs={'data-toggle': 'tooltip',
                                                         'rel': 'nofollow noreferrer',
                                                         'target': '_blank'})
    # print(match_all)

    # if forge_fabric_str == 'forge':
    #     search_str_forge = forge_fabric_str.capitalize() + '|' + 'forge'
    #     print(search_str_forge)
    # elif forge_fabric_str == 'fabric':
    #     search_str_fabric = forge_fabric_str.capitalize() + '|' + 'fabric'
    #     print(search_str_fabric)
    # elif (forge_fabric_str == 'GitHub') or (forge_fabric_str == 'MCBBS'):
    #     print(forge_fabric_str)
    # else:
    #     print('others')

    for a_tag in match_all:
        # print(a_tag.attrs.get('data-original-title'))
        match_curseforge = search('CurseForge', a_tag.attrs.get('data-original-title'))
        match_fabric = search('Fabric|fabric', a_tag.attrs.get('data-original-title'))
        match_forge = search('Forge|forge', a_tag.attrs.get('data-original-title'))
        # print(match_curseforge, match_forge, match_fabric)

        # match_github = search('GitHub', a_tag.attrs.get('data-original-title'))
        # match_mcbbs = search('MCBBS', a_tag.attrs.get('data-original-title'))

        # match_others = a_tag.attrs.get('data-original-title')

        if forge_fabric_str == 'fabric':
            if match_fabric and match_curseforge:
                code_url = a_tag['href']
                break
            elif match_fabric:
                code_url = a_tag['href']
                break
            else:
                code_url = '0' * 23
                continue

        elif forge_fabric_str == 'forge':
            if match_forge and match_curseforge and (not match_fabric):
                code_url = a_tag['href']
                break
            elif match_curseforge:
                # print("a")
                code_url = a_tag['href']
                break
            else:
                code_url = '0' * 23
                continue

        elif forge_fabric_str == 'GitHub':
            match_github = search('GitHub', a_tag.attrs.get('data-original-title'))
            if match_github and (not match_forge) and (not match_fabric) and (not match_curseforge):
                code_url = a_tag['href']
                break
            else:
                code_url = '0' * 23
                continue

        elif forge_fabric_str == 'MCBBS':
            match_mcbbs = search('MCBBS', a_tag.attrs.get('data-original-title'))
            if match_mcbbs:
                code_url = a_tag['href']
                break
            else:
                code_url = '0' * 23
                continue

        elif forge_fabric_str == 'Others':
            match_others = search('^CurseForge|^GitHub|MCBBS',
                                  a_tag.attrs.get('data-original-title'))
            if not match_others:
                code_url = a_tag['href']
                break
            else:
                code_url = '0' * 23
                continue

        else:
            code_url = '0' * 23
            continue

    try:
        txt_urlencoded = code_url[23:]
        txt_curseforge_url = b64decode(txt_urlencoded).decode()
    # 防止Incorrect padding错误 | prevent Incorrect padding Error
    except Error as e:
        print('Error: ' + str(e))
        # print(code_url)
        # txt_curseforge_url = 'https:' + code_url
        pass

    return txt_curseforge_url


if __name__ == '__main__':
    html_str1 = get('https://www.mcmod.cn/class/2346.html').text
    txt_curseforge_url1 = get_curseforgeurl_mcmod(html_str1, 'forge')
    print(txt_curseforge_url1)
