# Project: Goose or Geese?

## Overview
A web-based game where players guess whether a song snippet is by the band **Goose** or the band **Geese**.

## Architecture
- **Frontend**: Vanilla HTML/CSS/JS.
- **Data**: `songs.js` contains the song database as a JavaScript array.
- **Tools**: Python scripts for data management.

## Key Files
- `index.html`: Main game interface.
- `main.js`: Game logic (YouTube IFrame API integration, scoring, state management).
- `songs.js`: Source of truth for song data.
- `fetch_songs.py`: Utility to fetch new songs from YouTube Data API.
  - **Usage**: `python3 fetch_songs.py`
  - **Auth**: Requires `YOUTUBE_API_KEY` environment variable.
  - **Features**: Pagination support, basic filtering, random start time calculation.

## Data Management Workflow
To expand the song library:
1.  **Fetch**: Run `fetch_songs.py` to query the YouTube API.
2.  **Filter**: The data must be strictly filtered to ensure only actual songs are included.
    - **Exclude**: Interviews, full shows, "thoughts on" commentary, reviews, reactions, shorts, and fan covers.
    - **Include**: Official Music Videos, Official Audio, Official Visualizers, and high-quality live individual tracks.
3.  **Merge**: Valid unique songs are appended to the `songs` array in `songs.js`.

## User Preferences & Context
- **Content Quality**: High priority on cleaning the dataset. The user dislikes non-music content cluttering the game.
- **Bands**:
    - **Goose**: Jam band / Indie Groove.
    - **Geese**: Post-punk / Indie Rock.
- **Environment**: YouTube API Key is configured in the user's environment (`~/.zshrc`).

## Recent History
- **UI**: Updated footer text to be dynamic ("Name that fowl foursome!" during play). Added mobile layout styles.
- **Data Expansion**: Increased library size from ~50 to ~270 songs using the YouTube API with pagination.
- **Data Cleaning**:
    - Fixed HTML entities in titles (e.g., `&amp;`).
    - Aggressively filtered out "full shows", "interviews", and social media style content (hashtags, "my thoughts").
