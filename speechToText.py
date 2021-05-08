import speech_recognition as sr
import speech_recognition as sr
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

ltapikey = 'OZmPVJ_4X70AzVgC5OtKU-36Rk5ErjZw-cCJaifRlhKF'
lturl = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/1cd1e936-c1f3-4451-80dc-5de9c7be086a'
## translator upar hai
sttapikey = 'FC-qSiQERICDE4tCo3aVSugW0cjXBbEi5ypEZkCgiYXY'
stturl = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/02d77078-7947-4e3c-9feb-a4e3d6a1467f'

ltauthenticator = IAMAuthenticator(ltapikey)
lt = LanguageTranslatorV3(version='2018-05-01', authenticator=ltauthenticator)
lt.set_service_url(lturl)


sttauthenticator = IAMAuthenticator(sttapikey)
stt = SpeechToTextV1(authenticator=sttauthenticator)
stt.set_service_url(stturl)





def speech2Text(file):
  
    AUDIO_FILE = file







    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        greek = 'en-el'
        chinese = 'en-zh'
        hindi = 'en-hi'
        textdata = r.recognize_google(audio)
        #print("Text data: " + textdata)
        translation = lt.translate(text=textdata, model_id=hindi).get_result()
        translatedtext = translation['translations'][0]['translation']
        return translatedtext

    except sr.UnknownValueError:
        print(" Audio Error")

    except sr.RequestError as e:
        print("Could not request results from Google API; {0}".format(e))


#Write results to a txt file
#file = open("result.txt","w")
#file.write(textdata)
#file.writelines(L) 
#file.close()
