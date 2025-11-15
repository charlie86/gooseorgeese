# Goose or Geese

A deadpan web application to test your ability to distinguish between the bands Goose and Geese.

## Setup

1. **Add Song URLs**: Edit `script.js` and replace the placeholder YouTube URLs with actual song URLs. You can use:
   - Direct audio file URLs (MP3, etc.)
   - YouTube embed URLs
   - Spotify embed URLs
   - Or any other audio source

2. **Open the app**: Simply open `index.html` in a web browser.

## How to Add Real Songs

### Option 1: YouTube Videos
Replace the URLs in `script.js` with actual YouTube video IDs:
```javascript
{ title: "Hungersite", url: "https://www.youtube.com/watch?v=ACTUAL_VIDEO_ID" }
```

### Option 2: Direct Audio Files
If you have audio files, place them in the project folder and reference them:
```javascript
{ title: "Hungersite", url: "./audio/goose-hungersite.mp3" }
```

### Option 3: Spotify Embeds
You can also use Spotify track URLs if you modify the audio player to use iframe embeds.

## How It Works

1. Click "Play Random Song" to start
2. Listen to the song
3. Click either "Goose" or "Geese" to make your guess
4. Receive deadpan feedback
5. Your score is tracked

## Notes

- The humor derives from the deadpan presentation of this absurdly specific challenge
- Both bands are real: Goose (jam band) and Geese (indie rock)
- You'll need to source actual audio legally for this to work
