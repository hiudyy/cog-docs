const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

/**
 * Obter informações de arquivo do MediaFire
 */
async function getMediaFireInfo() {
  try {
    const url = 'https://www.mediafire.com/file/abc123xyz/arquivo.zip/file';
    
    const response = await axios.get(
      `${BASE_URL}/mediafire/info`,
      {
        params: { url },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log('📁 MediaFire File Info:');
    console.log(`   Nome: ${data.fileName}`);
    console.log(`   Tamanho: ${data.fileSize}`);
    console.log(`   Data Upload: ${data.uploadDate}`);
    console.log(`   Tipo: ${data.mimetype}`);
    console.log(`   Extensão: ${data.extension}`);
    console.log(`   Link: ${data.downloadUrl}`);
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Obter link de download do MediaFire
 */
async function downloadMediaFire() {
  try {
    const url = 'https://www.mediafire.com/file/abc123xyz/arquivo.zip/file';
    
    const response = await axios.get(
      `${BASE_URL}/mediafire/download`,
      {
        params: { url },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log('✅ Download disponível:');
    console.log(`   Arquivo: ${data.fileName}`);
    console.log(`   URL: ${data.downloadUrl}`);
    
    // Para redirecionar diretamente, use: params: { url, redirect: 'true' }
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Download com redirecionamento automático
 */
async function downloadWithRedirect() {
  try {
    const url = 'https://www.mediafire.com/file/abc123xyz/arquivo.zip/file';
    
    // Com redirect=true, a API redireciona direto para o arquivo
    const downloadUrl = `${BASE_URL}/mediafire/download?url=${encodeURIComponent(url)}&redirect=true`;
    
    console.log('🔗 URL para download direto:');
    console.log(`   ${downloadUrl}`);
    console.log('   (Adicione o header Authorization para usar)');
    
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

// Executar exemplos
console.log('=== MediaFire API Examples ===\n');
getMediaFireInfo();

