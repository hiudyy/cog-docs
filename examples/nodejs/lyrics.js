const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

async function searchLyrics() {
  try {
    const response = await axios.post(
      `${BASE_URL}/lyrics/search`,
      { query: 'bohemian rhapsody queen' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    const data = response.data.data;
    console.log(`Song: ${data.title}`);
    console.log(`Artist: ${data.artist}`);
    console.log(`Album: ${data.album}`);
    console.log(`Year: ${data.year}`);
    console.log(`\nLyrics:\n${data.lyrics.substring(0, 500)}...`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

searchLyrics();
