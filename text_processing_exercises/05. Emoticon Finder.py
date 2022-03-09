def emoticon(text):
    result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":" and text[i + 1] != " "]
    print('\n'.join(result))


text = input()
emoticon(text)
