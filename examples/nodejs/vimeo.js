const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download video from Vimeo
 * @param {string} url - Vimeo video URL
 */
async function downloadVimeo(url) {
  try {
    const response = await axios.get(`${API_BASE}/vimeo/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Vimeo Video Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Author:', response.data.data.author);
      console.log('Quality:', response.data.data.quality);
      console.log('Views:', response.data.data.views);
      console.log('Likes:', response.data.data.likes);
      console.log('Download URL:', response.data.data.downloadUrl);
      console.log('Duration:', response.data.data.duration, 'seconds');
      console.log('Resolution:', `${response.data.data.width}x${response.data.data.height}`);
      
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
 * Get available formats for Vimeo video
 * @param {string} url - Vimeo video URL
 */
async function getVimeoFormats(url) {
  try {
    const response = await axios.get(`${API_BASE}/vimeo/formats`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Available Formats:');
      response.data.formats.forEach((format, index) => {
        console.log(`\nFormat ${index + 1}:`);
        console.log('  ID:', format.formatId);
        console.log('  Quality:', format.quality);
        console.log('  Extension:', format.ext);
        console.log('  Size:', (format.filesize / 1024 / 1024).toFixed(2), 'MB');
      });
      
      return response.data.formats;
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
 * Get information about Vimeo video
 * @param {string} url - Vimeo video URL
 */
async function getVimeoInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/vimeo/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Vimeo Video Information:');
      console.log('Title:', response.data.info.title);
      console.log('Author:', response.data.info.author);
      console.log('Views:', response.data.info.views);
      console.log('Likes:', response.data.info.likes);
      console.log('Duration:', response.data.info.duration, 'seconds');
      console.log('Description:', response.data.info.description);
      console.log('Resolution:', `${response.data.info.width}x${response.data.info.height}`);
      
      return response.data.info;
    } else {
      console.error('Error:', response.data.error);
      return null;
    }
  } catch (error) {
    console.error('Request Error:', error.response?.data || error.message);
    return null;
  }
}

// Example usage
(async () => {
  console.log('=== Vimeo Download Example ===\n');
  
  // Example 1: Download Vimeo video
  const vimeoUrl = 'https://vimeo.com/123456789';
  console.log('Downloading from Vimeo:', vimeoUrl);
  await downloadVimeo(vimeoUrl);
  
  console.log('\n=== Vimeo Formats Example ===\n');
  
  // Example 2: Get available formats
  console.log('Getting formats for:', vimeoUrl);
  await getVimeoFormats(vimeoUrl);
  
  console.log('\n=== Vimeo Info Example ===\n');
  
  // Example 3: Get video info
  console.log('Getting video info:', vimeoUrl);
  await getVimeoInfo(vimeoUrl);
})();

module.exports = {
  downloadVimeo,
  getVimeoFormats,
  getVimeoInfo
};
