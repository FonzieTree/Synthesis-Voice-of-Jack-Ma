from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

file = open('result.txt', 'wt')

sliced = os.listdir('E:/lzy/sliced/')

for line in sliced[:5]:


    result = client.asr(get_file_content('E:/lzy/sliced/' + line), 'wav', 16000, {'lan': 'zh'})

    try:
        file.write(line[:8] + '|' + result['result'][0])

        file.write('\n')

        file.flush()
    except:

         pass

file.close()

