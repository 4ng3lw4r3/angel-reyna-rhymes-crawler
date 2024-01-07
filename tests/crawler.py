import requests
from bs4 import BeautifulSoup
import csv
import time

def get_lyrics(word):
    base_url = "https://genius.com"
    search_url = f"{base_url}/search?q={word}"
    
    try:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        first_result = soup.find('a', class_='song_link')
        
        if first_result:
            song_url = base_url + first_result['href']
            
            response = requests.get(song_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            lyrics = soup.find('div', class_='lyrics').get_text()

            return lyrics.strip()

    except Exception as e:
        print(f"Error: {e}")
    
    return None

def save_to_csv(word, lyrics):
    filename = f"{word}_lyrics.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['word', 'lyrics']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'word': word, 'lyrics': lyrics})

def main():
    word_to_search = "your_specific_word"
    
    start_time = time.time()
    lyrics = get_lyrics(word_to_search)
    
    if lyrics:
        save_to_csv(word_to_search, lyrics)
        elapsed_time = time.time() - start_time
        print(f"Lyrics saved to CSV in {elapsed_time:.2f} seconds.")
    else:
        print("Failed to retrieve lyrics.")

if __name__ == "__main__":
    main()
