import sys
import time # Using sleep directly from time module

def print_lyrics():
    """
    Prints lyrics line by line with custom delays for each segment,
    with letters appearing one by one within each line.
    """
    # Each tuple contains (lyrics_text, delay_after_line_in_seconds)
    # The letter_delay controls how fast individual letters appear.
    letter_delay = 0.05 # Adjust this value to change how fast letters appear
    line_spacing_delay = 0.8 # Adjust this value for the pause between lines

    lines = [
        ("I wanna da-", line_spacing_delay),
        ("I wanna dance in the lights", line_spacing_delay),
        ("I wanna ro-", line_spacing_delay),
        ("I wanna rock your body", line_spacing_delay),
        ("I wanna go-", line_spacing_delay),
        ("I wanna go for a ride", line_spacing_delay),
        ("Hop in the music and", line_spacing_delay),
        ("Rock your body", line_spacing_delay),
        ("Rock that body", line_spacing_delay),
        ("Come on, come on", line_spacing_delay),
        ("Rock that body", line_spacing_delay),
        ("Rock your body", line_spacing_delay),
        ("Rock that body", line_spacing_delay),
        ("Come on, come on", line_spacing_delay),
        ("Rock that body", line_spacing_delay),
    ]

    print("--- Playing Custom Lyrics (Letter by Letter) ---")
    print("Press Ctrl+C to stop.\n")

    try:
        for text, delay_after_line in lines:
            for char in text:
                sys.stdout.write(char) # Print character without a newline
                sys.stdout.flush()     # Force it to appear immediately
                sleep(letter_delay)    # Pause for each letter
            print() # After printing all characters, move to the next line
            sleep(delay_after_line) # Pause before the next line begins typing

    except KeyboardInterrupt:
        print("\n--- Lyrics playback stopped by user. ---")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n--- End of Custom Lyrics ---")

if __name__ == "__main__":
    # Call the function to start playing the lyrics
    print_lyrics()
