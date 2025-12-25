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
 */
async function downloadTrack(url) {
  try {
    console.log(`\n=== Downloading Track from Spotify ===\n`);
    console.log(`URL: ${url}\n`);
    
    const response = await axios.get(`${BASE_URL}/spotify/download`, {
      params: { url }
    });
    
    const { success, data } = response.data;
    
    if (success) {
      console.log('✅ Download Ready!\n');
      console.log(`Title: ${data.title}`);
      console.log(`Artists: ${data.artists.join(', ')}`);
      console.log(`Album: ${data.year}`);
      console.log(`Duration: ${data.duration}`);
      console.log(`\n📥 Download URL: ${data.downloadUrl}`);
      
      return data;
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search and download track automatically
 * @param {string} query - Track name or artist
 */
async function searchAndDownload(query) {
  try {
    console.log(`\n=== Searching and Downloading: "${query}" ===\n`);
    
    const response = await axios.get(`${BASE_URL}/spotify/search-download`, {
      params: { q: query }
    });
    
    const { success, track, download } = response.data;
    
    if (success) {
      console.log('✅ Track Found and Download Ready!\n');
      console.log('🎵 Track Info:');
      console.log(`   Name: ${track.name}`);
      console.log(`   Artists: ${track.artists}`);
      console.log(`   Link: ${track.link}`);
      console.log('\n📥 Download Info:');
      console.log(`   Title: ${download.title}`);
      console.log(`   Artists: ${download.artists.join(', ')}`);
      console.log(`   Album Image: ${download.albumImage}`);
      console.log(`   Year: ${download.year}`);
      console.log(`   Duration: ${download.duration}`);
      console.log(`\n📥 Download URL: ${download.downloadUrl}`);
      
      return { track, download };
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
    
    // Example 5: Download track by URL
    await downloadTrack('https://open.spotify.com/track/4irM0ZydWatEXDDC7SflXS');
    
    // Example 6: Search and download automatically (recommended!)
    await searchAndDownload('te vi de canto');
    
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
