import websocket
import threading # 1. 导入 threading 模块
import time

# 在接收到服务器发送消息时调用
def on_message(ws, message):
    print('Received: ' + message)


# 在和服务器建立完成连接时调用
def on_open(ws):
    # 线程运行函数
    def gao():
        # 往服务器依次发送 0-4，每次发送完休息 0.1 秒
        for i in range(5):
            time.sleep(0.01)
            msg = "{0}".format(i)
            ws.send(msg)
            print('Sent: ' + msg)
        # 休息 1 秒用于接受服务器回复的消息
        time.sleep(1)

        # 关闭 Websocket 的连接
        ws.close()
        print("Websocket closed")

    # 在另一个线程运行 gao() 函数
    # 2. 创建一个线程对象
    thread = threading.Thread(target=gao)
    # 3. 启动线程
    thread.start()


# 假设你还有一个 websocket 的主运行循环
if __name__ == "__main__":
    # websocket.enableTrace(True) # 如果需要调试信息，可以取消这行注释
    # 这里的 ws_url 需要替换成你实际的服务器地址
    ws_url = "ws://echo.websocket.events/"
    print(websocket.__file__)
    ws = websocket.WebSocketApp(ws_url,
                              on_message=on_message,
                              on_open=on_open)
    ws.run_forever()