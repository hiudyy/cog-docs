const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

async function searchPinterest() {
  try {
    const response = await axios.post(
      `${BASE_URL}/pinterest/search`,
      { query: 'modern interior design' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(`Found ${response.data.data.count} results`);
    response.data.data.results.slice(0, 5).forEach((item, i) => {
      console.log(`\n${i + 1}. ${item.title}`);
      console.log(`   URL: ${item.link}`);
    });
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

async function downloadPinterest() {
  try {
    const response = await axios.post(
      `${BASE_URL}/pinterest/download`,
      { url: 'https://pinterest.com/pin/123456789/' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Download info:');
    console.log(`Title: ${response.data.data.title}`);
    response.data.data.urls.forEach(urlInfo => {
      console.log(`${urlInfo.quality}: ${urlInfo.url}`);
    });
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

searchPinterest();
