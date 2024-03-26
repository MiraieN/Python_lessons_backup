import requests
import tkinter as tk

headers = {
    "X-RapidAPI-Key": "8edc69c65dmsh9314d6fc748018cp1104aejsn09d9fb0666ae",
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

usedLabels = []
fg_color = '#3C3C3C'

def word_into_definitions(word):
    # deleting previous definitions
    global usedLabels
    if usedLabels:
        for each in usedLabels:
            each.destroy()
        usedLabels.clear()

    url = "https://wordsapiv1.p.rapidapi.com/words/" + word.lower() + "/definitions"
    try:
        response = requests.get(url, headers=headers)
        definitions = [prop['definition'] for prop in response.json()['definitions']]
    except KeyError:
        createDefinitionLabel('The word is not typed correctly')
        return
    print(response.json())
    for definition in definitions[:3]:
        createDefinitionLabel(definition)
    # definitions = ['definition1', 'definition2', 'definition3']
    # for definition in definitions[:3]:
    #     createDefinitionLabel(definition)

def createDefinitionLabel(text):
    global usedLabels
    text = "-" + text
    if len(text) > 80:
        for i in range(1, len(text) // 80 + 1):
            sign = i * 80
            while text[sign] != " ":
                sign -= 1
            text = text[:sign] + '\n' + text[sign:]

    new_label = tk.Label(bg="#D9D9D9", text=text, font='Arial 18', fg=fg_color)
    new_label.pack(pady=20)
    usedLabels.append(new_label)


root = tk.Tk()

WIDTH, HEIGHT = root.winfo_screenwidth()//2, root.winfo_screenheight()//2
root.geometry(f'{WIDTH}x{HEIGHT}+{WIDTH//2}+{HEIGHT//2}')
root.resizable(False, False)
root.configure(bg='#E6E6E6')

entryFrame = tk.Frame(width=630, height=145, bg='#E6E6E6')
entryFrame.pack(pady=80)

entry = tk.Entry(master=entryFrame, borderwidth=0, font='Arial 40 bold', justify='center', bg='#C6C6C6')
entry.pack(side='left')

search_but = tk.Button(master=entryFrame, text="Search", font='Arial 24 bold', bg='#C6C6C6', fg=fg_color,
                       borderwidth=0, cursor="cross", command=lambda: word_into_definitions(entry.get()))
search_but.pack(side='left', padx=51)

root.mainloop()
