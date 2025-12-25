const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download all available media from any URL
 * @param {string} url - Any URL supported by yt-dlp
 */
async function downloadAllMedia(url) {
  try {
    const response = await axios.get(`${API_BASE}/alldl`, {
      params: { url }
    });

    if (response.data.success) {
      const { metadata, media, totalItems, videoCount, audioCount, imageCount } = response.data.data;
      
      console.log('=== METADATA ===');
      console.log('Title:', metadata.title);
      console.log('Platform:', metadata.platform);
      console.log('Duration:', metadata.duration, 'seconds');
      console.log('Views:', metadata.views);
      console.log('Uploader:', metadata.uploader);
      
      console.log('\n=== SUMMARY ===');
      console.log('Total Items:', totalItems);
      console.log('Videos:', videoCount);
      console.log('Audio:', audioCount);
      console.log('Images:', imageCount);
      
      console.log('\n=== ALL MEDIA ===');
      media.forEach((item, index) => {
        console.log(`\n[${index + 1}] ${item.type.toUpperCase()}`);
        console.log('  URL:', item.url.substring(0, 60) + '...');
        console.log('  Quality:', item.quality);
        console.log('  Format:', item.format);
        if (item.filesize) {
          console.log('  Size:', (item.filesize / 1024 / 1024).toFixed(2), 'MB');
        }
        if (item.isBest) {
          console.log('  ⭐ BEST QUALITY');
        }
      });
      
      return response.data.data;
    } else {
      console.error('Error:', response.data.error);
      return null;
    }
  } catch (error) {
    console.error('Request Error:', error.response?.data || error.message);
    return null;
  }
}

/**
 * Download media filtered by type
 * @param {string} url - Any URL supported by yt-dlp
 * @param {string} type - Media type: 'video', 'audio', or 'image'
 */
async function downloadByType(url, type) {
  try {
    const response = await axios.get(`${API_BASE}/alldl/type`, {
      params: { url, type }
    });

    if (response.data.success) {
      const { metadata, media, totalItems } = response.data.data;
      
      console.log('=== METADATA ===');
      console.log('Title:', metadata.title);
      console.log('Platform:', metadata.platform);
      
      console.log(`\n=== ${type.toUpperCase()} ONLY (${totalItems} items) ===`);
      media.forEach((item, index) => {
        console.log(`\n[${index + 1}] ${item.type.toUpperCase()}`);
        console.log('  URL:', item.url.substring(0, 60) + '...');
        console.log('  Quality:', item.quality);
        console.log('  Format:', item.format);
        
        if (type === 'video' && item.resolution) {
          console.log('  Resolution:', item.resolution);
          console.log('  FPS:', item.fps);
          console.log('  Codec:', item.vcodec);
        }
        
        if (type === 'audio') {
          console.log('  Codec:', item.acodec);
          console.log('  Bitrate:', item.abr, 'kbps');
          console.log('  Sample Rate:', item.asr, 'Hz');
        }
        
        if (type === 'image' && item.width) {
          console.log('  Resolution:', `${item.width}x${item.height}`);
        }
        
        if (item.filesize) {
          console.log('  Size:', (item.filesize / 1024 / 1024).toFixed(2), 'MB');
        }
      });
      
      return response.data.data;
    } else {
      console.error('Error:', response.data.error);
      return null;
    }
  } catch (error) {
    console.error('Request Error:', error.response?.data || error.message);
    return null;
  }
}

/**
 * Get only the best quality video
 * @param {string} url - Any URL supported by yt-dlp
 */
async function getBestQuality(url) {
  try {
    const response = await axios.get(`${API_BASE}/alldl`, {
      params: { url }
    });

    if (response.data.success) {
      const { media } = response.data.data;
      const best = media.find(m => m.isBest);
      
      if (best) {
        console.log('=== BEST QUALITY ===');
        console.log('Type:', best.type);
        console.log('Quality:', best.quality);
        console.log('Format:', best.format);
        console.log('Download URL:', best.url);
        
        return best;
      }
    }
    return null;
  } catch (error) {
    console.error('Request Error:', error.response?.data || error.message);
    return null;
  }
}

// Example usage
(async () => {
  // Example 1: Download all media
  console.log('=== EXAMPLE 1: ALL MEDIA ===\n');
  const youtubeUrl = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
  await downloadAllMedia(youtubeUrl);
  
  console.log('\n\n=== EXAMPLE 2: AUDIO ONLY ===\n');
  await downloadByType(youtubeUrl, 'audio');
  
  console.log('\n\n=== EXAMPLE 3: IMAGES ONLY ===\n');
  await downloadByType(youtubeUrl, 'image');
  
  console.log('\n\n=== EXAMPLE 4: BEST QUALITY ===\n');
  await getBestQuality(youtubeUrl);
  
  console.log('\n\n=== EXAMPLE 5: OTHER PLATFORMS ===\n');
  
  // TikTok
  console.log('\n--- TikTok ---');
  await downloadAllMedia('https://www.tiktok.com/@user/video/123456789');
  
  // Vimeo
  console.log('\n--- Vimeo ---');
  await downloadAllMedia('https://vimeo.com/123456789');
  
  // SoundCloud
  console.log('\n--- SoundCloud ---');
  await downloadByType('https://soundcloud.com/artist/track', 'audio');
})();

module.exports = {
  downloadAllMedia,
  downloadByType,
  getBestQuality
};
