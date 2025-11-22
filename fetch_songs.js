const https = require('https');
const fs = require('fs');

const API_KEY = process.argv[2];

if (!API_KEY) {
    console.error('Please provide a YouTube API key as the first argument.');
    console.error('Usage: node fetch_songs.js <YOUR_API_KEY>');
    process.exit(1);
}

const BANDS = [
    { name: 'Goose', query: 'Goose band songs' },
    { name: 'Geese', query: 'Geese band songs' }
];

const MAX_RESULTS = 35; // Fetch a few more to be safe

function searchYouTube(query, apiKey) {
    return new Promise((resolve, reject) => {
        const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(query)}&type=video&maxResults=${MAX_RESULTS}&key=${apiKey}`;

        https.get(url, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => {
                try {
                    const parsed = JSON.parse(data);
                    if (parsed.error) {
                        reject(parsed.error);
                    } else {
                        resolve(parsed.items);
                    }
                } catch (e) {
                    reject(e);
                }
            });
        }).on('error', (err) => reject(err));
    });
}

async function main() {
    const allSongs = [];

    for (const band of BANDS) {
        console.log(`Fetching songs for ${band.name}...`);
        try {
            const items = await searchYouTube(band.query, API_KEY);

            const songs = items.map(item => ({
                id: `${band.name.toLowerCase()}-${item.id.videoId}`,
                artist: band.name,
                title: item.snippet.title,
                youtubeId: item.id.videoId,
                startTime: 0,
                duration: 15 // Default duration
            }));

            allSongs.push(...songs);
            console.log(`Found ${songs.length} songs for ${band.name}`);
        } catch (err) {
            console.error(`Error fetching for ${band.name}:`, err.message);
        }
    }

    fs.writeFileSync('new_songs.json', JSON.stringify(allSongs, null, 2));
    console.log('Saved songs to new_songs.json');
}

main();
