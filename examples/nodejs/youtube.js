const axios = require('axios');
const fs = require('fs');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

async function searchYouTube() {
  try {
    const response = await axios.post(
      `${BASE_URL}/youtube/search`,
      { query: 'javascript tutorial' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(`Found ${response.data.data.count} results\n`);
    response.data.data.results.slice(0, 5).forEach((video, i) => {
      console.log(`${i + 1}. ${video.title}`);
      console.log(`   Channel: ${video.channel.name}`);
      console.log(`   Views: ${video.views.toLocaleString()}`);
      console.log(`   URL: ${video.url}\n`);
    });
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

async function downloadMp3() {
  try {
    const response = await axios.post(
      `${BASE_URL}/youtube/mp3`,
      { url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    const data = response.data.data;
    console.log('Audio downloaded!');
    console.log(`Title: ${data.title}`);
    console.log(`Duration: ${data.duration}s`);
    console.log(`Filename: ${data.filename}`);
    
    // Save file
    const audioBuffer = Buffer.from(data.buffer, 'base64');
    fs.writeFileSync(data.filename, audioBuffer);
    console.log(`Saved to ${data.filename}`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

async function downloadMp4() {
  try {
    const response = await axios.post(
      `${BASE_URL}/youtube/mp4`,
      { 
        url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        quality: '720p'
      },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Video downloaded!');
    console.log(`Title: ${response.data.data.title}`);
    console.log(`Quality: ${response.data.data.quality}`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

searchYouTube();
