/**
 * Cognima API - Facebook Download Examples (Node.js)
 * 
 * This file demonstrates how to use the Facebook download endpoints
 * to download videos with multiple quality options.
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
 * Download Facebook video (all quality options)
 * @param {string} url - Facebook video URL
 */
async function downloadFacebookVideo(url) {
  try {
    console.log('\n=== Downloading Facebook Video (All Qualities) ===\n');
    console.log(`URL: ${url}\n`);
    
    const response = await api.get('/facebook/download', {
      params: { url }
    });
    
    const { success, videos } = response.data;
    
    if (success) {
      console.log('✅ Download URLs Ready!\n');
      console.log(`Found ${videos.length} quality options:\n`);
      
      videos.forEach((video, index) => {
        console.log(`${index + 1}. Resolution: ${video.resolution}`);
        console.log(`   URL: ${video.url}`);
        console.log(`   Thumbnail: ${video.thumbnail}`);
        console.log(`   Should Render: ${video.shouldRender ? 'Yes' : 'No'}`);
        console.log();
      });
      
      return videos;
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Download Facebook video in best quality (HD preferred)
 * @param {string} url - Facebook video URL
 */
async function downloadFacebookVideoHD(url) {
  try {
    console.log('\n=== Downloading Facebook Video (Best Quality) ===\n');
    console.log(`URL: ${url}\n`);
    
    const response = await api.get('/facebook/download-hd', {
      params: { url }
    });
    
    const { success, video, allQualities } = response.data;
    
    if (success) {
      console.log('✅ Best Quality Download Ready!\n');
      console.log('🎬 Selected Quality:');
      console.log(`   Resolution: ${video.resolution}`);
      console.log(`   URL: ${video.url}`);
      console.log(`   Thumbnail: ${video.thumbnail}`);
      console.log(`   Should Render: ${video.shouldRender ? 'Yes' : 'No'}`);
      console.log(`\n📊 Available Qualities: ${allQualities.length}`);
      
      allQualities.forEach((q, i) => {
        console.log(`   ${i + 1}. ${q.resolution}`);
      });
      
      return video;
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Download multiple Facebook videos
 * @param {Array<string>} urls - Array of Facebook video URLs
 */
async function downloadMultipleVideos(urls) {
  try {
    console.log('\n=== Downloading Multiple Facebook Videos ===\n');
    
    const results = [];
    
    for (const url of urls) {
      try {
        const response = await api.get('/facebook/download-hd', {
          params: { url }
        });
        
        results.push({
          url,
          success: true,
          video: response.data.video
        });
        
        console.log(`✅ Downloaded: ${response.data.video.resolution}`);
      } catch (error) {
        results.push({
          url,
          success: false,
          error: error.response?.data?.error || error.message
        });
        
        console.log(`❌ Failed: ${url}`);
      }
    }
    
    console.log(`\n📋 Downloaded ${results.filter(r => r.success).length}/${urls.length} videos`);
    return results;
  } catch (error) {
    console.error('Error:', error.message);
    throw error;
  }
}

/**
 * Get specific quality from Facebook video
 * @param {string} url - Facebook video URL
 * @param {string} preferredResolution - Preferred resolution (e.g., "720p", "1080p")
 */
async function downloadSpecificQuality(url, preferredResolution) {
  try {
    console.log(`\n=== Downloading Facebook Video (${preferredResolution}) ===\n`);
    console.log(`URL: ${url}\n`);
    
    const response = await api.get('/facebook/download', {
      params: { url }
    });
    
    const { success, videos } = response.data;
    
    if (success) {
      // Find preferred quality
      const video = videos.find(v => 
        v.resolution.toLowerCase().includes(preferredResolution.toLowerCase())
      ) || videos[0];
      
      console.log('✅ Download URL Ready!\n');
      console.log(`Resolution: ${video.resolution}`);
      console.log(`URL: ${video.url}`);
      console.log(`Thumbnail: ${video.thumbnail}`);
      
      return video;
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Get video information without downloading
 * @param {string} url - Facebook video URL
 */
async function getVideoInfo(url) {
  try {
    console.log('\n=== Getting Facebook Video Info ===\n');
    console.log(`URL: ${url}\n`);
    
    const response = await api.get('/facebook/download', {
      params: { url }
    });
    
    const { success, videos } = response.data;
    
    if (success) {
      console.log('📊 Video Information:\n');
      console.log(`Available Qualities: ${videos.length}`);
      
      videos.forEach((video, index) => {
        console.log(`\n${index + 1}. ${video.resolution}`);
        console.log(`   Has Thumbnail: ${video.thumbnail ? 'Yes' : 'No'}`);
        console.log(`   Needs Rendering: ${video.shouldRender ? 'Yes' : 'No'}`);
      });
      
      // Find best quality
      const bestQuality = videos.find(v => v.resolution.includes('1080p')) ||
                         videos.find(v => v.resolution.includes('720p')) ||
                         videos[0];
      
      console.log(`\n🏆 Best Quality: ${bestQuality.resolution}`);
      
      return {
        totalQualities: videos.length,
        qualities: videos.map(v => v.resolution),
        bestQuality: bestQuality.resolution
      };
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Download and compare qualities
 * @param {string} url - Facebook video URL
 */
async function compareQualities(url) {
  try {
    console.log('\n=== Comparing Video Qualities ===\n');
    console.log(`URL: ${url}\n`);
    
    const response = await api.get('/facebook/download', {
      params: { url }
    });
    
    const { success, videos } = response.data;
    
    if (success) {
      console.log('📊 Quality Comparison:\n');
      
      const comparison = videos.map(video => ({
        resolution: video.resolution,
        hasThumbnail: !!video.thumbnail,
        needsRender: video.shouldRender,
        isDirectLink: !video.shouldRender
      }));
      
      console.table(comparison);
      
      return comparison;
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
    const testUrl = 'https://www.facebook.com/share/r/14RStacRcih/';
    
    // Example 1: Download all quality options
    await downloadFacebookVideo(testUrl);
    
    // Example 2: Download best quality (HD preferred)
    await downloadFacebookVideoHD(testUrl);
    
    // Example 3: Download specific quality
    await downloadSpecificQuality(testUrl, '720p');
    
    // Example 4: Get video information
    await getVideoInfo(testUrl);
    
    // Example 5: Compare qualities
    await compareQualities(testUrl);
    
    // Example 6: Download multiple videos
    const urls = [
      'https://www.facebook.com/share/r/14RStacRcih/',
      'https://fb.watch/example123/'
    ];
    await downloadMultipleVideos(urls);
    
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
  downloadFacebookVideo,
  downloadFacebookVideoHD,
  downloadMultipleVideos,
  downloadSpecificQuality,
  getVideoInfo,
  compareQualities
};
