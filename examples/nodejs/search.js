const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

/**
 * Pesquisa web geral
 */
async function searchWeb() {
  try {
    const query = 'inteligência artificial';
    
    const response = await axios.get(
      `${BASE_URL}/search`,
      {
        params: { 
          q: query,
          max: 10  // máximo de resultados
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log(`🔍 Pesquisa Web: "${data.query}"`);
    console.log(`   Total de resultados: ${data.totalResults}\n`);
    
    data.results.forEach((result, index) => {
      console.log(`${index + 1}. ${result.title}`);
      console.log(`   URL: ${result.url}`);
      console.log(`   ${result.description.substring(0, 100)}...`);
      console.log('');
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Pesquisa de notícias
 */
async function searchNews() {
  try {
    const query = 'tecnologia brasil';
    
    const response = await axios.get(
      `${BASE_URL}/search/news`,
      {
        params: { 
          q: query,
          max: 5
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log(`📰 Pesquisa de Notícias: "${data.query}"`);
    console.log(`   Total de resultados: ${data.totalResults}\n`);
    
    data.results.forEach((result, index) => {
      console.log(`${index + 1}. ${result.title}`);
      console.log(`   Fonte: ${result.displayUrl}`);
      console.log(`   ${result.description.substring(0, 100)}...`);
      console.log('');
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Pesquisa múltipla (exemplo de uso)
 */
async function multiSearch() {
  const queries = ['programação python', 'machine learning', 'web development'];
  
  console.log('🔎 Pesquisa Múltipla:\n');
  
  for (const query of queries) {
    try {
      const response = await axios.get(
        `${BASE_URL}/search`,
        {
          params: { q: query, max: 3 },
          headers: { 'Authorization': `Bearer ${API_KEY}` }
        }
      );
      
      console.log(`Query: "${query}"`);
      response.data.data.results.forEach(r => {
        console.log(`  • ${r.title}`);
      });
      console.log('');
      
    } catch (error) {
      console.error(`Erro em "${query}":`, error.message);
    }
  }
}

// Executar exemplos
console.log('=== Search API Examples ===\n');
searchWeb();

