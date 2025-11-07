const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

async function getStatus() {
  try {
    const response = await axios.get(`${BASE_URL}/status`, {
      headers: { 'X-API-Key': API_KEY }
    });
    
    const data = response.data.data;
    
    console.log('=== API Key Status ===');
    console.log(`Name: ${data.api_key.name}`);
    console.log(`Active: ${data.api_key.is_active}`);
    
    console.log('\n=== Limits ===');
    console.log(`Hourly: ${data.limits.hourly.remaining}/${data.limits.hourly.limit}`);
    console.log(`Daily Requests: ${data.limits.daily.requests.remaining}/${data.limits.daily.requests.limit}`);
    console.log(`Daily Tokens: ${data.limits.daily.tokens.remaining}/${data.limits.daily.tokens.limit}`);
    
    console.log('\n=== Usage Today ===');
    console.log(`Requests: ${data.usage.today.requests}`);
    console.log(`Tokens: ${data.usage.today.total_tokens.toLocaleString()}`);
    console.log(`Cost: $${data.usage.today.estimated_cost.toFixed(6)}`);
    
    console.log('\n=== Last 30 Days ===');
    console.log(`Requests: ${data.usage.last_30_days.requests.toLocaleString()}`);
    console.log(`Tokens: ${data.usage.last_30_days.total_tokens.toLocaleString()}`);
    console.log(`Cost: $${data.usage.last_30_days.estimated_cost.toFixed(4)}`);
    console.log(`Success Rate: ${data.usage.last_30_days.success_rate}%`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

async function getModelsStats() {
  try {
    const response = await axios.get(`${BASE_URL}/status/models?days=7`, {
      headers: { 'X-API-Key': API_KEY }
    });
    
    const data = response.data.data;
    console.log('\n=== Models Statistics ===');
    console.log(`Total Models: ${data.summary.total_models}`);
    console.log(`Total Requests: ${data.summary.total_requests.toLocaleString()}`);
    console.log(`Total Tokens: ${data.summary.total_tokens.toLocaleString()}`);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

getStatus().then(() => getModelsStats());
