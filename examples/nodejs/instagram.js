const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

async function downloadInstagram() {
  try {
    const response = await axios.post(
      `${BASE_URL}/instagram/download`,
      { url: 'https://www.instagram.com/p/ABC123xyz/' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    const data = response.data.data;
    console.log('Instagram Post Info:');
    console.log(`Type: ${data.type}`);
    console.log(`Caption: ${data.caption}`);
    console.log(`Author: ${data.author.username}`);
    console.log(`Likes: ${data.likes.toLocaleString()}`);
    console.log('\nMedia URLs:');
    data.media.forEach((media, i) => {
      console.log(`${i + 1}. ${media.type}: ${media.url}`);
    });
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

downloadInstagram();
