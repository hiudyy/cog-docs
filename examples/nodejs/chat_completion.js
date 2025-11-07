const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

async function chatCompletion() {
  try {
    const response = await axios.post(
      `${BASE_URL}/completion`,
      {
        model: 'microsoft/phi-3-medium-128k-instruct',
        messages: [
          { role: 'system', content: 'You are a helpful assistant.' },
          { role: 'user', content: 'What is artificial intelligence?' }
        ],
        max_tokens: 500,
        temperature: 0.7
      },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Success!');
    console.log(`Model: ${response.data.data.model}`);
    console.log(`Response: ${response.data.data.choices[0].message.content}`);
    console.log(`\nTokens used: ${response.data.usage.total_tokens}`);
    console.log(`Cost: $${response.data.usage.estimated_cost.toFixed(6)}`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

chatCompletion();
