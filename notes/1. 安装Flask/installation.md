# python 版本
推荐使用最新的python版本，python3.7及以上都支持

# 与Flask同时被安装的依赖
1. werkzeug: WSGI，是app和server之间的标准python接口
2. Jinja: 模板语言，渲染应用所服务的web页面
3. MarkupSafe: 在渲染模板时转义不受信任的输入以避免注入攻击
4. ItsDangerous: 安全地签署数据以确保其完整性，用于保护flask的session cookie
5. Click: 用于编写命令行应用程序的框架，它提供了flask命令并允许添加自定义管理命令

# 可选依赖
Flask不会自动安装这些依赖：
1. Blinker: 为信号提供支持(Signals)
2. python-dotenv: enables support for Environment Variables From dotenv when running flask commands.
3. Watchdog: 为开发服务器提供更快、更高效的重载器

# 虚拟环境
1. 解决不同python环境存在的包冲突问题

# Start venv & install Flask
```bash
# windows
## activate venv
.\venv\Scripts\activate

## install Flask
pip install Flask
```
