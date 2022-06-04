import requests

def punctuate(text):
    data = {'text': text,}
    response = requests.post('http://bark.phon.ioc.ee/punctuator', data=data)
    return response.text

if __name__ == "__main__":

    response = punctuate("will you follow me to the moon")
    print(response)