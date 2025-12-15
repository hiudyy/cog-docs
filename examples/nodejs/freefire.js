const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://cog.api.br/api/v1';

/**
 * Get Free Fire Likes service information
 */
async function getServiceInfo() {
  try {
    console.log('=== Free Fire Likes - Service Info ===\n');
    
    const response = await axios.get(`${BASE_URL}/freefire/info`, {
      headers: { 'X-API-Key': API_KEY }
    });
    
    const data = response.data;
    console.log(`Service: ${data.service}`);
    console.log(`Description: ${data.description}`);
    console.log(`Endpoint: ${data.endpoint}`);
    console.log(`\nMin Likes Required: ${data.rules.minLikes}`);
    console.log(`Rule: ${data.rules.minLikesDescription}`);
    
    return data;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Send likes to a Free Fire player
 * @param {string} playerId - Player UID (8-10 digits)
 */
async function sendLikes(playerId) {
  try {
    console.log(`\n=== Sending Likes to Player ${playerId} ===\n`);
    
    const response = await axios.get(`${BASE_URL}/freefire/sendlikes`, {
      params: { playerId },
      headers: { 'X-API-Key': API_KEY }
    });
    
    const { success, data, message } = response.data;
    
    if (success) {
      console.log('✅ Success!');
      console.log(`Player: ${data.player}`);
      console.log(`UID: ${data.uid}`);
      console.log(`Region: ${data.region}`);
      console.log(`Level: ${data.level}`);
      console.log(`\nInitial Likes: ${data.initialLikes.toLocaleString()}`);
      console.log(`Final Likes: ${data.finalLikes.toLocaleString()}`);
      console.log(`Likes Added: ${data.likesAdded}`);
      console.log(`\nUsage Counted: ${data.usageCounted ? 'Yes' : 'No'}`);
      console.log(`Status: ${data.usageStatus}`);
      console.log(`Key Stats: ${data.keystats}`);
    } else {
      console.log('❌ Failed');
      console.log(`Error: ${response.data.error}`);
      console.log(`Message: ${message}`);
      
      if (data) {
        console.log(`\nPlayer: ${data.player}`);
        console.log(`Likes Added: ${data.likesAdded} (less than ${data.minLikesRequired} required)`);
        console.log(`Status: ${data.usageStatus}`);
      }
    }
    
    return response.data;
  } catch (error) {
    if (error.response?.status === 403) {
      console.error('\n❌ Access Denied!');
      console.error('This endpoint requires an API key with daily limit > 500 requests.');
      console.error('Please upgrade to Unlimited or Bot plan.');
    } else if (error.response?.status === 400) {
      console.error('\n❌ Invalid Request!');
      console.error(error.response.data.message);
    } else {
      console.error('\n❌ Error:', error.response?.data || error.message);
    }
    throw error;
  }
}

/**
 * Send likes to multiple players
 * @param {string[]} playerIds - Array of player UIDs
 */
async function sendLikesToMultiplePlayers(playerIds) {
  console.log(`\n=== Sending Likes to ${playerIds.length} Players ===\n`);
  
  const results = {
    successful: [],
    failed: [],
    notCounted: []
  };
  
  for (const playerId of playerIds) {
    try {
      const result = await sendLikes(playerId);
      
      if (result.success && result.data.usageCounted) {
        results.successful.push(playerId);
      } else if (result.success && !result.data.usageCounted) {
        results.notCounted.push(playerId);
      } else {
        results.failed.push(playerId);
      }
      
      // Wait 2 seconds between requests to avoid rate limiting
      await new Promise(resolve => setTimeout(resolve, 2000));
    } catch (error) {
      results.failed.push(playerId);
    }
  }
  
  console.log('\n=== Summary ===');
  console.log(`✅ Successful (counted): ${results.successful.length}`);
  console.log(`⚠️  Successful (not counted): ${results.notCounted.length}`);
  console.log(`❌ Failed: ${results.failed.length}`);
  
  return results;
}

// Example usage
async function main() {
  try {
    // Get service info
    await getServiceInfo();
    
    // Send likes to a single player
    const testPlayerId = '1033857091'; // Replace with actual player UID
    await sendLikes(testPlayerId);
    
    // Uncomment to send likes to multiple players
    // const playerIds = ['1033857091', '1234567890', '9876543210'];
    // await sendLikesToMultiplePlayers(playerIds);
    
  } catch (error) {
    // Error already logged
  }
}

// Run examples
if (require.main === module) {
  main();
}

module.exports = {
  getServiceInfo,
  sendLikes,
  sendLikesToMultiplePlayers
};
