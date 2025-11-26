const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog2.cognima.com.br/api/v1';

/**
 * Obter informações completas de um tweet
 */
async function getTweetInfo() {
  try {
    const url = 'https://twitter.com/elonmusk/status/1234567890123456789';
    // Também funciona com x.com:
    // const url = 'https://x.com/elonmusk/status/1234567890123456789';
    
    const response = await axios.get(
      `${BASE_URL}/twitter/info`,
      {
        params: { url },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log('🐦 Tweet Info:');
    console.log(`   ID: ${data.id}`);
    console.log(`   Texto: ${data.text.substring(0, 100)}...`);
    console.log(`   Data: ${data.createdAt}`);
    console.log('\n👤 Autor:');
    console.log(`   Nome: ${data.author.name}`);
    console.log(`   Username: @${data.author.username}`);
    console.log(`   Avatar: ${data.author.avatarUrl}`);
    console.log('\n📊 Estatísticas:');
    console.log(`   Likes: ${data.stats.likes.toLocaleString()}`);
    console.log(`   Retweets: ${data.stats.retweets.toLocaleString()}`);
    console.log(`   Respostas: ${data.stats.replies.toLocaleString()}`);
    console.log(`\n📎 Tipo de Mídia: ${data.type}`);
    console.log(`   Tem Mídia: ${data.hasMedia ? 'Sim' : 'Não'}`);
    
    if (data.media && data.media.length > 0) {
      console.log('\n🎬 Mídias:');
      data.media.forEach((media, index) => {
        console.log(`   ${index + 1}. Tipo: ${media.type}`);
        if (media.type === 'video') {
          console.log(`      Duração: ${media.duration}ms`);
          console.log(`      Melhor qualidade: ${media.bestQuality?.resolution}`);
          console.log(`      URL: ${media.bestQuality?.url || media.url}`);
        } else {
          console.log(`      URL: ${media.url}`);
        }
      });
    }
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Obter links de download direto
 */
async function downloadTwitterMedia() {
  try {
    const url = 'https://twitter.com/user/status/1234567890123456789';
    
    const response = await axios.get(
      `${BASE_URL}/twitter/download`,
      {
        params: { url },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log('✅ Downloads disponíveis:');
    console.log(`   Tweet ID: ${data.tweetId}`);
    console.log(`   Autor: @${data.author}`);
    console.log(`   Tipo: ${data.type}`);
    
    console.log('\n📥 Links de Download:');
    data.downloads.forEach((download, index) => {
      console.log(`   ${index + 1}. Tipo: ${download.type}`);
      if (download.resolution) {
        console.log(`      Resolução: ${download.resolution}`);
      }
      if (download.duration) {
        console.log(`      Duração: ${download.duration}ms`);
      }
      console.log(`      URL: ${download.url}`);
    });
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Download com redirecionamento automático
 */
async function downloadWithRedirect() {
  const url = 'https://twitter.com/user/status/1234567890123456789';
  
  // Com redirect=true, a API redireciona direto para a mídia
  const downloadUrl = `${BASE_URL}/twitter/download?url=${encodeURIComponent(url)}&redirect=true`;
  
  console.log('🔗 URL para download direto:');
  console.log(`   ${downloadUrl}`);
  console.log('   (Adicione o header Authorization para usar)');
}

/**
 * Exemplo de download de diferentes tipos de tweet
 */
async function exampleTypes() {
  console.log('📋 Tipos de mídia suportados:');
  console.log('   • Vídeos (várias resoluções)');
  console.log('   • Fotos (qualidade original)');
  console.log('   • GIFs');
  console.log('\n🔗 Formatos de URL suportados:');
  console.log('   • https://twitter.com/user/status/ID');
  console.log('   • https://x.com/user/status/ID');
  console.log('   • https://twitter.com/i/status/ID');
}

// Executar exemplos
console.log('=== Twitter/X API Examples ===\n');
getTweetInfo();

