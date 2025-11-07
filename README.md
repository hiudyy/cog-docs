# Cognima API - Complete Documentation

Welcome to the Cognima API documentation! This guide provides detailed information on how to use all available endpoints.

**Base URL:** `https://cog2.cognima.com.br`

## Table of Contents

- [Authentication](#authentication)
- [Rate Limits](#rate-limits)
- [AI Models](#ai-models)
  - [List Models](#list-models)
  - [Get Model Info](#get-model-info)
  - [Chat Completion](#chat-completion)
  - [Image Generation](#image-generation)
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
curl -X GET "https://cog2.cognima.com.br/api/v1/models?include_stats=true" \
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
curl -X GET "https://cog2.cognima.com.br/api/v1/models/microsoft" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Models by Type

Filter models by type (chat, image, completion).

**Endpoint:** `GET /api/v1/models/:type`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/models/chat" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Model Info

Get detailed information about a specific model.

**Endpoint:** `GET /api/v1/models/:id/info`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/models/microsoft/phi-3-medium-128k-instruct/info" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Thinking Models

Get models that support advanced thinking mode.

**Endpoint:** `GET /api/v1/models/thinking`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/models/thinking" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/completion" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/completion" \
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

### Image Generation

Generate images using AI models.

**Endpoint:** `POST /api/v1/generate`

**Request Body:**

```json
{
  "model": "deepimg",
  "prompt": "A beautiful sunset over mountains",
  "negative_prompt": "blurry, low quality",
  "size": "1024x1024",
  "quality": "standard",
  "n": 1,
  "response_format": "url"
}
```

**Parameters:**

- `model` (string, required): Image model ID
- `prompt` (string, required): Image description (1-4000 chars)
- `negative_prompt` (string, optional): What to avoid (max 4000 chars)
- `size` (string, optional): Image dimensions (default: "1024x1024")
  - Options: "256x256", "512x512", "1024x1024", "1024x1792", "1792x1024"
- `quality` (string, optional): "standard" or "hd"
- `style` (string, optional): Image style
- `n` (integer, optional): Number of images (1-10, default: 1)
- `response_format` (string, optional): "url" or "b64_json"
- `guidance_scale` (number, optional): Guidance strength (1-20, default: 7.5)
- `num_inference_steps` (integer, optional): Generation steps (1-150, default: 50)
- `seed` (integer, optional): Random seed
- `scheduler` (string, optional): Scheduler algorithm
- `safety_checker` (boolean, optional): Enable safety filter (default: true)

**Example Request:**

```bash
curl -X POST "https://cog2.cognima.com.br/api/v1/generate" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepimg",
    "prompt": "A futuristic city with flying cars",
    "size": "1024x1024",
    "quality": "hd"
  }'
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "created": 1699999999,
    "data": [
      {
        "url": "https://example.com/image.png",
        "revised_prompt": "A futuristic city...",
        "size": "1024x1024",
        "quality": "hd",
        "index": 1
      }
    ]
  },
  "usage": {
    "images_generated": 1,
    "estimated_cost": 0.04
  },
  "request_id": "img_1699999999_xyz789",
  "processing_time_ms": 3456
}
```

### Get Image Models

List all available image generation models.

**Endpoint:** `GET /api/v1/generate/models`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/generate/models" \
  -H "X-API-Key: ck_your_api_key"
```

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
curl -X POST "https://cog2.cognima.com.br/api/v1/custom" \
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
curl -X GET "https://cog2.cognima.com.br/api/v1/custom?page=1&limit=10" \
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
curl -X GET "https://cog2.cognima.com.br/api/v1/custom/123" \
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
curl -X PUT "https://cog2.cognima.com.br/api/v1/custom/123" \
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
curl -X DELETE "https://cog2.cognima.com.br/api/v1/custom/123" \
  -H "X-API-Key: ck_your_api_key"
```

### Using Custom Models

Use your custom model in chat completions:

```bash
curl -X POST "https://cog2.cognima.com.br/api/v1/completion" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/pinterest/search" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/pinterest/download" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/tiktok/download" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/tiktok/search" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/instagram/download" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/youtube/search" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/youtube/mp3" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/youtube/mp3" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/youtube/mp4" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/lyrics/search" \
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

### Movies

#### List Movies

Get available movies from cache.

**Endpoint:** `GET /api/v1/filmes`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/filmes" \
  -H "X-API-Key: ck_your_api_key"
```

#### Search Movie

Search for a specific movie.

**Endpoint:** `GET /api/v1/filmes/buscar?nome=movie_name`

**Query Parameters:**
- `nome` (string, required): Movie name to search

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/filmes/buscar?nome=inception" \
  -H "X-API-Key: ck_your_api_key"
```

#### Get Movie Details

Get detailed information about a movie.

**Endpoint:** `GET /api/v1/filmes/:id`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/filmes/123" \
  -H "X-API-Key: ck_your_api_key"
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
curl -X GET "https://cog2.cognima.com.br/api/v1/status?include_chart=true" \
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
curl -X GET "https://cog2.cognima.com.br/api/v1/status/health" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Models Statistics

Get usage statistics for all models.

**Endpoint:** `GET /api/v1/status/models?days=30`

**Query Parameters:**
- `days` (integer, optional): Number of days (default: 30)

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/status/models?days=7" \
  -H "X-API-Key: ck_your_api_key"
```

### Get Model Detailed Stats

Get detailed statistics for a specific model.

**Endpoint:** `GET /api/v1/status/:model?days=30`

**Example Request:**

```bash
curl -X GET "https://cog2.cognima.com.br/api/v1/status/microsoft/phi-3-medium-128k-instruct?days=7" \
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
    base_url="https://cog2.cognima.com.br/openai/v1"
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
curl -X POST "https://cog2.cognima.com.br/openai/v1/chat/completions" \
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
curl -X GET "https://cog2.cognima.com.br/openai/v1/models" \
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
      'https://cog2.cognima.com.br/api/v1/completion',
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

#### Image Generation

```javascript
async function generateImage() {
  try {
    const response = await axios.post(
      'https://cog2.cognima.com.br/api/v1/generate',
      {
        model: 'deepimg',
        prompt: 'A serene mountain landscape at sunset',
        size: '1024x1024'
      },
      {
        headers: {
          'X-API-Key': 'ck_your_api_key',
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Image URL:', response.data.data.data[0].url);
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

generateImage();
```

### Python

#### Chat Completion

```python
import requests

def chat_completion():
    url = 'https://cog2.cognima.com.br/api/v1/completion'
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
    url = 'https://cog2.cognima.com.br/api/v1/completion'
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
    url = 'https://cog2.cognima.com.br/api/v1/tiktok/download'
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
    $url = 'https://cog2.cognima.com.br/api/v1/completion';
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
curl -X POST "https://cog2.cognima.com.br/api/v1/custom" \
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
curl -X POST "https://cog2.cognima.com.br/api/v1/lyrics/search" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "wonderwall oasis"}'
```

#### Download Instagram

```bash
curl -X POST "https://cog2.cognima.com.br/api/v1/instagram/download" \
  -H "X-API-Key: ck_your_api_key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/ABC123xyz/"}'
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
- **Documentation**: https://cog2.cognima.com.br/docs
- **Status Page**: https://cog2.cognima.com.br/status

---

## Changelog

### Version 2.0.0 (Current)

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
