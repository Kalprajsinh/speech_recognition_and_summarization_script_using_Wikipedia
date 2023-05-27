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
Done.
result:
{   'alternative': [   {   'confidence': 0.92995495,
                           'transcript': 'tell me about Albert Einstein '
                                         'invention'},
                       {   'transcript': 'tell me about Albert Einstein '
                                         'inventions'},
                       {   'transcript': 'tell me about Albert Einstein in '
                                         'invention'},
                       {   'transcript': 'tell me about Albert Einstein and '
                                         'invention'},
                       {   'transcript': 'tel me about Albert Einstein '
                                         'invention'}],
    'final': True}
> Albert Einstein ( EYEN-styne; German: [ˈalbɛʁt ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18 April 1955) was a 
German-born theoretical physicist, widely acknowledged to be one of the greatest and most influential physicists of all time. 
Best known for developing the theory of relativity, he also made important contributions to the development of 
the theory of quantum mechanics.
```
```
Talk...
Done.
result2:
{   'alternative': [   {   'confidence': 0.69254971,
                           'transcript': 'who is God Rama'},
                       {'transcript': 'who is ko Rahman'},
                       {'transcript': 'who is rama'},
                       {'transcript': 'who is ko Rama'},
                       {'transcript': 'who is God Rama'}],
    'final': True}
> Rama (; Sanskrit: राम, romanized: Rāma; Sanskrit: [ˈraːmɐ] (listen)) is a major deity in Hinduism. 
He is the seventh and one of the most popular avatars of Vishnu.
```

<sub>This answer is say by python <br>
engine.say(result)<br>
engine.say("Thank you, sir")</sub>
