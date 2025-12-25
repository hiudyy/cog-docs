const axios = require('axios');

const API_BASE = 'https://cog.api.br/api/v1';

/**
 * Download track/album from Bandcamp
 * @param {string} url - Bandcamp track or album URL
 */
async function downloadBandcamp(url) {
  try {
    const response = await axios.get(`${API_BASE}/bandcamp/download`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Bandcamp Track Downloaded Successfully!');
      console.log('Title:', response.data.data.title);
      console.log('Artist:', response.data.data.artist);
      console.log('Album:', response.data.data.album);
      console.log('Genre:', response.data.data.genre);
      console.log('Track Number:', response.data.data.trackNumber);
      console.log('Download URL:', response.data.data.downloadUrl);
      console.log('Duration:', response.data.data.duration, 'seconds');
      console.log('Release Date:', response.data.data.releaseDate);
      console.log('Format:', response.data.data.ext);
      
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
 * Get available formats for Bandcamp track
 * @param {string} url - Bandcamp track URL
 */
async function getBandcampFormats(url) {
  try {
    const response = await axios.get(`${API_BASE}/bandcamp/formats`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Available Formats:');
      response.data.formats.forEach((format, index) => {
        console.log(`\nFormat ${index + 1}:`);
        console.log('  ID:', format.formatId);
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
 * Get information about Bandcamp track/album
 * @param {string} url - Bandcamp track or album URL
 */
async function getBandcampInfo(url) {
  try {
    const response = await axios.get(`${API_BASE}/bandcamp/info`, {
      params: { url }
    });

    if (response.data.success) {
      console.log('Bandcamp Track Information:');
      console.log('Title:', response.data.info.title);
      console.log('Artist:', response.data.info.artist);
      console.log('Album:', response.data.info.album);
      console.log('Genre:', response.data.info.genre);
      console.log('Duration:', response.data.info.duration, 'seconds');
      console.log('Description:', response.data.info.description);
      console.log('Release Date:', response.data.info.releaseDate);
      
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
  console.log('=== Bandcamp Download Example ===\n');
  
  // Example 1: Download Bandcamp track
  const bandcampUrl = 'https://artist.bandcamp.com/track/example';
  console.log('Downloading from Bandcamp:', bandcampUrl);
  await downloadBandcamp(bandcampUrl);
  
  console.log('\n=== Bandcamp Formats Example ===\n');
  
  // Example 2: Get available formats
  console.log('Getting formats for:', bandcampUrl);
  await getBandcampFormats(bandcampUrl);
  
  console.log('\n=== Bandcamp Info Example ===\n');
  
  // Example 3: Get track info
  console.log('Getting track info:', bandcampUrl);
  await getBandcampInfo(bandcampUrl);
})();

module.exports = {
  downloadBandcamp,
  getBandcampFormats,
  getBandcampInfo
};
