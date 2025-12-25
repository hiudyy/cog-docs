const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download Twitch clip or VOD
 * @param {string} url - Twitch clip or VOD URL
 */
async function downloadTwitch(url) {
  try {
    const response = await axios.get(`${API_BASE}/twitch/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Twitch Video Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Streamer:', response.data.data.streamer);
      console.log('Type:', response.data.data.type);
      console.log('Game:', response.data.data.game);
      console.log('Views:', response.data.data.views);
      console.log('Download URL:', response.data.data.downloadUrl);
      console.log('Duration:', response.data.data.duration, 'seconds');
      
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
 * Get available formats for Twitch video
 * @param {string} url - Twitch clip or VOD URL
 */
async function getTwitchFormats(url) {
  try {
    const response = await axios.get(`${API_BASE}/twitch/formats`, {
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
 * Get information about Twitch clip or VOD
 * @param {string} url - Twitch clip or VOD URL
 */
async function getTwitchInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/twitch/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Twitch Video Information:');
      console.log('Title:', response.data.info.title);
      console.log('Streamer:', response.data.info.streamer);
      console.log('Type:', response.data.info.type);
      console.log('Game:', response.data.info.game);
      console.log('Views:', response.data.info.views);
      console.log('Duration:', response.data.info.duration, 'seconds');
      console.log('Description:', response.data.info.description);
      
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
  console.log('=== Twitch Download Example ===\n');
  
  // Example 1: Download Twitch clip
  const clipUrl = 'https://clips.twitch.tv/example';
  console.log('Downloading Twitch clip:', clipUrl);
  await downloadTwitch(clipUrl);
  
  console.log('\n=== Twitch Formats Example ===\n');
  
  // Example 2: Get available formats
  const vodUrl = 'https://www.twitch.tv/videos/123456789';
  console.log('Getting formats for:', vodUrl);
  await getTwitchFormats(vodUrl);
  
  console.log('\n=== Twitch Info Example ===\n');
  
  // Example 3: Get video info
  console.log('Getting video info:', clipUrl);
  await getTwitchInfo(clipUrl);
})();

module.exports = {
  downloadTwitch,
  getTwitchFormats,
  getTwitchInfo
};
