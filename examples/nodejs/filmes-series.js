/**
 * Cognima API - Exemplo de Filmes e Séries (XC IPTV)
 * 
 * Este exemplo demonstra como usar a API de filmes e séries
 * integrada com XC IPTV.
 */

const axios = require('axios');

// Configuração
const API_BASE_URL = 'https://cog.api.br/api/v1';
const API_KEY = 'sua-api-key-aqui'; // Substitua pela sua API key

// Cliente HTTP configurado
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json'
  }
});

// ===== EXEMPLOS DE FILMES =====

/**
 * Exemplo 1: Listar todas as categorias de filmes
 */
async function listarCategoriasFilmes() {
  try {
    console.log('\n📁 Listando categorias de filmes...\n');
    
    const response = await api.get('/filmes/categorias');
    const categorias = response.data.data;
    
    console.log(`✅ ${categorias.length} categorias encontradas:`);
    categorias.slice(0, 5).forEach(cat => {
      console.log(`   - ${cat.category_name} (ID: ${cat.category_id})`);
    });
    
    return categorias;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Exemplo 2: Listar filmes (todos ou por categoria)
 */
async function listarFilmes(categoryId = null) {
  try {
    console.log('\n🎬 Listando filmes...\n');
    
    const params = categoryId ? { category_id: categoryId } : {};
    const response = await api.get('/filmes', { params });
    const filmes = response.data.data;
    
    console.log(`✅ ${filmes.length} filmes encontrados:`);
    filmes.slice(0, 5).forEach(filme => {
      console.log(`   - ${filme.name}`);
      console.log(`     ID: ${filme.stream_id} | Rating: ${filme.rating || 'N/A'}`);
    });
    
    return filmes;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Exemplo 3: Buscar filmes por nome
 */
async function buscarFilmes(query) {
  try {
    console.log(`\n🔍 Buscando filmes: "${query}"...\n`);
    
    const response = await api.get('/filmes/buscar', {
      params: { query }
    });
    const filmes = response.data.data;
    
    console.log(`✅ ${filmes.length} resultados encontrados:`);
    filmes.forEach(filme => {
      console.log(`   - ${filme.name}`);
      console.log(`     ID: ${filme.stream_id} | Rating: ${filme.rating || 'N/A'}`);
    });
    
    return filmes;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Exemplo 4: Obter detalhes completos de um filme
 */
async function obterDetalhesFilme(streamId) {
  try {
    console.log(`\n📄 Obtendo detalhes do filme ID ${streamId}...\n`);
    
    const response = await api.get(`/filmes/${streamId}`);
    const dados = response.data.data;
    
    console.log('✅ Detalhes do filme:');
    console.log(`   Nome: ${dados.info.name}`);
    console.log(`   Gênero: ${dados.info.genre || 'N/A'}`);
    console.log(`   Rating: ${dados.info.rating || 'N/A'}`);
    console.log(`   Duração: ${dados.info.duration || 'N/A'}`);
    console.log(`   Diretor: ${dados.info.director || 'N/A'}`);
    console.log(`   Elenco: ${dados.info.cast || 'N/A'}`);
    console.log(`   Sinopse: ${dados.info.plot || 'N/A'}`);
    console.log(`   URL de Stream: ${dados.streamUrl}`);
    
    return dados;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

// ===== EXEMPLOS DE SÉRIES =====

/**
 * Exemplo 5: Listar categorias de séries
 */
async function listarCategoriasSeries() {
  try {
    console.log('\n📁 Listando categorias de séries...\n');
    
    const response = await api.get('/series/categorias');
    const categorias = response.data.data;
    
    console.log(`✅ ${categorias.length} categorias encontradas:`);
    categorias.slice(0, 5).forEach(cat => {
      console.log(`   - ${cat.category_name} (ID: ${cat.category_id})`);
    });
    
    return categorias;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Exemplo 6: Buscar séries
 */
async function buscarSeries(query) {
  try {
    console.log(`\n🔍 Buscando séries: "${query}"...\n`);
    
    const response = await api.get('/series/buscar', {
      params: { query }
    });
    const series = response.data.data;
    
    console.log(`✅ ${series.length} resultados encontrados:`);
    series.slice(0, 5).forEach(serie => {
      console.log(`   - ${serie.name}`);
      console.log(`     ID: ${serie.series_id} | Rating: ${serie.rating || 'N/A'}`);
    });
    
    return series;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Exemplo 7: Obter detalhes completos de uma série (com temporadas e episódios)
 */
async function obterDetalhesSerie(seriesId) {
  try {
    console.log(`\n📄 Obtendo detalhes da série ID ${seriesId}...\n`);
    
    const response = await api.get(`/series/${seriesId}`);
    const dados = response.data.data;
    
    console.log('✅ Detalhes da série:');
    console.log(`   Nome: ${dados.info.name}`);
    console.log(`   Gênero: ${dados.info.genre || 'N/A'}`);
    console.log(`   Rating: ${dados.info.rating || 'N/A'}`);
    console.log(`   Temporadas: ${dados.seasons?.length || 0}`);
    
    if (dados.episodes) {
      const totalEpisodes = Object.values(dados.episodes).reduce((sum, eps) => sum + eps.length, 0);
      console.log(`   Total de Episódios: ${totalEpisodes}`);
      
      // Mostrar primeira temporada
      const firstSeason = Object.keys(dados.episodes)[0];
      if (firstSeason) {
        console.log(`\n   📺 Temporada ${firstSeason}:`);
        dados.episodes[firstSeason].slice(0, 3).forEach(ep => {
          console.log(`      E${ep.episode_num}: ${ep.title || 'Sem título'}`);
          console.log(`      Stream URL: ${ep.streamUrl}`);
        });
      }
    }
    
    return dados;
  } catch (error) {
    console.error('❌ Erro:', error.response?.data || error.message);
  }
}

/**
 * Exemplo 8: Gerar link do player web
 */
function gerarLinkPlayer(tipo, id, episodeId = null) {
  const BASE_URL = 'https://cog.api.br';
  
  if (tipo === 'filme') {
    const link = `${BASE_URL}/watch/${id}`;
    console.log(`\n🎬 Link do Player (Filme):\n   ${link}\n`);
    return link;
  } else if (tipo === 'serie') {
    const link = episodeId 
      ? `${BASE_URL}/watch/series/${id}/${episodeId}`
      : `${BASE_URL}/watch/series/${id}`;
    console.log(`\n📺 Link do Player (Série):\n   ${link}\n`);
    return link;
  }
}

// ===== EXECUTAR EXEMPLOS =====

async function executarExemplos() {
  console.log('═══════════════════════════════════════════════════');
  console.log('   🎬 Cognima API - Exemplos de Filmes e Séries');
  console.log('═══════════════════════════════════════════════════');

  // Exemplos de filmes
  await listarCategoriasFilmes();
  await listarFilmes();
  
  const filmesMatrix = await buscarFilmes('matrix');
  if (filmesMatrix && filmesMatrix.length > 0) {
    await obterDetalhesFilme(filmesMatrix[0].stream_id);
    gerarLinkPlayer('filme', filmesMatrix[0].stream_id);
  }

  // Exemplos de séries
  await listarCategoriasSeries();
  
  const seriesBreaking = await buscarSeries('breaking bad');
  if (seriesBreaking && seriesBreaking.length > 0) {
    const detalhes = await obterDetalhesSerie(seriesBreaking[0].series_id);
    gerarLinkPlayer('serie', seriesBreaking[0].series_id);
    
    // Link para episódio específico
    if (detalhes && detalhes.episodes) {
      const firstSeason = Object.keys(detalhes.episodes)[0];
      if (firstSeason && detalhes.episodes[firstSeason][0]) {
        gerarLinkPlayer('serie', seriesBreaking[0].series_id, detalhes.episodes[firstSeason][0].id);
      }
    }
  }

  console.log('\n═══════════════════════════════════════════════════');
  console.log('   ✅ Exemplos concluídos!');
  console.log('═══════════════════════════════════════════════════\n');
}

// Executar se for o arquivo principal
if (require.main === module) {
  executarExemplos().catch(console.error);
}

// Exportar funções para uso em outros arquivos
module.exports = {
  listarCategoriasFilmes,
  listarFilmes,
  buscarFilmes,
  obterDetalhesFilme,
  listarCategoriasSeries,
  buscarSeries,
  obterDetalhesSerie,
  gerarLinkPlayer
};
