import tiktoken
import requests
import openai
from bs4 import BeautifulSoup

if __name__ == '__main__':

    def application_getter(url):
        # get all info from section class = 'panel'
        # return a string
        res = ''
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        panel = soup.find_all('section', class_='panel')

        # get everythong within <section class='panel'>
        for i in panel:
            res += i.text
        return res

    application = input('Enter the Finn url of the application: ')
    application = application_getter(application)



    print('Your application is being written, this might take a while...')

    openai.api_key = ""

    with open('application_paretoH23.txt', 'r') as f:
        example = f.read()

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "system", "content": 'Jeg er 22 år gammel og studerer Informatikk, Matematikk og økonomi ved UiB. Skriv en søknadstekst til denne stillingsannonsen: ' + application + f'bruk {example} som eksempel på en god søknadstekst. Hvis annonsen er på norsk, skriv på norsk, men om den er på engelsk, skriv på engelsk. finn på et eksempel på da jeg viste stor evne til problemløsning og bak det inn i søknaden.'}
                  ]
    )

    chatGPT_assignment_answer = completion["choices"][0]["message"]["content"]

    filename = input(
        'What should the file be saved as? (remember to include filetype) \n (.txt is recommended)')

    with open(filename, 'w') as f:
        f.write(chatGPT_assignment_answer)

    print(f'Your application has been saved as {filename}!')
