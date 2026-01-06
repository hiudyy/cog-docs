const axios = require('axios');

const BASE_URL = 'https://cog.api.br/api/v1';

/**
 * Search for tracks on Spotify
 * @param {string} query - Track name or artist
 * @param {number} limit - Number of results (default: 10, max: 50)
 */
async function searchSpotify(query, limit = 10) {
  try {
    console.log(`\n=== Searching Spotify: "${query}" ===\n`);
    
    const response = await axios.get(`${BASE_URL}/spotify/search`, {
      params: { 
        q: query, 
        limit 
      }
    });
    
    const { success, platform, total, results } = response.data;
    
    if (success) {
      console.log(`✅ Found ${total} results on ${platform}\n`);
      
      results.forEach(track => {
        console.log(`${track.index}. ${track.name}`);
        console.log(`   Artist(s): ${track.artists}`);
        console.log(`   Link: ${track.link}`);
        console.log('');
      });
      
      return results;
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search for a specific track (returns first result)
 * @param {string} query - Track name or artist
 */
async function searchOneTrack(query) {
  try {
    console.log(`\n=== Searching One Track: "${query}" ===\n`);
    
    const response = await axios.get(`${BASE_URL}/spotify/search-one`, {
      params: { q: query }
    });
    
    const { success, platform, result } = response.data;
    
    if (success) {
      console.log(`✅ Found on ${platform}\n`);
      console.log(`Track: ${result.name}`);
      console.log(`Artist(s): ${result.artists}`);
      console.log(`Link: ${result.link}`);
      
      return result;
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search for multiple tracks from different artists
 * @param {string[]} queries - Array of search queries
 */
async function searchMultipleTracks(queries) {
  console.log('\n=== Searching Multiple Tracks ===\n');
  
  const results = [];
  
  for (const query of queries) {
    try {
      const result = await searchOneTrack(query);
      results.push({ query, result });
      
      // Small delay to avoid rate limiting
      await new Promise(resolve => setTimeout(resolve, 500));
    } catch (error) {
      console.error(`Failed to search: ${query}`);
      results.push({ query, error: error.message });
    }
  }
  
  return results;
}

/**
 * Get track recommendations based on a search
 * @param {string} query - Track name or artist
 * @param {number} count - Number of recommendations
 */
async function getRecommendations(query, count = 5) {
  try {
    console.log(`\n=== Getting ${count} Recommendations for: "${query}" ===\n`);
    
    const response = await axios.get(`${BASE_URL}/spotify/search`, {
      params: { 
        q: query, 
        limit: count 
      }
    });
    
    const { results } = response.data;
    
    console.log('🎵 Recommendations:\n');
    results.forEach((track, index) => {
      console.log(`${index + 1}. ${track.name} - ${track.artists}`);
    });
    
    return results;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Download track from Spotify by URL
 * @param {string} url - Spotify track URL
 * @param {string} outputPath - Optional path to save file
 */
async function downloadTrack(url, outputPath = null) {
  try {
    console.log(`\n=== Downloading Track from Spotify ===\n`);
    console.log(`URL: ${url}\n`);
    
    const response = await axios.get(`${BASE_URL}/spotify/download`, {
      params: { url },
      responseType: 'arraybuffer' // Recebe arquivo binário diretamente
    });
    
    console.log('✅ Download Completo!\n');
    
    // Se especificar caminho, salvar arquivo
    if (outputPath) {
      const fs = require('fs');
      fs.writeFileSync(outputPath, response.data);
      console.log(`💾 Arquivo salvo em: ${outputPath}`);
    }
    
    return {
      success: true,
      buffer: response.data,
      size: response.data.length,
      contentType: response.headers['content-type'],
      filename: response.headers['content-disposition']?.match(/filename="(.+)"/)?.[1] || 'track.mp3'
    };
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search and download track automatically
 * @param {string} query - Track name or artist
 * @param {string} outputPath - Optional path to save file
 */
async function searchAndDownload(query, outputPath = null) {
  try {
    console.log(`\n=== Searching and Downloading: "${query}" ===\n`);
    
    // Primeiro busca para obter informações
    const searchResponse = await axios.get(`${BASE_URL}/spotify/search-one`, {
      params: { q: query }
    });
    
    const { result } = searchResponse.data;
    
    if (result) {
      console.log('✅ Track Found!\n');
      console.log(`   Name: ${result.name}`);
      console.log(`   Artists: ${result.artists}`);
      console.log(`   Link: ${result.link}\n`);
      
      // Agora faz o download
      console.log('⬇️  Starting download...\n');
      const downloadResult = await downloadTrack(result.link, outputPath);
      
      return { track: result, download: downloadResult };
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

// ===================
// EXAMPLES
// ===================

async function main() {
  try {
    // Example 1: Search for multiple tracks
    await searchSpotify('te vi dançando', 5);
    
    // Example 2: Search for a specific track
    await searchOneTrack('Bohemian Rhapsody Queen');
    
    // Example 3: Search multiple different tracks
    const queries = [
      'Blinding Lights',
      'Shape of You',
      'Someone Like You Adele'
    ];
    await searchMultipleTracks(queries);
    
    // Example 4: Get recommendations
    await getRecommendations('acoustic guitar', 5);
    
    // Example 5: Download track by URL (save to file)
    await downloadTrack('https://open.spotify.com/track/4irM0ZydWatEXDDC7SflXS', './downloads/track.mp3');
    
    // Example 6: Search and download automatically (recommended!)
    await searchAndDownload('te vi de canto', './downloads/te_vi_de_canto.mp3');
    
  } catch (error) {
    console.error('Main error:', error.message);
    process.exit(1);
  }
}

// Run examples
if (require.main === module) {
  main();
}

module.exports = {
  searchSpotify,
  searchOneTrack,
  searchMultipleTracks,
  getRecommendations,
  downloadTrack,
  searchAndDownload
};
