const https = require('https');

// Function to extract latest stories from Time.com
function getLatestStories(callback) {
    const url = 'https://time.com/';

    https.get(url, (res) => {
        let data = '';

        // A chunk of data has been received
        res.on('data', (chunk) => {
            data += chunk;
        });

        // The whole response has been received
        res.on('end', () => {
            const latestStories = [];
            const storyRegex = /<a class="headline-link" href="(.?)">(.?)<\/a>/g;
            let match;

            // Extract titles and links using regex
            while ((match = storyRegex.exec(data)) !== null) {
                if (match.length === 3) {
                    latestStories.push({ title: match[2], link: match[1] });
                }
            }

            callback(null, latestStories);
        });
    }).on('error', (err) => {
        console.error('Error fetching data from Time.com:', err);
        callback(err, null);
    });
}

// Example usage
getLatestStories((err, latestStories) => {
    if (err) {
        console.error('Failed to fetch latest stories:', err);
    } else {
        console.log('Latest stories:');
        latestStories.slice(0, 6).forEach((story, index) => {
            console.log('${index + 1}.${story.title}');
            console.log(`   Link: ${story.link}`);
        });
    }
});
