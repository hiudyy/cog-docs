const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download video from Dailymotion
 * @param {string} url - Dailymotion video URL
 */
async function downloadDailymotion(url) {
  try {
    const response = await axios.get(`${API_BASE}/dailymotion/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Dailymotion Video Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Author:', response.data.data.author);
      console.log('Quality:', response.data.data.quality);
      console.log('Views:', response.data.data.views);
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
 * Get available formats for Dailymotion video
 * @param {string} url - Dailymotion video URL
 */
async function getDailymotionFormats(url) {
  try {
    const response = await axios.get(`${API_BASE}/dailymotion/formats`, {
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
 * Get information about Dailymotion video
 * @param {string} url - Dailymotion video URL
 */
async function getDailymotionInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/dailymotion/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Dailymotion Video Information:');
      console.log('Title:', response.data.info.title);
      console.log('Author:', response.data.info.author);
      console.log('Views:', response.data.info.views);
      console.log('Duration:', response.data.info.duration, 'seconds');
      console.log('Description:', response.data.info.description);
      console.log('Quality:', response.data.info.quality);
      
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
  console.log('=== Dailymotion Download Example ===\n');
  
  // Example 1: Download Dailymotion video
  const dailymotionUrl = 'https://www.dailymotion.com/video/x8example';
  console.log('Downloading from Dailymotion:', dailymotionUrl);
  await downloadDailymotion(dailymotionUrl);
  
  console.log('\n=== Dailymotion Formats Example ===\n');
  
  // Example 2: Get available formats
  console.log('Getting formats for:', dailymotionUrl);
  await getDailymotionFormats(dailymotionUrl);
  
  console.log('\n=== Dailymotion Info Example ===\n');
  
  // Example 3: Get video info
  console.log('Getting video info:', dailymotionUrl);
  await getDailymotionInfo(dailymotionUrl);
})();

module.exports = {
  downloadDailymotion,
  getDailymotionFormats,
  getDailymotionInfo
};
