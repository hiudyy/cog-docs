const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download media from a Reddit post
 * @param {string} url - Reddit post URL
 */
async function downloadReddit(url) {
  try {
    const response = await axios.get(`${API_BASE}/reddit/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Reddit Media Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Author:', response.data.data.author);
      console.log('Subreddit:', response.data.data.subreddit);
      console.log('Upvotes:', response.data.data.upvotes);
      console.log('Comments:', response.data.data.comments);
      console.log('Download URL:', response.data.data.downloadUrl);
      console.log('Is Video:', response.data.data.isVideo);
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
 * Get information about a Reddit post
 * @param {string} url - Reddit post URL
 */
async function getRedditInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/reddit/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Reddit Post Information:');
      console.log('Title:', response.data.info.title);
      console.log('Author:', response.data.info.author);
      console.log('Subreddit:', response.data.info.subreddit);
      console.log('Upvotes:', response.data.info.upvotes);
      console.log('Comments:', response.data.info.comments);
      console.log('Is Video:', response.data.info.isVideo);
      console.log('Description:', response.data.info.description);
      console.log('URL:', response.data.info.url);
      
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
  console.log('=== Reddit Download Example ===\n');
  
  // Example 1: Download Reddit video
  const redditUrl = 'https://www.reddit.com/r/videos/comments/example';
  console.log('Downloading from Reddit:', redditUrl);
  await downloadReddit(redditUrl);
  
  console.log('\n=== Reddit Info Example ===\n');
  
  // Example 2: Get post info
  console.log('Getting post info:', redditUrl);
  await getRedditInfo(redditUrl);
})();

module.exports = {
  downloadReddit,
  getRedditInfo
};
