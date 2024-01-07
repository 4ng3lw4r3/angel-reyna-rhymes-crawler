from genius import get_lyrics_context, save_to_csv
import time

def example():
    word_to_search = "myliu"
    genius_access_token = "ZaPD3fRtXHq6TGHdZFC6TO7VPxTNV9bJpAiS95RnGyMXS3xqEj4FQ9ehzBBG3XuF"
    
    start_time = time.time()
    context_list = get_lyrics_context(word_to_search, genius_access_token, num_songs=30, words_around=10)
    
    if context_list:
        save_to_csv(word_to_search, context_list)
        elapsed_time = time.time() - start_time
        print(f"Context saved to CSV in {elapsed_time:.2f} seconds.")
    else:
        print(f"Failed to retrieve context for the word: {word_to_search}")

if __name__ == "__main__":
    example()
