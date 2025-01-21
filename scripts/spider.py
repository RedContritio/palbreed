import os
import requests
import json
from bs4 import BeautifulSoup
from lxml import html


def download_and_cache_data(url, cache_file):
    """下载数据并缓存到指定文件"""
    response = requests.get(url, verify=False)
    data = response.json()

    # 将数据写入本地缓存文件
    os.makedirs(os.path.dirname(cache_file), exist_ok=True)
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return data


def load_data(cache_file, allow_remote_request, remote_url):
    """加载已缓存的数据，如果没有缓存且允许远程请求，则下载数据"""
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif allow_remote_request:
        print("缓存文件不存在，开始下载数据...")
        return download_and_cache_data(remote_url, cache_file)
    else:
        raise FileNotFoundError(f"缓存文件不存在且未允许远程请求: {cache_file}")


def save_data(data, cache_file):
    """保存数据到缓存文件"""
    os.makedirs(os.path.dirname(cache_file), exist_ok=True)
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    cache_dir = "data/.cache"
    cache_index_file = os.path.join(cache_dir, "autocomplete_cn.json")
    url = "https://paldb.cc/json/autocomplete_cn.json"

    data = load_data(cache_index_file, allow_remote_request=True, remote_url=url)
    
    all_pals = [item for item in data if item['desc'] == '帕鲁']
    pal_names = [{'name_en': item['value'], 'name_cn': item['label']} for item in all_pals]
    cache_palname_file = os.path.join(cache_dir, "pal_names.json")
    save_data(pal_names, cache_palname_file)
    
    
    
    