const axios = require('axios');

const API_KEY = process.env.COGNIMA_API_KEY || 'ck_your_api_key';
const BASE_URL = 'https://consultas.cog.api.br/api/v1';

/**
 * Check Telegram bot connection status
 */
async function checkStatus() {
  try {
    console.log('=== Checking Telegram Bot Status ===\n');
    
    const response = await axios.get(`${BASE_URL}/consulta/status`, {
      headers: { 'X-API-Key': API_KEY }
    });
    
    const data = response.data;
    console.log(`Status: ${data.status}`);
    console.log(`Message: ${data.message}`);
    console.log(`Timestamp: ${data.timestamp}`);
    
    return data;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
    throw error;
  }
}

/**
 * Perform a data query
 * @param {string} type - Query type (cpf, nome, telefone, etc.)
 * @param {string} data - Data to query
 */
async function performQuery(type, data) {
  try {
    console.log(`\n=== Query: ${type.toUpperCase()} ===`);
    console.log(`Data: ${data}\n`);
    
    const response = await axios.get(`${BASE_URL}/consulta`, {
      params: { type, dados: data },
      headers: { 'X-API-Key': API_KEY }
    });
    
    const result = response.data;
    
    if (result.success) {
      console.log('✅ Query successful!');
      console.log(`Type: ${result.data.type}`);
      console.log(`Query: ${result.data.query}`);
      console.log(`Timestamp: ${result.data.timestamp}`);
      console.log('\n--- Result ---');
      console.log(result.data.resultado);
    } else {
      console.log('❌ Query failed');
      console.log(`Error: ${result.error}`);
      console.log(`Message: ${result.message}`);
    }
    
    return result;
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
 * Query by CPF
 */
async function queryByCPF(cpf) {
  console.log('\n=== CPF Query ===');
  return performQuery('cpf', cpf);
}

/**
 * Query by name
 */
async function queryByName(name) {
  console.log('\n=== Name Query ===');
  return performQuery('nome', name);
}

/**
 * Query by phone
 */
async function queryByPhone(phone) {
  console.log('\n=== Phone Query ===');
  return performQuery('telefone', phone);
}

/**
 * Query by email
 */
async function queryByEmail(email) {
  console.log('\n=== Email Query ===');
  return performQuery('email', email);
}

/**
 * Query by vehicle plate
 */
async function queryByPlate(plate) {
  console.log('\n=== Vehicle Plate Query ===');
  return performQuery('placa', plate);
}

/**
 * Query by CNPJ
 */
async function queryByCNPJ(cnpj) {
  console.log('\n=== CNPJ Query ===');
  return performQuery('cnpj', cnpj);
}

/**
 * Query neighbors by CPF
 */
async function queryNeighbors(cpf) {
  console.log('\n=== Neighbors Query ===');
  return performQuery('vizinhos', cpf);
}

/**
 * Query relatives by CPF
 */
async function queryRelatives(cpf) {
  console.log('\n=== Relatives Query ===');
  return performQuery('parentes', cpf);
}

/**
 * Query addresses by CPF
 */
async function queryAddresses(cpf) {
  console.log('\n=== Addresses Query ===');
  return performQuery('enderecos', cpf);
}

/**
 * Query jobs by CPF
 */
async function queryJobs(cpf) {
  console.log('\n=== Jobs Query ===');
  return performQuery('empregos', cpf);
}

// Example usage
async function main() {
  try {
    // Check status first
    await checkStatus();
    
    // Example queries (replace with real data)
    
    // CPF query
    // await queryByCPF('00000000000');
    
    // Name query
    // await queryByName('João Silva');
    
    // Phone query
    // await queryByPhone('11999999999');
    
    // Email query
    // await queryByEmail('example@email.com');
    
    // Vehicle plate query
    // await queryByPlate('ABC1234');
    
    // CNPJ query
    // await queryByCNPJ('00000000000000');
    
    // Advanced queries
    // await queryNeighbors('00000000000');
    // await queryRelatives('00000000000');
    // await queryAddresses('00000000000');
    // await queryJobs('00000000000');
    
    console.log('\n✅ Examples completed!');
    console.log('\nAvailable query types:');
    console.log('- cpf, nome, telefone, email');
    console.log('- placa, chassi, cnpj, cep');
    console.log('- titulo, pai, mae');
    console.log('- vizinhos, proprietario, empregos, vacinas');
    console.log('- beneficios, internet, parentes, enderecos');
    console.log('- obito, score, compras, cnh, funcionarios');
    
  } catch (error) {
    // Error already logged
  }
}

// Run examples
if (require.main === module) {
  main();
}

module.exports = {
  checkStatus,
  performQuery,
  queryByCPF,
  queryByName,
  queryByPhone,
  queryByEmail,
  queryByPlate,
  queryByCNPJ,
  queryNeighbors,
  queryRelatives,
  queryAddresses,
  queryJobs
};
