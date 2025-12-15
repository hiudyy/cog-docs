const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

async function downloadTikTok() {
  try {
    const response = await axios.post(
      `${BASE_URL}/tiktok/download`,
      { url: 'https://www.tiktok.com/@user/video/1234567890' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    const data = response.data.data;
    console.log('TikTok Video Info:');
    console.log(`Title: ${data.title}`);
    console.log(`Author: ${data.author.username}`);
    console.log(`Views: ${data.stats.views.toLocaleString()}`);
    console.log(`Likes: ${data.stats.likes.toLocaleString()}`);
    console.log('\nDownload URLs:');
    data.urls.forEach(video => {
      console.log(`${video.quality}: ${video.url}`);
    });
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

async function searchTikTok() {
  try {
    const response = await axios.post(
      `${BASE_URL}/tiktok/search`,
      { query: 'cooking recipes' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Search results:');
    console.log(response.data.data);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

downloadTikTok();
