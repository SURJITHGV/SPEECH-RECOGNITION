import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak now :")
    audio=r.listen(source)
try:
    text1=r.recognize_google(audio)
    print("="*120)
    print("You said the following : {}".format(text1))
    print("="*120)
except:
    print("Sorry I Couldn't Understand")        
def savefile():
    savetxt=open('yourspeech1.txt','w')
    savetxt.write(text1)
    savetxt.close()
savefile()
print("Open yourspeech.txt to view your speech in text format !")

d=input("continue?")
if(d=='y'):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now :")
        audio=r.listen(source)
    try:
        text2=r.recognize_google(audio)
        print("="*120)
        print("You said the following : {}".format(text2))
        print("="*120)
    except:
        print("Sorry I Couldn't Understand")
    def addtxt():
        addtxt=open('yourspeech2.txt','w')
        addtxt.write(text2)
        addtxt.close()
    addtxt()
    def append():    
        txt1=open('yourspeech1.txt','r')
        txt1.read()
        txt2=open('yourspeech2.txt','r')
        txt2.read()
        fintxt=open('finalspeech.txt','w')
        txt3=text1+text2
        fintxt.write( txt3)
        fintxt.close()
    append()                    
    print("open finalspeech.txt to view your appended speeches !!)
