# LinguaBridge
Real-Time Speech Recognition and Translation Project

## 👋 Introduction

In today's increasingly interconnected world, the ability to communicate across language barriers is more important than ever. Our Real-Time Speech Recognition and Translation project aims to bridge these gaps by leveraging advanced technologies to provide seamless and instant speech-to-text transcription and translation services.

This project combines state-of-the-art speech recognition with real-time translation, enabling users to effortlessly convert spoken language into text and translate it into multiple target languages. This functionality is particularly beneficial for diverse applications, such as international business meetings, multilingual customer service, language learning, and accessibility for the hearing impaired.


## 🚀 Getting Started
### Requirements

```
openai==1.23.1
SpeechRecognition==3.10.3
translate==3.6.1
```

And you should export your openai key in your envioronment.

### Settings
These settings are typically read from the JSON file and applied to configure the speech recognition system. The voice setting file is located at ./Data/Settings

```json
{
  "record_timeout": 2,
  "phrase_timeout": 3,
  "pause_threshold": 0.8,
  "energy_threshold": 1000,
  "sample_rate": 16000,
  "dynamic_energy_threshold": false
}
```

**record_timeout**: Specifies the maximum amount of time (in seconds) to record each phrase or chunk of audio before automatically stopping. This setting helps ensure that each audio recording is of manageable length.

**phrase_timeout**: Defines the amount of time (in seconds) to wait for a new phrase to start before considering the current phrase complete. This is useful for determining the end of a phrase based on pauses in speech.

**pause_threshold**: Sets the minimum length (in seconds) of silence that will be considered a pause between phrases. This threshold helps in identifying pauses in speech, thereby determining where one phrase ends, and another begins.

**energy_threshold**: The energy level threshold for the microphone to consider as speech. Audio with an energy level above this threshold is treated as speech, while audio below this level is considered silence or background noise.

**sample_rate**: Specifies the sampling rate (in Hz) for the microphone audio input. A higher sample rate means better audio quality but more data to process.

**dynamic_energy_threshold**: Indicates whether the recognizer should automatically adjust the energy threshold based on the ambient noise levels. If set to true, the system dynamically adjusts the threshold to adapt to varying noise environments.

### Usage

```
python3 app.py
```


## 👨 Contributors

<table>
  <tbody>
        <td align="center" valign="middle" width="128">
         <a href="https://github.com/bochendong">
          <img src="https://github.com/bochendong.png?size=128" />
          Bochen Dong
        </a>
        <br>
        <sub><sup>Team Leader</sup></sub>
      </td>
      <td align="center" valign="middle" width="128">
        <a href="https://github.com/VGLALALA">
          <img src="https://github.com/VGLALALA.png?size=128" />
          Sting Zhang
        </a>
        <br>
        <sub><sup>Team Member</sup></sub>
      </td>
      <td align="center" valign="middle" width="128">
         <a href="https://github.com/nancyzhao1">
          <img src="https://github.com/nancyzhao1.png?size=128" />
          Nancy Zhao
        </a>
        <br>
        <sub><sup>Team Member</sup></sub>
      </td>
      <td align="center" valign="middle" width="128">
         <a href="https://github.com/Tabel0112">
          <img src="https://github.com/Tabel0112.png?size=128" />
          Abel Chen
        </a>
        <br>
        <sub><sup>Team Member</sup></sub>
      </td>

     
  </tbody>
</table>


## 📝 License

[MIT License](https://github.com/leon-ai/leon/blob/develop/LICENSE.md)