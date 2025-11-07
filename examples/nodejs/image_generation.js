const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

async function generateImage() {
  try {
    const response = await axios.post(
      `${BASE_URL}/generate`,
      {
        model: 'deepimg',
        prompt: 'A beautiful sunset over mountains, highly detailed',
        size: '1024x1024',
        quality: 'hd'
      },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Image generated successfully!');
    console.log(`URL: ${response.data.data.data[0].url}`);
    console.log(`Cost: $${response.data.usage.estimated_cost.toFixed(6)}`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

generateImage();
