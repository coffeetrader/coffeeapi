import setuptools
import re
import requests
from bs4 import BeautifulSoup
import os
from twine.commands.upload import upload
from twine.settings import Settings

package_name = "coffeeapi"

# ... (保持其他函数不变)

def build_and_upload():
    # 构建包
    os.system('python setup.py sdist bdist_wheel')

    # 使用 twine 上传
    dist_files = ['dist/*']
    pypi_token = os.environ.get('pypi-AgEIcHlwaS5vcmcCJGM0NTY0YzYxLTEwOGUtNGQ4NS04OTA4LTgwZWEwYWQyZjNmMQACKlszLCI5MWFjYWU5NC1hYTY4LTQxOTYtYmZmNy1jNDIxNmQ5ZmUzMzMiXQAABiCzypkPPaEQEJZVbqvY4E_k3EGdZuNlcWRuak-pHM1Qvg')  # 从环境变量获取令牌
    if not pypi_token:
        raise ValueError("未设置 PYPI_API_TOKEN 环境变量")

    settings = Settings(
        username='limooor',
        password='zlw01023337',
        repository_url='https://github.com/coffeetrader/coffeeapi'
    )
    upload(settings, dist_files)

def main():
    try:
        build_and_upload()
        print("上传成功，当前版本:", curr_version())
    except Exception as e:
        raise Exception("上传包时出错", e)

if __name__ == '__main__':
    main()