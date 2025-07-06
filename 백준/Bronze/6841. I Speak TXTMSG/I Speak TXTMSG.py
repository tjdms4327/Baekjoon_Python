trans={'CU':'see you', ':-)':"I’m happy", ':-(':"I’m unhappy", ';-)': 'wink',
      ':-P':'stick out my tongue', '(~.~)':'sleepy', 'TA':'totally awesome',
      'CCC':'Canadian Computing Competition', 'CUZ': 'because', 'TY':'thank-you',
      'YW':"you’re welcome", 'TTYL':'talk to you later'}

try:
    while True:
        form=input()
        if form in trans:
            form=trans[form]
        print(form)
except:
    exit(0)