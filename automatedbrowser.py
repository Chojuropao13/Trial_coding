import webbrowser as wb

def webauto ():
    internet_path =  #add path chrome,mozilla, microsoft edge disini
    URLS = (
            "https://google.com",
    )

    for url in URLS:
        print("opening :"+ url)
        wb.open(url)

webauto()