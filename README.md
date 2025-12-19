# Cognima API - Complete Documentation

Welcome to the Cognima API documentation! This guide provides detailed information on how to use all available endpoints.

**Base URL:** `https://cog.api.br`

## Table of Contents

- [Authentication](#authentication)
- [Rate Limits](#rate-limits)
- [AI Models](#ai-models)
  - [List Models](#list-models)
  - [Get Model Info](#get-model-info)
  - [Chat Completion](#chat-completion)
- [Custom Models](#custom-models)
  - [Create Custom Model](#create-custom-model)
  - [List Custom Models](#list-custom-models)
  - [Get Custom Model](#get-custom-model)
  - [Update Custom Model](#update-custom-model)
  - [Delete Custom Model](#delete-custom-model)
- [Social Media](#social-media)
  - [Pinterest](#pinterest)
  - [TikTok](#tiktok)
  - [Instagram](#instagram)
- [Content Services](#content-services)
  - [YouTube](#youtube)
  - [Lyrics](#lyrics)
  - [Movies](#movies)
- [File Download Services](#file-download-services)
  - [Google Drive](#google-drive)
  - [MediaFire](#mediafire)
  - [Twitter/X](#twitterx)
- [Web Search](#web-search)
  - [General Search](#general-search)
  - [News Search](#news-search)
- [App Store Search](#app-store-search)
  - [Search Both Stores](#search-both-stores)
  - [Google Play Store](#google-play-store)
  - [Apple App Store](#apple-app-store)
  - [App Details](#app-details)
  - [Similar Apps](#similar-apps)
- [Free Fire Likes](#free-fire-likes)
  - [Service Info](#free-fire-service-info)
  - [Send Likes](#send-free-fire-likes)
- [Data Queries](#data-queries)
  - [Query Status](#query-status)
  - [Perform Query](#perform-data-query)
- [API Status](#api-status)
- [OpenAI Compatible Endpoints](#openai-compatible-endpoints)
- [Error Handling](#error-handling)
- [Code Examples](#code-examples)

---

## Authentication

All API requests require authentication using an API key. Include your API key in the request header:

```http
X-API-Key: your_api_key_here
```

Or as a query parameter:

```http
?api_key=your_api_key_here
```

### API Key Format

API keys follow the format: `ck_xxxxxxxxxxxxxxxxxxxx`

---

## Rate Limits

Rate limits are enforced per API key:

- **Hourly Limit**: Configurable per key (default: 100 requests/hour)
- **Daily Requests**: Configurable per key (default: 1000 requests/day)
- **Daily Tokens**: Configurable per key (default: 50,000 tokens/day)
- **Max Tokens Per Request**: Configurable per key (default: 4000 tokens)

Check your current limits using the [Status endpoint](#get-api-status).

---

## AI Models

### List Models

Get all available AI models.

**Endpoint:** `GET /api/v1/models`

**Query Parameters:**
- `sync` (boolean, optional): Sync with NVIDIA API
- `include_stats` (boolean, optional): Include usage statistics

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/models?include_stats=true" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "models": {
      "chat": [
        {
          "id": 1,
          "nvidia_model_id": "microsoft/phi-3-medium-128k-instruct",
          "name": "Phi-3 Medium 128K Instruct",
          "type": "chat",
          "description": "Microsoft's Phi-3 Medium model",
          "max_tokens": 128000,
          "supports_thinking": false,
          "empresa": "Microsoft"
        }
      ],
      "image": [],
      "completion": []
    },
    "total": 15,
    "counts": {
      "nvidia": 12,
      "cognima": 3,
      "total": 15
    }
  }
}
```

### Get Models by Company

Filter models by company/provider.

**Endpoint:** `GET /api/v1/models/:company`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/models/microsoft" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Models by Type

Filter models by type (chat, image, completion).

**Endpoint:** `GET /api/v1/models/:type`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/models/chat" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Model Info

Get detailed information about a specific model.

**Endpoint:** `GET /api/v1/models/:id/info`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/models/microsoft/phi-3-medium-128k-instruct/info" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Thinking Models

Get models that support advanced thinking mode.

**Endpoint:** `GET /api/v1/models/thinking`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/models/thinking" \
  -H "X-API-Key: ck_your_api_key"
```

### Chat Completion

Generate text responses using AI models.

**Endpoint:** `POST /api/v1/completion`

**Request Body:**

```json
{
  "model": "microsoft/phi-3-medium-128k-instruct",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is artificial intelligence?"
    }
  ],
  "max_tokens": 1000,
  "temperature": 0.7,
  "top_p": 0.95,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "stream": false
}
```

**Parameters:**

- `model` (string, required): Model ID to use
- `messages` (array, required): Array of message objects with `role` and `content`
  - Roles: `system`, `user`, `assistant`
- `max_tokens` (integer, optional): Maximum tokens to generate (default: 1000, max: 32768)
- `temperature` (number, optional): Controls randomness (0-2, default: 0.7)
- `top_p` (number, optional): Nucleus sampling parameter (0-1, default: 0.95)
- `frequency_penalty` (number, optional): Penalize frequent tokens (-2 to 2)
- `presence_penalty` (number, optional): Penalize repeated tokens (-2 to 2)
- `stop` (string/array, optional): Stop sequences
- `seed` (integer, optional): Random seed for reproducibility
- `stream` (boolean, optional): Enable streaming responses
- `thinking_enabled` (boolean, optional): Enable thinking mode
- `thinking_model` (string, optional): Model to use for thinking

**Advanced Parameters:**

- `top_k` (integer, optional): Top-K sampling (1-100)
- `repetition_penalty` (number, optional): Penalize repetition (0.1-2)
- `min_tokens` (integer, optional): Minimum tokens to generate
- `length_penalty` (number, optional): Length penalty (-2 to 2)
- `early_stopping` (boolean, optional): Enable early stopping
- `logit_bias` (object, optional): Token bias adjustments
- `logprobs` (boolean, optional): Return log probabilities
- `top_logprobs` (integer, optional): Number of top logprobs (0-20)
- `n` (integer, optional): Number of completions (1-10)
- `best_of` (integer, optional): Best of N generations (1-20)
- `user` (string, optional): User identifier

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/completion" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "microsoft/phi-3-medium-128k-instruct",
    "messages": [
      {"role": "user", "content": "Explain quantum computing in simple terms"}
    ],
    "max_tokens": 500,
    "temperature": 0.7
  }'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "id": "chatcmpl-123456",
    "object": "chat.completion",
    "created": 1699999999,
    "model": "microsoft/phi-3-medium-128k-instruct",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "Quantum computing is a revolutionary approach..."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 15,
      "completion_tokens": 150,
      "total_tokens": 165
    }
  },
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 150,
    "total_tokens": 165,
    "thinking_tokens": 0,
    "estimated_cost": 0.000165
  },
  "limits": {
    "remaining": {
      "hourly": 99,
      "daily_requests": 999,
      "daily_tokens": 49835
    }
  },
  "request_id": "req_1699999999_abc123",
  "processing_time_ms": 1234
}
```

### Streaming Responses

Enable streaming for real-time token generation:

```bash
curl -X POST "https://cog.api.br/api/v1/completion" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "microsoft/phi-3-medium-128k-instruct",
    "messages": [{"role": "user", "content": "Write a poem"}],
    "stream": true
  }'
```

**Stream Format:** Server-Sent Events (SSE)

Each chunk:
```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion.chunk",
  "created": 1699999999,
  "model": "microsoft/phi-3-medium-128k-instruct",
  "choices": [{
    "index": 0,
    "delta": {"content": "Hello"},
    "finish_reason": null
  }]
}
```

Final message: `data: [DONE]`

---

## Custom Models

Create personalized AI models with custom personalities and behaviors.

### Create Custom Model

**Endpoint:** `POST /api/v1/custom`

**Request Body:**

```json
{
  "name": "helpful-assistant",
  "display_name": "Helpful Assistant",
  "description": "A friendly and helpful AI assistant",
  "personality_summary": "You are a friendly, professional assistant who always provides clear and concise answers. You have a warm tone and make complex topics easy to understand.",
  "base_model": "microsoft/phi-3-medium-128k-instruct"
}
```

**Parameters:**

- `name` (string, required): Model identifier (2-50 chars, alphanumeric, hyphens, underscores)
- `display_name` (string, optional): Display name (max 100 chars)
- `description` (string, optional): Model description (max 500 chars)
- `personality_summary` (string, required): Personality description (10-2000 chars)
- `base_model` (string, optional): Base NVIDIA model (default: "microsoft/phi-3-medium-128k-instruct")

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/custom" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "coding-mentor",
    "display_name": "Coding Mentor",
    "personality_summary": "You are an experienced programming mentor who explains code with patience and uses practical examples."
  }'
```

**Example Response:**

```json
{
  "success": true,
  "message": "Modelo personalizado criado com sucesso",
  "data": {
    "id": 123,
    "name": "coding-mentor",
    "display_name": "Coding Mentor",
    "full_name": "@cognima/coding-mentor",
    "description": "",
    "personality_summary": "You are an experienced...",
    "system_prompt": "# Role: Coding Mentor\n\nYou are an experienced...",
    "base_model": "microsoft/phi-3-medium-128k-instruct",
    "created_at": "2024-11-07T10:00:00Z"
  }
}
```

### List Custom Models

Get all your custom models.

**Endpoint:** `GET /api/v1/custom`

**Query Parameters:**
- `page` (integer, optional): Page number (default: 1)
- `limit` (integer, optional): Results per page (default: 20)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/custom?page=1&limit=10" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "models": [
      {
        "id": 123,
        "name": "coding-mentor",
        "display_name": "Coding Mentor",
        "full_name": "@cognima/coding-mentor",
        "description": "",
        "base_model": "microsoft/phi-3-medium-128k-instruct",
        "usage_count": 45,
        "created_at": "2024-11-07T10:00:00Z",
        "updated_at": "2024-11-07T10:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 3,
      "pages": 1
    }
  }
}
```

### Get Custom Model

Get details of a specific custom model.

**Endpoint:** `GET /api/v1/custom/:id`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/custom/123" \
  -H "X-API-Key: ck_your_api_key"
```

### Update Custom Model

Update an existing custom model.

**Endpoint:** `PUT /api/v1/custom/:id`

**Request Body:**

```json
{
  "display_name": "Advanced Coding Mentor",
  "description": "Updated description",
  "regenerate_prompt": true
}
```

**Parameters:**

- `name` (string, optional): New model identifier
- `display_name` (string, optional): New display name
- `description` (string, optional): New description
- `personality_summary` (string, optional): New personality
- `base_model` (string, optional): New base model
- `regenerate_prompt` (boolean, optional): Regenerate system prompt

**Example Request:**

```bash
curl -X PUT "https://cog.api.br/api/v1/custom/123" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Senior Coding Mentor",
    "regenerate_prompt": true
  }'
```

### Delete Custom Model

Delete a custom model.

**Endpoint:** `DELETE /api/v1/custom/:id`

**Example Request:**

```bash
curl -X DELETE "https://cog.api.br/api/v1/custom/123" \
  -H "X-API-Key: ck_your_api_key"
```

### Using Custom Models

Use your custom model in chat completions:

```bash
curl -X POST "https://cog.api.br/api/v1/completion" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "@cognima/coding-mentor",
    "messages": [
      {"role": "user", "content": "Explain recursion"}
    ]
  }'
```

### Get Personality Suggestions

Get example personality templates.

**Endpoint:** `GET /api/v1/custom/suggestions`

### Preview System Prompt

Preview the generated system prompt before creating a model.

**Endpoint:** `POST /api/v1/custom/preview-prompt`

**Request Body:**

```json
{
  "personality_summary": "You are a friendly assistant...",
  "display_name": "Friendly AI",
  "description": "A helpful assistant"
}
```

### Custom Model Statistics

**Endpoint:** `GET /api/v1/custom/stats?days=30`

---

## Social Media

### Pinterest

#### Search Pinterest

Search for images on Pinterest.

**Endpoint:** `POST /api/v1/pinterest/search`

**Request Body:**

```json
{
  "query": "modern interior design"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/pinterest/search" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "minimalist architecture"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "query": "minimalist architecture",
    "results": [
      {
        "id": "123456789",
        "title": "Modern Minimalist Home",
        "description": "A beautiful example...",
        "image_url": "https://i.pinimg.com/...",
        "link": "https://pinterest.com/pin/...",
        "board": "Architecture Ideas"
      }
    ],
    "count": 20
  },
  "cached": false,
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### Download Pinterest Pin

Download media from a Pinterest pin.

**Endpoint:** `POST /api/v1/pinterest/download`

**Request Body:**

```json
{
  "url": "https://pinterest.com/pin/123456789/"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/pinterest/download" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://pinterest.com/pin/123456789/"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "title": "Beautiful Design",
    "description": "A stunning example...",
    "urls": [
      {
        "quality": "original",
        "url": "https://i.pinimg.com/originals/..."
      },
      {
        "quality": "736x",
        "url": "https://i.pinimg.com/736x/..."
      }
    ],
    "author": "DesignStudio",
    "board": "Inspiration"
  },
  "cached": false,
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### Pinterest Cache Stats

**Endpoint:** `GET /api/v1/pinterest/cache/stats`

#### Clear Pinterest Cache

**Endpoint:** `DELETE /api/v1/pinterest/cache`

---

### TikTok

#### Download TikTok Video

Download videos from TikTok.

**Endpoint:** `POST /api/v1/tiktok/download`

**Request Body:**

```json
{
  "url": "https://www.tiktok.com/@user/video/1234567890"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/tiktok/download" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@user/video/1234567890"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "id": "1234567890",
    "title": "Amazing video!",
    "author": {
      "username": "user",
      "nickname": "User Name",
      "avatar": "https://..."
    },
    "stats": {
      "views": 1000000,
      "likes": 50000,
      "comments": 1000,
      "shares": 5000
    },
    "urls": [
      {
        "quality": "hd",
        "url": "https://...",
        "format": "mp4"
      },
      {
        "quality": "watermark",
        "url": "https://...",
        "format": "mp4"
      }
    ],
    "music": {
      "title": "Original Sound",
      "author": "user",
      "url": "https://..."
    }
  },
  "cached": false,
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### Search TikTok

Search for videos on TikTok.

**Endpoint:** `POST /api/v1/tiktok/search`

**Request Body:**

```json
{
  "query": "cooking recipes"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/tiktok/search" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "funny cats"}'
```

#### TikTok Cache Stats

**Endpoint:** `GET /api/v1/tiktok/cache/stats`

#### Clear TikTok Cache

**Endpoint:** `DELETE /api/v1/tiktok/cache`

---

### Instagram

#### Download Instagram Post

Download media from Instagram posts, reels, or stories.

**Endpoint:** `POST /api/v1/instagram/download`

**Request Body:**

```json
{
  "url": "https://www.instagram.com/p/ABC123xyz/"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/instagram/download" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/ABC123xyz/"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "id": "ABC123xyz",
    "type": "post",
    "caption": "Beautiful sunset! 🌅",
    "author": {
      "username": "photographer",
      "full_name": "John Photographer",
      "avatar": "https://..."
    },
    "timestamp": "2024-11-07T10:00:00Z",
    "likes": 5000,
    "comments": 250,
    "media": [
      {
        "type": "image",
        "url": "https://...",
        "width": 1080,
        "height": 1080
      }
    ],
    "count": 1
  },
  "cached": false,
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### Instagram Cache Stats

**Endpoint:** `GET /api/v1/instagram/cache/stats`

#### Clear Instagram Cache

**Endpoint:** `DELETE /api/v1/instagram/cache`

---

## Content Services

### YouTube

#### Search YouTube

Search for videos on YouTube.

**Endpoint:** `POST /api/v1/youtube/search`

**Request Body:**

```json
{
  "query": "programming tutorial"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/youtube/search" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "javascript tutorial"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "query": "javascript tutorial",
    "results": [
      {
        "id": "dQw4w9WgXcQ",
        "title": "JavaScript Tutorial for Beginners",
        "description": "Learn JavaScript from scratch...",
        "thumbnail": "https://i.ytimg.com/vi/...",
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "channel": {
          "name": "Programming Channel",
          "url": "https://www.youtube.com/channel/..."
        },
        "duration": "PT45M30S",
        "views": 1000000,
        "published": "2024-01-01T00:00:00Z"
      }
    ],
    "count": 10
  },
  "cached": false,
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### Download YouTube Audio (MP3)

Download audio from YouTube videos.

**Endpoint:** `POST /api/v1/youtube/mp3`

**Request Body:**

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "quality": "mp3",
  "direct": false
}
```

**Parameters:**

- `url` (string, required): YouTube video URL
- `quality` (string, optional): Audio quality (default: "mp3")
- `direct` (boolean, optional): Return binary data directly (default: false)

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/youtube/mp3" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

**Example Response (JSON):**

```json
{
  "success": true,
  "data": {
    "title": "Song Title",
    "duration": 180,
    "filename": "song-title.mp3",
    "buffer": "<base64_encoded_audio>",
    "source": "ytdlp"
  },
  "timestamp": "2024-11-07T10:00:00Z"
}
```

**Direct Download:**

Set `Accept: audio/mpeg` header or `direct: true` to receive the file directly:

```bash
curl -X POST "https://cog.api.br/api/v1/youtube/mp3" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Accept: audio/mpeg" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}' \
  --output song.mp3
```

#### Download YouTube Video (MP4)

Download videos from YouTube.

**Endpoint:** `POST /api/v1/youtube/mp4`

**Request Body:**

```json
{
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "quality": "720p",
  "direct": false
}
```

**Parameters:**

- `url` (string, required): YouTube video URL
- `quality` (string, optional): Video quality - "360p", "720p", "1080p" (default: "360p")
- `direct` (boolean, optional): Return binary data directly (default: false)

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/youtube/mp4" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "quality": "720p"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "title": "Video Title",
    "duration": 300,
    "quality": "720p",
    "filename": "video-title-720p.mp4",
    "buffer": "<base64_encoded_video>",
    "source": "ytdlp"
  },
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### YouTube Cache Stats

**Endpoint:** `GET /api/v1/youtube/cache/stats`

#### Clear YouTube Cache

**Endpoint:** `DELETE /api/v1/youtube/cache`

---

### Lyrics

#### Search Song Lyrics

Search for song lyrics.

**Endpoint:** `POST /api/v1/lyrics/search`

**Request Body:**

```json
{
  "query": "imagine dragons believer"
}
```

**Example Request:**

```bash
curl -X POST "https://cog.api.br/api/v1/lyrics/search" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "bohemian rhapsody queen"}'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "title": "Bohemian Rhapsody",
    "artist": "Queen",
    "album": "A Night at the Opera",
    "year": 1975,
    "lyrics": "Is this the real life?\nIs this just fantasy?...",
    "url": "https://genius.com/...",
    "thumbnail": "https://..."
  },
  "cached": false,
  "timestamp": "2024-11-07T10:00:00Z"
}
```

#### Lyrics Cache Stats

**Endpoint:** `GET /api/v1/lyrics/cache/stats`

#### Clear Lyrics Cache

**Endpoint:** `DELETE /api/v1/lyrics/cache`

---

### Movies & Series

The Cognima API provides access to thousands of movies and TV series via XC IPTV integration. You can browse by categories, search, get detailed information, and stream content directly.

**Features:**
- 🎬 13,863+ movies available
- 📺 9,251+ TV series with complete seasons and episodes
- 📁 39 movie categories and 30 series categories
- 🔍 Fast search functionality
- 🎥 Built-in web player with episode selector
- 💾 Intelligent caching (1 hour for content, 2 hours for categories)

#### Movies API

##### List Movie Categories

Get all available movie categories.

**Endpoint:** `GET /api/v1/filmes/categorias`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/filmes/categorias" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "category_id": "1",
      "category_name": "Action",
      "parent_id": 0
    },
    {
      "category_id": "2",
      "category_name": "Comedy",
      "parent_id": 0
    }
  ],
  "cached": true,
  "cached_at": "2024-01-15T10:30:00.000Z"
}
```

##### List Movies

Get all movies or filter by category.

**Endpoint:** `GET /api/v1/filmes`

**Query Parameters:**
- `category_id` (string, optional): Filter by category ID

**Example Request:**

```bash
# Get all movies
curl -X GET "https://cog.api.br/api/v1/filmes" \
  -H "X-API-Key: ck_your_api_key"

# Get movies from specific category
curl -X GET "https://cog.api.br/api/v1/filmes?category_id=1" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "num": 1,
      "name": "The Matrix",
      "stream_type": "movie",
      "stream_id": 12345,
      "stream_icon": "https://image.tmdb.org/...",
      "rating": "8.7",
      "rating_5based": 4.35,
      "added": "1617235200",
      "category_id": "1",
      "container_extension": "mp4",
      "direct_source": ""
    }
  ],
  "total": 13863,
  "cached": true
}
```

##### Search Movies

Search for movies by name.

**Endpoint:** `GET /api/v1/filmes/buscar`

**Query Parameters:**
- `query` (string, required): Search term

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/filmes/buscar?query=matrix" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "name": "The Matrix",
      "stream_id": 12345,
      "rating": "8.7",
      "stream_icon": "https://image.tmdb.org/..."
    }
  ],
  "total": 3
}
```

##### Get Movie Details

Get detailed information about a specific movie including stream URL.

**Endpoint:** `GET /api/v1/filmes/:stream_id`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/filmes/12345" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "info": {
      "tmdb_id": "603",
      "name": "The Matrix",
      "o_name": "The Matrix",
      "cover_big": "https://image.tmdb.org/...",
      "movie_image": "https://image.tmdb.org/...",
      "releasedate": "1999-03-30",
      "youtube_trailer": "vKQi3bBA1y8",
      "director": "Lana Wachowski, Lilly Wachowski",
      "actors": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
      "cast": "Keanu Reeves, Laurence Fishburne",
      "description": "Set in the 22nd century...",
      "plot": "A computer hacker learns...",
      "age": "R",
      "mpaa_rating": "R",
      "rating_count_kinopoisk": 0,
      "country": "United States of America",
      "genre": "Action, Science Fiction",
      "backdrop_path": ["https://image.tmdb.org/..."],
      "duration_secs": 8160,
      "duration": "136 min",
      "video": 1,
      "audio": 1,
      "bitrate": 5000
    },
    "movie_data": {
      "stream_id": 12345,
      "name": "The Matrix",
      "added": "1617235200",
      "category_id": "1",
      "container_extension": "mp4",
      "custom_sid": "",
      "direct_source": ""
    },
    "streamUrl": "https://cogtv.com.br/movie/cogapi/cog1234/12345.mp4"
  }
}
```

##### Web Player for Movies

Watch movies directly in the browser with our built-in player.

**Endpoint:** `GET /watch/:stream_id`

**Example:**

```
https://cog.api.br/watch/12345
```

This opens a full-featured video player with:
- Video.js based player
- HLS and MP4 support
- Fullscreen mode
- Playback controls
- Responsive design

---

#### Series API

##### List Series Categories

Get all available series categories.

**Endpoint:** `GET /api/v1/series/categorias`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/series/categorias" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "category_id": "10",
      "category_name": "Drama",
      "parent_id": 0
    },
    {
      "category_id": "11",
      "category_name": "Sci-Fi",
      "parent_id": 0
    }
  ],
  "cached": true
}
```

##### List Series

Get all series or filter by category.

**Endpoint:** `GET /api/v1/series`

**Query Parameters:**
- `category_id` (string, optional): Filter by category ID

**Example Request:**

```bash
# Get all series
curl -X GET "https://cog.api.br/api/v1/series" \
  -H "X-API-Key: ck_your_api_key"

# Get series from specific category
curl -X GET "https://cog.api.br/api/v1/series?category_id=10" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "num": 1,
      "name": "Breaking Bad",
      "series_id": 54321,
      "cover": "https://image.tmdb.org/...",
      "plot": "A high school chemistry teacher...",
      "cast": "Bryan Cranston, Aaron Paul",
      "director": "Vince Gilligan",
      "genre": "Crime, Drama, Thriller",
      "releaseDate": "2008-01-20",
      "last_modified": "1617235200",
      "rating": "9.5",
      "rating_5based": 4.75,
      "backdrop_path": ["https://image.tmdb.org/..."],
      "youtube_trailer": "HhesaQXLuRY",
      "episode_run_time": "45",
      "category_id": "10"
    }
  ],
  "total": 9251,
  "cached": true
}
```

##### Search Series

Search for series by name.

**Endpoint:** `GET /api/v1/series/buscar`

**Query Parameters:**
- `query` (string, required): Search term

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/series/buscar?query=breaking%20bad" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "name": "Breaking Bad",
      "series_id": 54321,
      "rating": "9.5",
      "cover": "https://image.tmdb.org/..."
    }
  ],
  "total": 1
}
```

##### Get Series Details

Get complete series information including all seasons and episodes.

**Endpoint:** `GET /api/v1/series/:series_id`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/series/54321" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "seasons": [
      {
        "id": 1,
        "name": "Season 1",
        "episode_count": 7,
        "overview": "Walter White...",
        "air_date": "2008-01-20",
        "cover": "https://image.tmdb.org/...",
        "cover_big": "https://image.tmdb.org/...",
        "cover_tmdb": "https://image.tmdb.org/..."
      },
      {
        "id": 2,
        "name": "Season 2",
        "episode_count": 13,
        "overview": "Walt and Jesse...",
        "air_date": "2009-03-08",
        "cover": "https://image.tmdb.org/..."
      }
    ],
    "info": {
      "name": "Breaking Bad",
      "cover": "https://image.tmdb.org/...",
      "plot": "A high school chemistry teacher...",
      "cast": "Bryan Cranston, Aaron Paul",
      "director": "Vince Gilligan",
      "genre": "Crime, Drama, Thriller",
      "releaseDate": "2008-01-20",
      "last_modified": "1617235200",
      "rating": "9.5",
      "rating_5based": 4.75,
      "backdrop_path": ["https://image.tmdb.org/..."],
      "youtube_trailer": "HhesaQXLuRY",
      "episode_run_time": "45",
      "category_id": "10",
      "tmdb_id": "1396"
    },
    "episodes": {
      "1": [
        {
          "id": "12345_1_1",
          "episode_num": 1,
          "title": "Pilot",
          "container_extension": "mp4",
          "info": {
            "tmdb_id": 62085,
            "releasedate": "2008-01-20",
            "plot": "Walter White begins his journey...",
            "duration_secs": 3480,
            "duration": "58:00",
            "video": {
              "index": 0,
              "codec_name": "h264",
              "codec_long_name": "H.264",
              "width": 1920,
              "height": 1080
            },
            "audio": {
              "index": 1,
              "codec_name": "aac",
              "codec_long_name": "AAC"
            },
            "bitrate": 3500,
            "rating": "8.2"
          },
          "custom_sid": "",
          "added": "1617235200",
          "season": 1,
          "direct_source": "",
          "streamUrl": "https://cogtv.com.br/series/cogapi/cog1234/12345_1_1.mp4"
        }
      ],
      "2": [
        {
          "id": "12345_2_1",
          "episode_num": 1,
          "title": "Seven Thirty-Seven",
          "season": 2,
          "streamUrl": "https://cogtv.com.br/series/cogapi/cog1234/12345_2_1.mp4"
        }
      ]
    }
  }
}
```

##### Web Player for Series

Watch series with an interactive episode selector sidebar.

**Endpoints:**

```
# Watch first episode
GET /watch/series/:series_id

# Watch specific episode
GET /watch/series/:series_id/:episode_id
```

**Example:**

```
# First episode
https://cog.api.br/watch/series/54321

# Specific episode (Season 1, Episode 1)
https://cog.api.br/watch/series/54321/12345_1_1
```

**Player Features:**
- Video.js based player
- Sidebar with all seasons and episodes
- Click to switch episodes instantly
- Responsive design (desktop and mobile)
- Accordion-style season selector
- Episode thumbnails and information
- Fullscreen support

---

#### Code Examples

##### Node.js Example

```javascript
const axios = require('axios');

const api = axios.create({
  baseURL: 'https://cog.api.br/api/v1',
  headers: { 'X-API-Key': 'ck_your_api_key' }
});

// Search for a movie
async function searchMovie(query) {
  const response = await api.get('/filmes/buscar', {
    params: { query }
  });
  return response.data.data;
}

// Get series with episodes
async function getSeries(seriesId) {
  const response = await api.get(`/series/${seriesId}`);
  return response.data.data;
}

// Usage
searchMovie('matrix').then(movies => console.log(movies));
getSeries(54321).then(series => console.log(series.episodes));
```

**Full example:** [examples/nodejs/filmes-series.js](examples/nodejs/filmes-series.js)

##### Python Example

```python
import requests

API_BASE_URL = 'https://cog.api.br/api/v1'
API_KEY = 'ck_your_api_key'

headers = {'X-API-Key': API_KEY}

# Search for a movie
def search_movie(query):
    response = requests.get(
        f'{API_BASE_URL}/filmes/buscar',
        headers=headers,
        params={'query': query}
    )
    return response.json()['data']

# Get series with episodes
def get_series(series_id):
    response = requests.get(
        f'{API_BASE_URL}/series/{series_id}',
        headers=headers
    )
    return response.json()['data']

# Usage
movies = search_movie('matrix')
series = get_series(54321)
print(f"Episodes: {series['episodes']}")
```

**Full example:** [examples/python/filmes_series.py](examples/python/filmes_series.py)

---

## File Download Services

### Google Drive

Download files from Google Drive.

#### Get Google Drive File Info

Get file information without downloading.

**Endpoint:** `GET /api/v1/gdrive/info`

**Query Parameters:**
- `url` (string, required): Google Drive file URL

**Supported URL Formats:**
- `https://drive.google.com/file/d/FILE_ID/view`
- `https://drive.google.com/open?id=FILE_ID`
- `https://drive.google.com/uc?id=FILE_ID`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/gdrive/info?url=https://drive.google.com/file/d/1ABC123xyz/view" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "fileId": "1ABC123xyz",
    "fileName": "document.pdf",
    "fileSize": "15.32 MB",
    "fileSizeBytes": 16066560,
    "downloadUrl": "https://drive.google.com/uc?...",
    "mimetype": "application/pdf"
  }
}
```

#### Download Google Drive File

Get download link or redirect to file.

**Endpoint:** `GET /api/v1/gdrive/download`

**Query Parameters:**
- `url` (string, required): Google Drive file URL
- `redirect` (boolean, optional): If `true`, redirects to download URL

**Example Request:**

```bash
# Get download info as JSON
curl -X GET "https://cog.api.br/api/v1/gdrive/download?url=https://drive.google.com/file/d/1ABC123xyz/view" \
  -H "X-API-Key: ck_your_api_key"

# Redirect directly to download
curl -L "https://cog.api.br/api/v1/gdrive/download?url=https://drive.google.com/file/d/1ABC123xyz/view&redirect=true" \
  -H "X-API-Key: ck_your_api_key" \
  --output file.pdf
```

---

### MediaFire

Download files from MediaFire.

#### Get MediaFire File Info

Get file information without downloading.

**Endpoint:** `GET /api/v1/mediafire/info`

**Query Parameters:**
- `url` (string, required): MediaFire file URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/mediafire/info?url=https://www.mediafire.com/file/abc123xyz/arquivo.zip/file" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "fileName": "arquivo.zip",
    "fileSize": "256.45 MB",
    "uploadDate": "2024-01-15",
    "mimetype": "application/zip",
    "extension": "zip",
    "downloadUrl": "https://download123.mediafire.com/..."
  }
}
```

#### Download MediaFire File

Get download link or redirect to file.

**Endpoint:** `GET /api/v1/mediafire/download`

**Query Parameters:**
- `url` (string, required): MediaFire file URL
- `redirect` (boolean, optional): If `true`, redirects to download URL

**Example Request:**

```bash
# Get download info as JSON
curl -X GET "https://cog.api.br/api/v1/mediafire/download?url=https://www.mediafire.com/file/abc123xyz/arquivo.zip/file" \
  -H "X-API-Key: ck_your_api_key"

# Redirect directly to download
curl -L "https://cog.api.br/api/v1/mediafire/download?url=https://www.mediafire.com/file/abc123xyz/arquivo.zip/file&redirect=true" \
  -H "X-API-Key: ck_your_api_key" \
  --output arquivo.zip
```

---

### Twitter/X

Download media from Twitter/X posts.

#### Get Tweet Info

Get complete tweet information including author, stats, and media.

**Endpoint:** `GET /api/v1/twitter/info`

**Query Parameters:**
- `url` (string, required): Twitter/X tweet URL

**Supported URL Formats:**
- `https://twitter.com/user/status/ID`
- `https://x.com/user/status/ID`
- `https://twitter.com/i/status/ID`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/twitter/info?url=https://twitter.com/user/status/1234567890" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "id": "1234567890",
    "text": "This is a tweet with video! 🎬",
    "createdAt": "Wed Nov 06 12:00:00 +0000 2024",
    "createdTimestamp": 1730894400,
    "url": "https://twitter.com/user/status/1234567890",
    "stats": {
      "replies": 50,
      "retweets": 200,
      "likes": 1500
    },
    "possiblySensitive": false,
    "author": {
      "id": "9876543210",
      "name": "User Name",
      "username": "user",
      "avatarUrl": "https://pbs.twimg.com/profile_images/...",
      "bannerUrl": "https://pbs.twimg.com/profile_banners/..."
    },
    "type": "video",
    "media": [
      {
        "type": "video",
        "duration": 30000,
        "thumbnailUrl": "https://pbs.twimg.com/...",
        "url": "https://video.twimg.com/...",
        "bestQuality": {
          "bitrate": 2176000,
          "contentType": "video/mp4",
          "resolution": "1280x720",
          "url": "https://video.twimg.com/..."
        },
        "variants": [
          {
            "bitrate": 2176000,
            "contentType": "video/mp4",
            "resolution": "1280x720",
            "url": "https://..."
          },
          {
            "bitrate": 832000,
            "contentType": "video/mp4",
            "resolution": "640x360",
            "url": "https://..."
          }
        ]
      }
    ],
    "hasMedia": true
  }
}
```

#### Download Twitter Media

Get direct download links for best quality media.

**Endpoint:** `GET /api/v1/twitter/download`

**Query Parameters:**
- `url` (string, required): Twitter/X tweet URL
- `redirect` (boolean, optional): If `true`, redirects to first media download URL

**Example Request:**

```bash
# Get download links as JSON
curl -X GET "https://cog.api.br/api/v1/twitter/download?url=https://twitter.com/user/status/1234567890" \
  -H "X-API-Key: ck_your_api_key"

# Redirect directly to first media
curl -L "https://cog.api.br/api/v1/twitter/download?url=https://twitter.com/user/status/1234567890&redirect=true" \
  -H "X-API-Key: ck_your_api_key" \
  --output video.mp4
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "tweetId": "1234567890",
    "author": "user",
    "type": "video",
    "downloads": [
      {
        "type": "video",
        "url": "https://video.twimg.com/...",
        "resolution": "1280x720",
        "thumbnail": "https://pbs.twimg.com/...",
        "duration": 30000
      }
    ]
  }
}
```

**Supported Media Types:**
- **Videos**: Multiple resolutions available (best quality selected automatically)
- **Photos**: Original quality images
- **GIFs**: Animated GIFs

---

## Web Search

Search the web using DuckDuckGo (privacy-focused search).

### General Search

Search for anything on the web.

**Endpoint:** `GET /api/v1/search`

**Query Parameters:**

- `q` or `query` (string, required): Search query
- `max` or `maxResults` (integer, optional): Maximum results (default: 10)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/search?q=artificial+intelligence&max=5" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "query": "artificial intelligence",
    "totalResults": 5,
    "results": [
      {
        "position": 1,
        "title": "Artificial Intelligence - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "description": "Artificial intelligence (AI) is the intelligence of machines...",
        "displayUrl": "en.wikipedia.org"
      },
      {
        "position": 2,
        "title": "What is AI? | IBM",
        "url": "https://www.ibm.com/topics/artificial-intelligence",
        "description": "Artificial intelligence leverages computers and machines...",
        "displayUrl": "www.ibm.com"
      }
    ]
  }
}
```

### News Search

Search for recent news articles.

**Endpoint:** `GET /api/v1/search/news`

**Query Parameters:**

- `q` or `query` (string, required): Search query
- `max` or `maxResults` (integer, optional): Maximum results (default: 10)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/search/news?q=technology+brazil&max=5" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "query": "technology brazil news",
    "type": "news",
    "totalResults": 5,
    "results": [
      {
        "position": 1,
        "title": "Brazil Tech Industry Growth in 2024",
        "url": "https://example.com/article",
        "description": "Brazil's technology sector continues to grow...",
        "displayUrl": "example.com"
      }
    ]
  }
}
```

---

## App Store Search

Search for apps on Google Play Store and Apple App Store.

### Search Both Stores

Search for apps on both stores in a single request.

**Endpoint:** `GET /api/v1/apps/search`

**Query Parameters:**

- `q` or `query` (string, required): Search query
- `num` (integer, optional): Number of results per store (default: 10, max: 50)
- `country` (string, optional): Country code (default: 'br')
- `lang` (string, optional): Language code (default: 'pt')

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/apps/search?q=whatsapp&num=5" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "query": "whatsapp",
    "playStore": [
      {
        "store": "playStore",
        "appId": "com.whatsapp",
        "title": "WhatsApp Messenger",
        "developer": "WhatsApp LLC",
        "icon": "https://play-lh.googleusercontent.com/...",
        "url": "https://play.google.com/store/apps/details?id=com.whatsapp",
        "score": 4.2,
        "price": "Free",
        "free": true,
        "summary": "Simple. Reliable. Private.",
        "installs": "5,000,000,000+"
      }
    ],
    "appStore": [
      {
        "store": "appStore",
        "id": 310633997,
        "appId": "com.whatsapp.WhatsApp",
        "title": "WhatsApp Messenger",
        "developer": "WhatsApp Inc.",
        "icon": "https://is1-ssl.mzstatic.com/...",
        "url": "https://apps.apple.com/...",
        "score": 4.7,
        "price": 0,
        "free": true
      }
    ],
    "errors": []
  }
}
```

### Google Play Store

Search only on Google Play Store.

**Endpoint:** `GET /api/v1/apps/playstore`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/apps/playstore?q=games&num=5" \
  -H "X-API-Key: ck_your_api_key"
```

### Apple App Store

Search only on Apple App Store.

**Endpoint:** `GET /api/v1/apps/appstore`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/apps/appstore?q=music&num=5" \
  -H "X-API-Key: ck_your_api_key"
```

### App Details

Get detailed information about a specific app.

**Endpoint:** `GET /api/v1/apps/details`

**Query Parameters:**
- `id` or `appId` (string, required): App ID (e.g., 'com.whatsapp' for Play Store)
- `store` (string, required): 'playStore', 'appStore', 'play', or 'ios'
- `country` (string, optional): Country code (default: 'br')

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/apps/details?appId=com.whatsapp&store=playStore" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "store": "playStore",
    "appId": "com.whatsapp",
    "title": "WhatsApp Messenger",
    "description": "WhatsApp from Meta is a FREE messaging and video calling app...",
    "developer": "WhatsApp LLC",
    "developerEmail": "support@whatsapp.com",
    "icon": "https://play-lh.googleusercontent.com/...",
    "screenshots": ["..."],
    "score": 4.2,
    "ratings": 178509328,
    "reviews": 12956341,
    "price": "Free",
    "free": true,
    "installs": "5,000,000,000+",
    "genre": "Communication",
    "version": "2.24.10.75",
    "updated": 1715875200000,
    "androidVersion": "5.0"
  }
}
```

### Similar Apps

Get apps similar to a specific app.

**Endpoint:** `GET /api/v1/apps/similar`

**Query Parameters:**
- `id` or `appId` (string, required): App ID
- `store` (string, required): 'playStore', 'appStore', 'play', or 'ios'
- `num` (integer, optional): Number of results (default: 10)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/apps/similar?appId=com.whatsapp&store=playStore&num=5" \
  -H "X-API-Key: ck_your_api_key"
```

---

## Free Fire Likes

> **⚠️ Premium Feature:** Requires API key with daily limit > 500 requests (Unlimited or Bot plan)

Send likes to Free Fire players.

### Free Fire Service Info

Get information about the Free Fire Likes service.

**Endpoint:** `GET /api/v1/freefire/info`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/freefire/info" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "service": "Free Fire Likes",
  "description": "Envio de likes para jogadores de Free Fire",
  "endpoint": "/api/v1/freefire/sendlikes",
  "parameters": {
    "playerId": {
      "type": "string",
      "required": true,
      "description": "ID do jogador (UID) - 8 a 10 dígitos",
      "example": "1033857091"
    }
  },
  "rules": {
    "minLikes": 100,
    "minLikesDescription": "Apenas solicitações que enviam 100+ likes são contabilizadas",
    "usageLimit": "Definido pela chave externa fornecida"
  }
}
```

### Send Free Fire Likes

Send likes to a Free Fire player by their UID.

**Endpoint:** `GET /api/v1/freefire/sendlikes`

**Query Parameters:**
- `playerId` (string, required): Player UID (8-10 digits)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/freefire/sendlikes?playerId=1033857091" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response (Success - 100+ likes):**

```json
{
  "success": true,
  "data": {
    "player": "#Regiis7x'ㅤ⁑",
    "uid": "1033857091",
    "region": "BR",
    "initialLikes": 15162,
    "finalLikes": 15362,
    "likesAdded": 200,
    "level": 72,
    "exp": 3502529,
    "status": 1,
    "timestamp": "11/12/2024 14:30:00",
    "usageCounted": true,
    "minLikesRequired": 100,
    "usageStatus": "CONTABILIZADO (100+ likes enviados)",
    "keystats": "1/100"
  },
  "error": null,
  "message": "Likes enviados com sucesso"
}
```

**Example Response (Less than 100 likes):**

```json
{
  "success": false,
  "data": {
    "player": "#PlayerName",
    "uid": "1033857091",
    "region": "BR",
    "initialLikes": 100,
    "finalLikes": 150,
    "likesAdded": 50,
    "level": 72,
    "exp": 3502529,
    "status": 1,
    "timestamp": "11/12/2024 14:30:00",
    "usageCounted": false,
    "minLikesRequired": 100,
    "usageStatus": "NÃO CONTABILIZADO (menos de 100 likes)",
    "keystats": "0/100"
  },
  "error": "INSUFFICIENT_LIKES",
  "message": "Menos de 100 likes foram enviados"
}
```

**Important Rules:**
- Only requests sending **100+ likes** are counted toward limits
- Requires API key with daily limit > 500 requests
- Player UID must be valid (8-10 digits)

**Error Codes:**
- `INVALID_PLAYER_ID` (400): Invalid player UID
- `Acesso negado` (403): Insufficient API key limit
- `player_not_found` (404): Player not found
- `INSUFFICIENT_LIKES` (400): Less than 100 likes sent
- `KEY_EXPIRED` (403): External API key expired
- `LIMIT_EXCEEDED` (403): Daily limit exceeded

---

## Data Queries

> **⚠️ Premium Feature:** Requires API key with daily limit > 500 requests (Unlimited or Bot plan)

Perform data queries via Telegram bot integration.

### Query Status

Check the status of the Telegram connection.

**Endpoint:** `GET /api/v1/consulta/status`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/consulta/status" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "status": "connected",
  "message": "Telegram bot is connected and ready",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Perform Data Query

Execute a data query using the Telegram bot.

**Endpoint:** `GET /api/v1/consulta`

**Query Parameters:**
- `type` (string, required): Type of query
- `dados` (string, required): Data to query

**Available Query Types:**
- `cpf` - Query by CPF (full number)
- `nome` - Query by name
- `telefone` - Query by phone number
- `email` - Query by email
- `placa` - Query by vehicle plate
- `chassi` - Query by vehicle chassis
- `cnpj` - Query by CNPJ (company registration)
- `cep` - Query by postal code
- `titulo` - Query by voter registration
- `pai` - Query by father's name
- `mae` - Query by mother's name
- `vizinhos` - Query neighbors by CPF
- `proprietario` - Query owner by CPF
- `empregos` - Query jobs by CPF
- `vacinas` - Query vaccines by CPF
- `beneficios` - Query benefits by CPF
- `internet` - Query internet by CPF
- `parentes` - Query relatives by CPF
- `enderecos` - Query addresses by CPF
- `obito` - Query death record by CPF
- `score` - Query credit score by CPF
- `compras` - Query purchases by CPF
- `cnh` - Query driver's license by CPF
- `funcionarios` - Query employees by CNPJ

**Example Request (CPF Query):**

```bash
curl -X GET "https://cog.api.br/api/v1/consulta?type=cpf&dados=00000000000" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Request (Name Query):**

```bash
curl -X GET "https://cog.api.br/api/v1/consulta?type=nome&dados=Jo%C3%A3o%20Silva" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "type": "cpf",
    "query": "000.000.000-00",
    "resultado": "...query results...",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

**Error Codes:**
- `Acesso negado` (403): Insufficient API key limit (requires > 500/day)
- `MISSING_PARAMETERS` (400): Missing required parameters
- `INVALID_TYPE` (400): Invalid query type
- `TELEGRAM_ERROR` (503): Telegram bot connection error

**Code Examples:**

**Node.js:**
```javascript
const axios = require('axios');

async function queryData(type, data) {
  try {
    const response = await axios.get('https://cog.api.br/api/v1/consulta', {
      params: { type, dados: data },
      headers: { 'X-API-Key': 'ck_your_api_key' }
    });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error(error.response?.data || error.message);
  }
}

// Query by CPF
queryData('cpf', '00000000000');

// Query by name
queryData('nome', 'João Silva');
```

**Python:**
```python
import requests

def query_data(query_type, data):
    url = 'https://cog.api.br/api/v1/consulta'
    headers = {'X-API-Key': 'ck_your_api_key'}
    params = {'type': query_type, 'dados': data}
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Error: {response.json()}")
        return None

# Query by CPF
query_data('cpf', '00000000000')

# Query by phone
query_data('telefone', '11999999999')
```

---

## API Status

### Get API Status

Get your API key usage and limits.

**Endpoint:** `GET /api/v1/status`

**Query Parameters:**
- `include_chart` (boolean, optional): Include usage chart data

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/status?include_chart=true" \
  -H "X-API-Key: ck_your_api_key"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "api_key": {
      "id": 1,
      "name": "My API Key",
      "key_prefix": "ck_abc",
      "is_active": true,
      "created_at": "2024-01-01T00:00:00Z",
      "expires_at": null,
      "days_until_expiration": null
    },
    "limits": {
      "hourly": {
        "limit": 100,
        "used": 45,
        "remaining": 55,
        "reset_at": "2024-11-07T11:00:00Z"
      },
      "daily": {
        "requests": {
          "limit": 1000,
          "used": 234,
          "remaining": 766
        },
        "tokens": {
          "limit": 50000,
          "used": 12345,
          "remaining": 37655
        }
      }
    },
    "usage": {
      "today": {
        "requests": 45,
        "successful_requests": 42,
        "failed_requests": 3,
        "total_tokens": 5678,
        "estimated_cost": 0.05678
      },
      "last_7_days": {
        "requests": 234,
        "total_tokens": 34567,
        "estimated_cost": 0.34567,
        "success_rate": 95.3
      },
      "last_30_days": {
        "requests": 890,
        "total_tokens": 123456,
        "estimated_cost": 1.23456,
        "success_rate": 96.7
      }
    },
    "health": {
      "api_key_status": "active",
      "expiration_status": "no_expiration",
      "usage_status": "healthy"
    }
  }
}
```

### Health Check

Check API health status.

**Endpoint:** `GET /api/v1/status/health`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/status/health" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Models Statistics

Get usage statistics for all models.

**Endpoint:** `GET /api/v1/status/models?days=30`

**Query Parameters:**
- `days` (integer, optional): Number of days (default: 30)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/status/models?days=7" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Model Detailed Stats

Get detailed statistics for a specific model.

**Endpoint:** `GET /api/v1/status/:model?days=30`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/status/microsoft/phi-3-medium-128k-instruct?days=7" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Overview Stats

**Endpoint:** `GET /api/v1/status/overview`

---

## OpenAI Compatible Endpoints

For compatibility with OpenAI SDK and tools.

### Chat Completions (OpenAI Format)

**Endpoint:** `POST /openai/v1/chat/completions`

**Request Body:**

```json
{
  "model": "microsoft/phi-3-medium-128k-instruct",
  "messages": [
    {"role": "user", "content": "Hello!"}
  ],
  "max_tokens": 100,
  "temperature": 0.7,
  "stream": false
}
```

**Example with OpenAI Python SDK:**

```python
from openai import OpenAI

client = OpenAI(
    api_key="ck_your_api_key",
    base_url="https://cog.api.br/openai/v1"
)

response = client.chat.completions.create(
    model="microsoft/phi-3-medium-128k-instruct",
    messages=[
        {"role": "user", "content": "Write a haiku about coding"}
    ]
)

print(response.choices[0].message.content)
```

**Example with curl:**

```bash
curl -X POST "https://cog.api.br/openai/v1/chat/completions" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "microsoft/phi-3-medium-128k-instruct",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### List Models (OpenAI Format)

**Endpoint:** `GET /openai/v1/models`

**Example Request:**

```bash
curl -X GET "https://cog.api.br/openai/v1/models" \
  -H "X-API-Key: ck_your_api_key"
```

---

## Error Handling

### Error Response Format

```json
{
  "success": false,
  "error": "Error Type",
  "message": "Detailed error message",
  "details": ["Additional error information"]
}
```

### Common Error Codes

| Status Code | Error Type | Description |
|-------------|------------|-------------|
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Missing or invalid API key |
| 403 | Forbidden | API key inactive or expired |
| 404 | Not Found | Resource not found |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 502 | Bad Gateway | External service error |

### Rate Limit Errors

When rate limited, response includes limit information:

```json
{
  "success": false,
  "error": "Rate limit exceeded",
  "message": "Hourly rate limit exceeded",
  "limits": {
    "hourly": {
      "limit": 100,
      "used": 100,
      "remaining": 0,
      "reset_at": "2024-11-07T11:00:00Z"
    }
  }
}
```

### Validation Errors

Detailed field-level validation errors:

```json
{
  "success": false,
  "error": "Dados inválidos",
  "message": "Os dados enviados não são válidos",
  "details": [
    {
      "field": "messages",
      "message": "Pelo menos uma mensagem é obrigatória",
      "value": []
    }
  ]
}
```

---

## Code Examples

### JavaScript/Node.js

#### Chat Completion

```javascript
const axios = require('axios');

async function chatCompletion() {
  try {
    const response = await axios.post(
      'https://cog.api.br/api/v1/completion',
      {
        model: 'microsoft/phi-3-medium-128k-instruct',
        messages: [
          { role: 'user', content: 'Explain async/await in JavaScript' }
        ],
        max_tokens: 500
      },
      {
        headers: {
          'X-API-Key': 'ck_your_api_key',
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(response.data.data.choices[0].message.content);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

chatCompletion();
```


### Python

#### Chat Completion

```python
import requests

def chat_completion():
    url = 'https://cog.api.br/api/v1/completion'
    headers = {
        'X-API-Key': 'ck_your_api_key',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'microsoft/phi-3-medium-128k-instruct',
        'messages': [
            {'role': 'user', 'content': 'What is machine learning?'}
        ],
        'max_tokens': 500
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print(result['data']['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

chat_completion()
```

#### Using Custom Model

```python
def use_custom_model():
    url = 'https://cog.api.br/api/v1/completion'
    headers = {
        'X-API-Key': 'ck_your_api_key',
        'Content-Type': 'application/json'
    }
    data = {
        'model': '@cognima/coding-mentor',
        'messages': [
            {'role': 'user', 'content': 'Explain Python decorators'}
        ]
    }
    
    response = requests.post(url, json=data, headers=headers)
    print(response.json())

use_custom_model()
```

#### Download TikTok Video

```python
def download_tiktok():
    url = 'https://cog.api.br/api/v1/tiktok/download'
    headers = {
        'X-API-Key': 'ck_your_api_key',
        'Content-Type': 'application/json'
    }
    data = {
        'url': 'https://www.tiktok.com/@user/video/1234567890'
    }
    
    response = requests.post(url, json=data, headers=headers)
    result = response.json()
    
    if result['success']:
        video_url = result['data']['urls'][0]['url']
        print(f"Download URL: {video_url}")
    else:
        print(f"Error: {result['message']}")

download_tiktok()
```

### PHP

```php
<?php

function chatCompletion() {
    $url = 'https://cog.api.br/api/v1/completion';
    $apiKey = 'ck_your_api_key';
    
    $data = [
        'model' => 'microsoft/phi-3-medium-128k-instruct',
        'messages' => [
            ['role' => 'user', 'content' => 'What is PHP used for?']
        ],
        'max_tokens' => 500
    ];
    
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'X-API-Key: ' . $apiKey,
        'Content-Type: application/json'
    ]);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    $result = json_decode($response, true);
    
    if ($result['success']) {
        echo $result['data']['choices'][0]['message']['content'];
    } else {
        echo 'Error: ' . $result['message'];
    }
}

chatCompletion();
?>
```

### cURL Examples

#### Create Custom Model

```bash
curl -X POST "https://cog.api.br/api/v1/custom" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "travel-guide",
    "display_name": "Travel Guide AI",
    "personality_summary": "You are an enthusiastic travel guide with extensive knowledge of global destinations. You provide practical travel tips and exciting recommendations."
  }'
```

#### Search Lyrics

```bash
curl -X POST "https://cog.api.br/api/v1/lyrics/search" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "wonderwall oasis"}'
```

#### Download Instagram

```bash
curl -X POST "https://cog.api.br/api/v1/instagram/download" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/ABC123xyz/"}'
```

#### Google Drive Download

```bash
# Get file info
curl -X GET "https://cog.api.br/api/v1/gdrive/info?url=https://drive.google.com/file/d/1ABC123xyz/view" \
  -H "X-API-Key: ck_your_api_key"

# Download file
curl -X GET "https://cog.api.br/api/v1/gdrive/download?url=https://drive.google.com/file/d/1ABC123xyz/view" \
  -H "X-API-Key: ck_your_api_key"
```

#### MediaFire Download

```bash
# Get file info
curl -X GET "https://cog.api.br/api/v1/mediafire/info?url=https://www.mediafire.com/file/abc123xyz/arquivo.zip/file" \
  -H "X-API-Key: ck_your_api_key"

# Download file
curl -X GET "https://cog.api.br/api/v1/mediafire/download?url=https://www.mediafire.com/file/abc123xyz/arquivo.zip/file" \
  -H "X-API-Key: ck_your_api_key"
```

#### Twitter/X Download

```bash
# Get tweet info
curl -X GET "https://cog.api.br/api/v1/twitter/info?url=https://twitter.com/user/status/1234567890" \
  -H "X-API-Key: ck_your_api_key"

# Download media
curl -X GET "https://cog.api.br/api/v1/twitter/download?url=https://twitter.com/user/status/1234567890" \
  -H "X-API-Key: ck_your_api_key"
```

#### Web Search

```bash
# General web search
curl -X GET "https://cog.api.br/api/v1/search?q=artificial+intelligence&max=10" \
  -H "X-API-Key: ck_your_api_key"

# News search
curl -X GET "https://cog.api.br/api/v1/search/news?q=technology+news&max=5" \
  -H "X-API-Key: ck_your_api_key"
```

#### App Store Search

```bash
# Search both stores (Play Store + App Store)
curl -X GET "https://cog.api.br/api/v1/apps/search?q=whatsapp&num=5" \
  -H "X-API-Key: ck_your_api_key"

# Search Play Store only
curl -X GET "https://cog.api.br/api/v1/apps/playstore?q=games&num=10" \
  -H "X-API-Key: ck_your_api_key"

# Search App Store only
curl -X GET "https://cog.api.br/api/v1/apps/appstore?q=music&num=10" \
  -H "X-API-Key: ck_your_api_key"

# Get app details
curl -X GET "https://cog.api.br/api/v1/apps/details?appId=com.whatsapp&store=playStore" \
  -H "X-API-Key: ck_your_api_key"

# Get similar apps
curl -X GET "https://cog.api.br/api/v1/apps/similar?appId=com.whatsapp&store=playStore&num=5" \
  -H "X-API-Key: ck_your_api_key"
```

---

## Best Practices

### 1. API Key Security

- **Never expose API keys** in client-side code
- Store keys in environment variables
- Use different keys for development/production
- Rotate keys periodically

### 2. Error Handling

Always implement proper error handling:

```javascript
try {
  const response = await fetch(url, options);
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message);
  }
  return await response.json();
} catch (error) {
  console.error('API Error:', error);
  // Handle error appropriately
}
```

### 3. Rate Limiting

- Monitor your usage via `/api/v1/status`
- Implement exponential backoff for retries
- Cache responses when appropriate
- Use streaming for long responses

### 4. Custom Models

- Write clear, specific personality descriptions
- Test with preview before creating
- Use descriptive names
- Update prompts as needed

### 5. Performance

- Use streaming for real-time applications
- Leverage caching endpoints
- Set appropriate `max_tokens` limits
- Choose the right model for your task

---

## Support

For questions, issues, or feature requests:

- **Email**: support@cognima.com.br
- **Documentation**: https://cog.api.br/docs
- **Status Page**: https://cog.api.br/status

---

## Changelog

### Version 2.4.0 (Current)

- ✨ Free Fire Likes API (premium feature)
- ✨ Data Queries via Telegram integration (premium feature)
- 🔧 Premium features require API key with daily limit > 500
- 🔧 New plan requirements for advanced features

### Version 2.3.0

- ✨ App Store search API (Google Play + Apple App Store)
- ✨ App details and similar apps endpoints
- ✨ Multi-store search in single request

### Version 2.2.0

- ✨ Web search API (DuckDuckGo)
- ✨ News search API
- 🔧 Privacy-focused search results

### Version 2.1.0

- ✨ Google Drive file download support
- ✨ MediaFire file download support
- ✨ Twitter/X media download (videos, photos, GIFs)
- ✨ Admin panel quick key creation presets
- ✨ API key regeneration feature
- 🔧 Improved admin panel UX

### Version 2.0.0

- ✨ Custom models support
- ✨ Cognima branded models
- ✨ Social media integrations (Pinterest, TikTok, Instagram)
- ✨ YouTube download support
- ✨ Lyrics search
- ✨ OpenAI compatible endpoints
- ✨ Streaming responses
- ✨ Advanced model statistics
- 🔧 Improved error handling
- 🔧 Enhanced caching system
- 🔧 Better rate limiting

---

## License

This API is proprietary software owned by Cognima. Unauthorized use is prohibited.

© 2024 Cognima. All rights reserved.
