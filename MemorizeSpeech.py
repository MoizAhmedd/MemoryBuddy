import io
import os


def transcribe_file(speech_file):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    transcript = ''


    client = speech.SpeechClient(credentials = "Your Credentials")

    with io.open(speech_file,'rb') as audio_file:
        content = audio_file.read

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(encoding = enums.RegonitionConfig.AudioEncoding.LINEAR16,sample_rate_hertz = 16000,language_code = 'en-US')

    response = client.recognize(config,audio)

    for result in response.results:
        #print(u'Transcript:{}'.format(result.alternatives[0].transcript))
        transcript += result

    return transcript


def checkMemorization(speech_audio:str,speech_text:IO):


    transcript = transcribe_file(speech_audio).split() #Takes string text, and splits it into list of words
    attempt = [] #Stores words from file
    file = open(speech_text,'r') #Opens file
    numerrors = 0 #Accumulator
    errors = [] #Stores troublesome words

    for line in file:
        words = line.split()
        for word in words:
            attempt.append(word)

    for x,word in attempt:
        if word != transcript[x]:
            numerrors += 1
            errors.append([])

    #Results
    print("You have {} errors, the words you struggled with were {}".format(numerrors,errors))











