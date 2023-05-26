## speech recognition and summarization script using Wikipedia

> The speech recognition and summarization system presented here is a powerful tool that allows users to retrieve information hands-free and eyes-free using voice commands. By leveraging the speech recognition capabilities of the `speech_recognition` library, the system can understand spoken words and convert them into text. It then utilizes the `wikipedia` library to retrieve concise summaries from Wikipedia based on the recognized text. The obtained summaries are then read aloud to the user using the text-to-speech engine provided by `pyttsx3`.

**Python librarys**

[speech_recognition](https://pypi.org/project/SpeechRecognition/)<br>
[pyttsx3](https://pypi.org/project/pyttsx3/)<br>
[wikipedia](https://pypi.org/project/wikipedia/)<br>

***This system provides a simple yet effective way to obtain information from Wikipedia using voice commands. It combines speech recognition, Wikipedia integration, and text-to-speech capabilities to create an interactive and hands-free experience for accessing knowledge.***

```
Example :
Talk...
tell me about india          # your question
Done.
India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[25] is a country in South Asia. It is the seventh-largest country by area, and the most populous country in the world as of 1 May 2023.[26][27] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest
```

<sub>This answer is say by python <br>
engine.say(result)<br>
engine.say("Thank you, sir")</sub>
