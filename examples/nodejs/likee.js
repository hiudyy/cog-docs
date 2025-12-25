const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download video from Likee
 * @param {string} url - Likee video URL
 */
async function downloadLikee(url) {
  try {
    const response = await axios.get(`${API_BASE}/likee/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Likee Video Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Author:', response.data.data.author);
      console.log('Views:', response.data.data.views);
      console.log('Likes:', response.data.data.likes);
      console.log('Comments:', response.data.data.comments);
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
 * Get information about Likee video
 * @param {string} url - Likee video URL
 */
async function getLikeeInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/likee/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Likee Video Information:');
      console.log('Title:', response.data.info.title);
      console.log('Author:', response.data.info.author);
      console.log('Views:', response.data.info.views);
      console.log('Likes:', response.data.info.likes);
      console.log('Comments:', response.data.info.comments);
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
  console.log('=== Likee Download Example ===\n');
  
  // Example 1: Download Likee video
  const likeeUrl = 'https://likee.video/@username/video/123456';
  console.log('Downloading from Likee:', likeeUrl);
  await downloadLikee(likeeUrl);
  
  console.log('\n=== Likee Info Example ===\n');
  
  // Example 2: Get video info
  console.log('Getting video info:', likeeUrl);
  await getLikeeInfo(likeeUrl);
})();

module.exports = {
  downloadLikee,
  getLikeeInfo
};
