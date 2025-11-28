import speech_recognition as sr

reco = sr.Recognizer()
  
    # print("What you said is : " + text)

while True:
       with sr.Microphone() as source:
         reco.adjust_for_ambient_noise(source)
 
       print("Speak now...")
       audio = reco.listen(source)

       print("Recognizing speech...")
       text = reco.recognize_google(audio)

       if text.lower().strip() == "hello":
           print("Hi there!")

       elif text.lower().strip() == "how are you":
           print("I'm doing well, thank you!")

       elif text.lower().strip() == "what about you ":
           print("I'm just a program, but thanks for asking!")   

       elif text.lower().strip() == "what is your name ":
           print("I am your speech recognition assistant.")
           
       elif text.lower().strip() == "ok then bye":
           print("Goodbye!")
           break