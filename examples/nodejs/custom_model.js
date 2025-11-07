const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

async function createCustomModel() {
  try {
    const response = await axios.post(
      `${BASE_URL}/custom`,
      {
        name: 'js-mentor',
        display_name: 'JavaScript Programming Mentor',
        description: 'Expert JavaScript programming assistant',
        personality_summary: 'You are an expert JavaScript developer with deep knowledge of modern JS, Node.js, and web development. You explain concepts clearly with practical examples.',
        base_model: 'microsoft/phi-3-medium-128k-instruct'
      },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Custom model created!');
    console.log(`Name: ${response.data.data.full_name}`);
    console.log(`ID: ${response.data.data.id}`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

async function useCustomModel() {
  try {
    const response = await axios.post(
      `${BASE_URL}/completion`,
      {
        model: '@cognima/js-mentor',
        messages: [
          { role: 'user', content: 'Explain JavaScript closures with an example' }
        ]
      },
      {
        headers: {
          'X-API-Key': API_KEY,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('\nUsing custom model:');
    console.log(response.data.data.choices[0].message.content);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

// createCustomModel();
useCustomModel();
