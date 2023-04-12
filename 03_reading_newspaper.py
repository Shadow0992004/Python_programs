import requests
import json

def speak(str):
    from win32com.client import Dispatch
    
    speak=Dispatch("SAPI.Spvoice")
    speak.speak(str)

if __name__=="__main__":
    speak("News for today..lets begin ")
    API=""
    url=f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API}"
    news=requests.get(url).text
    news_dict=json.loads(news)
    # print(news_dict["articles"])
    arts=news_dict["articles"]
    for articles in arts:
        speak(articles['title'])
        speak("Moving on to the next news!! Listen carefully")
    print("thanks for listening.....")
