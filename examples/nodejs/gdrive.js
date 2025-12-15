const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

/**
 * Obter informações de arquivo do Google Drive
 */
async function getGDriveInfo() {
  try {
    const url = 'https://drive.google.com/file/d/1ABC123xyz/view?usp=sharing';
    
    const response = await axios.get(
      `${BASE_URL}/gdrive/info`,
      {
        params: { url },
        headers: {
          'Authorization': `Bearer ${API_KEY}`
        }
      }
    );
    
    const data = response.data.data;
    console.log('📁 Google Drive File Info:');
    console.log(`   Nome: ${data.fileName}`);
    console.log(`   Tamanho: ${data.fileSize}`);
    console.log(`   Tipo: ${data.mimetype}`);
    console.log(`   Link: ${data.downloadUrl}`);
    
    return data;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Obter link de download do Google Drive
 */
async function downloadGDrive() {
  try {
    const url = 'https://drive.google.com/file/d/1ABC123xyz/view?usp=sharing';
    
    const response = await axios.get(
      `${BASE_URL}/gdrive/download`,
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
 * Exemplo com diferentes formatos de URL
 */
async function testDifferentFormats() {
  const urls = [
    'https://drive.google.com/file/d/FILE_ID/view',
    'https://drive.google.com/open?id=FILE_ID',
    'https://drive.google.com/uc?id=FILE_ID&export=download'
  ];
  
  console.log('🔗 Formatos de URL suportados:');
  urls.forEach((url, i) => {
    console.log(`   ${i + 1}. ${url}`);
  });
}

// Executar exemplos
console.log('=== Google Drive API Examples ===\n');
getGDriveInfo();

