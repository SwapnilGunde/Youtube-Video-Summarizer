import tkinter as tk
from tkinter import messagebox
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

def summarize_video():
    video_url = url_entry.get()

    video_id = video_url.split("=")[1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        result = ""

        for i in transcript:
            result += ' ' + i['text']

        summarizer = pipeline('summarization')

        num_iters = int(len(result) / 1000)
        summarized_text = []

        for i in range(num_iters + 1):
            start = i * 1000
            end = (i + 1) * 1000
            out = summarizer(result[start:end])
            out = out[0]
            out = out['summary_text']
            summarized_text.append(out)

        summary_box.delete(1.0, tk.END)
        summary_box.insert(tk.END, "\n".join(summarized_text))

    except Exception as e:
        messagebox.showerror("Error", str(e))



window = tk.Tk()
window.title("YouTube Video Summarizer")


url_label = tk.Label(window, text="YouTube Video URL:")
url_label.pack()
url_entry = tk.Entry(window, width=40)
url_entry.pack()


summarize_button = tk.Button(window, text="Summarize", command=summarize_video)
summarize_button.pack()

summary_label = tk.Label(window, text="Summary:")
summary_label.pack()
summary_box = tk.Text(window, height=25)
summary_box.pack()


window.mainloop()



#ASR,NLP,Video analysis,Sentiment Analysis