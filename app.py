from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "If you see me on the web page, prove that you have completed all the tasks"
#def check_network():
#    try:
#        result = subprocess.run(
#            ["ping", "-c", "2", "baidu.com"], 
#            stdout=subprocess.PIPE, 
#            stderr=subprocess.PIPE
#        )
#        return result.returncode == 0
#    except Exception as e:
#        print(f"网络检测异常: 我好像需要ping 通baidu.com才能启动成功: {e}")
#        return False

# 测试
if __name__ == "__main__":
    #if not check_network():
    #    print("我没有网络，如果我无法访问baidu.com,我就会一直拒绝启动")
    #    sys.exit(1)
    print("tips: 我在容器内监听的端口是80")
    app.run(host="0.0.0.0", port=80)

