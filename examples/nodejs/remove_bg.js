const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

async function removeBackground() {
  try {
    const response = await axios.post(
      `${BASE_URL}/image/remove-bg`,
      { url: 'https://files.catbox.moe/ldsyfx.jpg' },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );

    const data = response.data;

    console.log('Remove BG Response:');
    console.log(data);

    if (data?.result?.download) {
      console.log(`\nDownload: ${data.result.download}`);
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

removeBackground();
