 
 
app = Flask('')
 
 
 
@app.route('/')
 
def home():
 
    return f"Discord.py API version: {discord.__version__} \nPython version: {platform.python_version()} \nRunning on: {platform.system()} {platform.release()} ({os.name})  Enjoy!"
 
 
def run():
 
  app.run(host='0.0.0.0',port=8080) 
 
def keep_alive():  
 
    t = Thread(target=run)
 
    t.start()

