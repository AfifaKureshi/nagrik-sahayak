import speech_recognition as sr

def voice_to_text(file_path, language="hi-IN"): # Now accepts file_path
    r = sr.Recognizer()
    
    # Cloud-safe: Use AudioFile instead of Microphone
    with sr.AudioFile(file_path) as source:
        r.adjust_for_ambient_noise(source, duration=1.2)
        try:
            audio = r.record(source) # Records from the file
            text = r.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Voice not understood"
        except sr.RequestError:
            return "Speech service not available"