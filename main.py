from flask import Flask

from src.CookieTool import Cookie
from src.main_complete import TikTok
from src.main_web_UI import WebUI


def main():
    try:
        mode = int(
            input(
                "请输入 TikTokDownloader 运行模式: \n0. 写入 Cookie 信息\n1. 单线程终端模式\n2. 多进程终端模式\n3. Web UI 交互模式\n"))
    except ValueError:
        return
    # mode = 3
    match mode:
        case 0:
            Cookie().run()
        case 1:
            example = TikTok()
            example.run()
        case 2:
            pass
        case 3:
            """设置host=0.0.0.0可以启用局域网访问，但是本项目暂时不支持直接部署至公开服务器"""
            app = WebUI().webui_run(Flask(__name__))
            app.run(host=None, debug=False)


if __name__ == '__main__':
    main()
