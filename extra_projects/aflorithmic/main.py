import aflr
aflr.api_key = "2a75ce38d8bb4dbea063852cdc89f118"


text = "<<sectionName::question>> Hallo, wie geht es dir heute? <<sectionName::answer>> Hallo, ich fühle mich heute sehr glücklich"
script = aflr.Script().create(scriptText=text, scriptName="german_test_2")
print(script) 

# Create text to speech 
r = aflr.Speech().create(
    scriptId=script["scriptId"],
    voice="en-US-Standard-D",
    speed=90,
    silence_padding=0,
     sections={
        "question": {
            "voice": "de-DE-KatjaNeural",
            "speed": 110,
            "silence_padding": 1000
        },
        "answer": {
            "voice": "de-DE-Wavenet-E",
            "speed": 100,
        }
   
     }
)
print(r)

# Mastering creation 
r = aflr.Mastering().create(scriptId=script["scriptId"], backgroundTrackId="full__deepsea.wav")
print(r)

# retrieve the mastered audio files
r = aflr.Mastering().retrieve(scriptId=script["scriptId"])
print(r)

# download all speech audio files
# check your folder :) you should have the following audio_files
file = aflr.Mastering().download(scriptId=script.get("scriptId"), destination=".")
print(file)