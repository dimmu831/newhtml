from flask import Flask
app = Flask(__name__) #__name__代表目前執行的模組

@app.route("/") #fn的裝飾(Decorator)已函式為基礎，提供附加功能
def hello():
    return "Hello Flask!"

@app.route("/test") 
def test():
    return "Hello test!"
if __name__ == "__main__":#如果以主程式執行
    app.run()#立刻啟動伺服器