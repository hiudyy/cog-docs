/**
 * Cognima API - SoundCloud Examples (Node.js)
 * 
 * This file demonstrates how to use the SoundCloud endpoints
 * to search and download tracks.
 */

const axios = require('axios');

// API Configuration
const BASE_URL = 'https://cog.api.br/api/v1';
const API_KEY = 'YOUR_API_KEY_HERE';

// Configure axios with API key
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'apikey': API_KEY
  }
});

/**
 * Search for tracks on SoundCloud
 * @param {string} query - Track name or artist
 * @param {number} limit - Number of results
 */
async function searchSoundCloud(query, limit = 10) {
  try {
    console.log(`\n=== Searching SoundCloud: "${query}" ===\n`);
    
    const response = await api.get('/soundcloud/search', {
      params: { 
        q: query, 
        limit 
      }
    });
    
    const { total, results } = response.data;
    
    console.log(`Found ${total} results:\n`);
    
    results.forEach((track, index) => {
      console.log(`${index + 1}. ${track.title}`);
      console.log(`   Artist ID: ${track.artist}`);
      console.log(`   Duration: ${track.duration}s`);
      console.log(`   Plays: ${track.playback_count.toLocaleString()}`);
      console.log(`   Likes: ${track.likes_count.toLocaleString()}`);
      console.log(`   URL: ${track.permalink_url}`);
      console.log();
    });
    
    return results;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search for a specific track
 * @param {string} query - Track name or artist
 */
async function searchOneTrack(query) {
  try {
    console.log(`\n=== Searching One Track: "${query}" ===\n`);
    
    const response = await api.get('/soundcloud/search-one', {
      params: { q: query }
    });
    
    const { result } = response.data;
    
    console.log('✅ Track found:\n');
    console.log(`Title: ${result.title}`);
    console.log(`Artist ID: ${result.artist}`);
    console.log(`Duration: ${result.duration}s`);
    console.log(`Plays: ${result.playback_count.toLocaleString()}`);
    console.log(`Likes: ${result.likes_count.toLocaleString()}`);
    console.log(`Genre: ${result.genre}`);
    console.log(`URL: ${result.permalink_url}`);
    
    return result;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search for multiple different tracks
 * @param {Array<string>} queries - Array of track names
 */
async function searchMultipleTracks(queries) {
  try {
    console.log('\n=== Searching Multiple Tracks ===\n');
    
    const allResults = [];
    
    for (const query of queries) {
      const response = await api.get('/soundcloud/search-one', {
        params: { q: query }
      });
      
      allResults.push(response.data.result);
      console.log(`✅ Found: ${response.data.result.title}`);
    }
    
    console.log(`\n📋 Total tracks found: ${allResults.length}`);
    return allResults;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Get track recommendations based on a search
 * @param {string} query - Track name or artist
 * @param {number} count - Number of recommendations
 */
async function getRecommendations(query, count = 5) {
  try {
    console.log(`\n=== Getting ${count} Recommendations for: "${query}" ===\n`);
    
    const response = await api.get('/soundcloud/search', {
      params: { 
        q: query, 
        limit: count 
      }
    });
    
    const { results } = response.data;
    
    console.log('🎵 Recommendations:\n');
    results.forEach((track, index) => {
      console.log(`${index + 1}. ${track.title}`);
      console.log(`   Plays: ${track.playback_count.toLocaleString()} | Likes: ${track.likes_count.toLocaleString()}`);
    });
    
    return results;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Download track from SoundCloud by URL
 * @param {string} url - SoundCloud track URL
 */
async function downloadTrack(url) {
  try {
    console.log(`\n=== Downloading Track from SoundCloud ===\n`);
    console.log(`URL: ${url}\n`);
    
    const response = await api.get('/soundcloud/download', {
      params: { url }
    });
    
    const { success, data } = response.data;
    
    if (success) {
      console.log('✅ Download Ready!\n');
      console.log(`Title: ${data.title}`);
      console.log(`Artist: ${data.artist}`);
      console.log(`Thumbnail: ${data.thumbnail}`);
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
    
    const response = await api.get('/soundcloud/search-download', {
      params: { q: query }
    });
    
    const { success, track, download } = response.data;
    
    if (success) {
      console.log('✅ Track Found and Download Ready!\n');
      console.log('🎵 Track Info:');
      console.log(`   Title: ${track.title}`);
      console.log(`   Artist ID: ${track.artist}`);
      console.log(`   Duration: ${track.duration}s`);
      console.log(`   Plays: ${track.playback_count.toLocaleString()}`);
      console.log(`   Likes: ${track.likes_count.toLocaleString()}`);
      console.log(`   URL: ${track.permalink_url}`);
      console.log('\n📥 Download Info:');
      console.log(`   Title: ${download.title}`);
      console.log(`   Artist: ${download.artist}`);
      console.log(`   Thumbnail: ${download.thumbnail}`);
      console.log(`\n📥 Download URL: ${download.downloadUrl}`);
      
      return { track, download };
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Search by genre and get top tracks
 * @param {string} genre - Genre name
 * @param {number} limit - Number of results
 */
async function searchByGenre(genre, limit = 10) {
  try {
    console.log(`\n=== Searching ${genre} tracks ===\n`);
    
    const response = await api.get('/soundcloud/search', {
      params: { 
        q: genre, 
        limit 
      }
    });
    
    const { results } = response.data;
    
    console.log(`🎵 Top ${genre} Tracks:\n`);
    results.forEach((track, index) => {
      console.log(`${index + 1}. ${track.title}`);
      console.log(`   Genre: ${track.genre}`);
      console.log(`   Plays: ${track.playback_count.toLocaleString()}`);
    });
    
    return results;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Get trending tracks based on play count
 * @param {string} query - Search query
 * @param {number} limit - Number of results
 */
async function getTrendingTracks(query, limit = 10) {
  try {
    console.log(`\n=== Getting Trending Tracks: "${query}" ===\n`);
    
    const response = await api.get('/soundcloud/search', {
      params: { 
        q: query, 
        limit 
      }
    });
    
    const { results } = response.data;
    
    // Sort by playback count
    const trending = results.sort((a, b) => b.playback_count - a.playback_count);
    
    console.log('🔥 Trending Tracks:\n');
    trending.forEach((track, index) => {
      console.log(`${index + 1}. ${track.title}`);
      console.log(`   Plays: ${track.playback_count.toLocaleString()}`);
      console.log(`   Likes: ${track.likes_count.toLocaleString()}`);
    });
    
    return trending;
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
    await searchSoundCloud('te vi de canto', 5);
    
    // Example 2: Search for a specific track
    await searchOneTrack('te vi dançando');
    
    // Example 3: Search multiple different tracks
    const queries = [
      'lofi hip hop',
      'deep house mix',
      'ambient music'
    ];
    await searchMultipleTracks(queries);
    
    // Example 4: Get recommendations
    await getRecommendations('electronic music', 5);
    
    // Example 5: Download track by URL
    await downloadTrack('https://soundcloud.com/jose-luiiz-ii/ro-rosa-te-vi-de-canto-prod');
    
    // Example 6: Search and download automatically (recommended!)
    await searchAndDownload('te vi de canto');
    
    // Example 7: Search by genre
    await searchByGenre('hip hop', 5);
    
    // Example 8: Get trending tracks
    await getTrendingTracks('remix', 5);
    
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
  searchSoundCloud,
  searchOneTrack,
  searchMultipleTracks,
  getRecommendations,
  downloadTrack,
  searchAndDownload,
  searchByGenre,
  getTrendingTracks
};
