const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download video from Streamable
 * @param {string} url - Streamable video URL
 */
async function downloadStreamable(url) {
  try {
    const response = await axios.get(`${API_BASE}/streamable/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Streamable Video Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Quality:', response.data.data.quality);
      console.log('Download URL:', response.data.data.downloadUrl);
      console.log('Duration:', response.data.data.duration, 'seconds');
      console.log('Resolution:', `${response.data.data.width}x${response.data.data.height}`);
      console.log('Filesize:', (response.data.data.filesize / 1024 / 1024).toFixed(2), 'MB');
      
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
 * Get available formats for Streamable video
 * @param {string} url - Streamable video URL
 */
async function getStreamableFormats(url) {
  try {
    const response = await axios.get(`${API_BASE}/streamable/formats`, {
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
 * Get information about Streamable video
 * @param {string} url - Streamable video URL
 */
async function getStreamableInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/streamable/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Streamable Video Information:');
      console.log('Title:', response.data.info.title);
      console.log('Duration:', response.data.info.duration, 'seconds');
      console.log('Description:', response.data.info.description);
      console.log('Quality:', response.data.info.quality);
      console.log('Filesize:', (response.data.info.filesize / 1024 / 1024).toFixed(2), 'MB');
      
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
  console.log('=== Streamable Download Example ===\n');
  
  // Example 1: Download Streamable video
  const streamableUrl = 'https://streamable.com/example';
  console.log('Downloading from Streamable:', streamableUrl);
  await downloadStreamable(streamableUrl);
  
  console.log('\n=== Streamable Formats Example ===\n');
  
  // Example 2: Get available formats
  console.log('Getting formats for:', streamableUrl);
  await getStreamableFormats(streamableUrl);
  
  console.log('\n=== Streamable Info Example ===\n');
  
  // Example 3: Get video info
  console.log('Getting video info:', streamableUrl);
  await getStreamableInfo(streamableUrl);
})();

module.exports = {
  downloadStreamable,
  getStreamableFormats,
  getStreamableInfo
};
