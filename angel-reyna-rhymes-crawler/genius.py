import requests
import csv
from bs4 import BeautifulSoup

def get_lyrics_context(word, access_token, num_songs=30, words_around=10):
    base_url = "https://api.genius.com"
    search_url = f"{base_url}/search"
    
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        
        params = {
            'q': word,
        }

        response = requests.get(search_url, headers=headers, params=params)
        data = response.json()

        hits = data.get('response', {}).get('hits', [])
        context_list = []

        for hit in hits[:num_songs]:
            song_url = hit['result']['url']
            response = requests.get(song_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            lyrics_container = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
            if lyrics_container:
                all_words = lyrics_container.get_text(separator=' ').split()

                if word.lower() in all_words:
                    target_word_index = all_words.index(word.lower())

                    start_index = max(0, target_word_index - words_around)
                    end_index = min(len(all_words), target_word_index + words_around + 1)
                    context_words = all_words[start_index:end_index]

                    context_string = ' '.join(context_words)

                    context_list.append(context_string)

        return context_list

    except Exception as e:
        print(f"Error: {e}")
    
    return None

def save_to_csv(word, context_list):
    filename = f"{word}_context.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'context']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, context_string in enumerate(context_list):
            writer.writerow({'word': f'{word}_{i+1}', 'context': context_string})