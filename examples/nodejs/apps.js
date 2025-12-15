const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

/**
 * Pesquisar apps em ambas as lojas (Google Play + App Store)
 */
async function searchAllStores() {
  try {
    const query = 'whatsapp';
    
    const response = await axios.get(
      `${BASE_URL}/apps/search`,
      {
        params: { 
          q: query,
          num: 5,
          country: 'br'
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log(`📱 Pesquisa de Apps: "${data.query}"\n`);
    
    console.log('=== Google Play Store ===');
    data.playStore.forEach((app, i) => {
      console.log(`${i + 1}. ${app.title}`);
      console.log(`   Developer: ${app.developer}`);
      console.log(`   Score: ${app.score} | ${app.price}`);
      console.log(`   ID: ${app.appId}`);
      console.log('');
    });
    
    console.log('=== Apple App Store ===');
    data.appStore.forEach((app, i) => {
      console.log(`${i + 1}. ${app.title}`);
      console.log(`   Developer: ${app.developer}`);
      console.log(`   Score: ${app.score} | ${app.free ? 'Free' : app.price}`);
      console.log(`   ID: ${app.appId}`);
      console.log('');
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Pesquisar apenas na Google Play Store
 */
async function searchPlayStore() {
  try {
    const query = 'games';
    
    const response = await axios.get(
      `${BASE_URL}/apps/playstore`,
      {
        params: { 
          q: query,
          num: 5,
          country: 'br',
          lang: 'pt'
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log(`🤖 Google Play Store: "${data.query}"\n`);
    
    data.results.forEach((app, i) => {
      console.log(`${i + 1}. ${app.title}`);
      console.log(`   ${app.developer} | ⭐ ${app.score} | ${app.price}`);
      console.log(`   ${app.summary?.substring(0, 60)}...`);
      console.log('');
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Pesquisar apenas na Apple App Store
 */
async function searchAppStore() {
  try {
    const query = 'music';
    
    const response = await axios.get(
      `${BASE_URL}/apps/appstore`,
      {
        params: { 
          q: query,
          num: 5,
          country: 'br'
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log(`🍎 Apple App Store: "${data.query}"\n`);
    
    data.results.forEach((app, i) => {
      console.log(`${i + 1}. ${app.title}`);
      console.log(`   ${app.developer} | ⭐ ${app.score} | ${app.free ? 'Free' : app.price}`);
      console.log(`   Genres: ${app.genres?.join(', ')}`);
      console.log('');
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Obter detalhes de um app
 */
async function getAppDetails() {
  try {
    const appId = 'com.whatsapp'; // WhatsApp no Play Store
    
    const response = await axios.get(
      `${BASE_URL}/apps/details`,
      {
        params: { 
          appId: appId,
          store: 'playStore',
          country: 'br'
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const app = response.data.data;
    console.log(`📋 Detalhes do App: ${app.title}\n`);
    console.log(`   Developer: ${app.developer}`);
    console.log(`   Score: ⭐ ${app.score} (${app.ratings} avaliações)`);
    console.log(`   Installs: ${app.installs}`);
    console.log(`   Version: ${app.version}`);
    console.log(`   Size: ${app.size}`);
    console.log(`   Android: ${app.androidVersionText}`);
    console.log(`   Updated: ${app.updated}`);
    console.log(`   ${app.summary}`);
    
    return app;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Obter apps similares
 */
async function getSimilarApps() {
  try {
    const appId = 'com.whatsapp';
    
    const response = await axios.get(
      `${BASE_URL}/apps/similar`,
      {
        params: { 
          appId: appId,
          store: 'playStore',
          num: 5
        },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log(`🔗 Apps Similares a "${data.appId}":\n`);
    
    data.results.forEach((app, i) => {
      console.log(`${i + 1}. ${app.title}`);
      console.log(`   ${app.developer} | ⭐ ${app.score}`);
      console.log('');
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

// Executar exemplos
console.log('=== Apps Search API Examples ===\n');
searchAllStores();

