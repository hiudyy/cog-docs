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

## Spotify Search

Search for tracks on Spotify.

### Search Spotify Tracks

Search for multiple tracks on Spotify.

**Endpoint:** `GET /api/v1/spotify/search`

**Query Parameters:**
- `q` (string, required): Track name or artist (can also use: `query`, `name`)
- `limit` (number, optional): Number of results (default: 10, max: 50)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/spotify/search?q=te%20vi%20dançando&limit=5"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Spotify",
  "query": "te vi dançando",
  "total": 5,
  "results": [
    {
      "index": 1,
      "name": "te vi dançando",
      "artists": "Braga",
      "link": "https://open.spotify.com/track/0e950NUOTB4BIYXpeaqtzn"
    },
    {
      "index": 2,
      "name": "Te Vi Dançando",
      "artists": "Matheus Fernandes",
      "link": "https://open.spotify.com/track/..."
    }
  ]
}
```

### Search One Spotify Track

Search for a specific track (returns only the first result).

**Endpoint:** `GET /api/v1/spotify/search-one`

**Query Parameters:**
- `q` (string, required): Track name or artist (can also use: `query`, `name`)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/spotify/search-one?q=te%20vi%20dançando"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Spotify",
  "query": "te vi dançando",
  "result": {
    "index": 1,
    "name": "te vi dançando",
    "artists": "Braga",
    "link": "https://open.spotify.com/track/0e950NUOTB4BIYXpeaqtzn"
  }
}
```

**Response Fields:**
- `success` (boolean): Request status
- `platform` (string): Always "Spotify"
- `query` (string): Search query used
- `total` (number): Total results found (only in `/search`)
- `results` (array): Array of tracks (only in `/search`)
- `result` (object): Single track object (only in `/search-one`)
- `index` (number): Result position
- `name` (string): Track name
- `artists` (string): Artist(s) name
- `link` (string): Spotify track URL

**Error Codes:**
- `400` - Missing search parameter
- `500` - Error searching Spotify or internal error

### Download Spotify Track

Download a track from Spotify by URL.

**Endpoint:** `GET /api/v1/spotify/download`

**Query Parameters:**
- `url` (string, required): Spotify track URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/spotify/download?url=https%3A%2F%2Fopen.spotify.com%2Ftrack%2F4irM0ZydWatEXDDC7SflXS"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Spotify",
  "data": {
    "title": "Te vi de canto",
    "artists": [
      "Rô Rosa"
    ],
    "albumImage": "https://i.scdn.co/image/ab67616d00001e02e1a461f6e0c4cafc6632a270",
    "year": "2023",
    "duration": "2:08",
    "downloadUrl": "https://cdn-spotify.zm.io.vn/download/4irM0ZydWatEXDDC7SflXS/..."
  }
}
```

### Search and Download Spotify

Search for a track and automatically download it (combines search + download).

**Endpoint:** `GET /api/v1/spotify/search-download`

**Query Parameters:**
- `q` (string, required): Track name or artist (can also use: `query`, `name`)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/spotify/search-download?q=te%20vi%20de%20canto"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Spotify",
  "query": "te vi de canto",
  "track": {
    "name": "Te vi de canto",
    "artists": "Rô Rosa",
    "link": "https://open.spotify.com/track/4irM0ZydWatEXDDC7SflXS"
  },
  "download": {
    "title": "Te vi de canto",
    "artists": [
      "Rô Rosa"
    ],
    "albumImage": "https://i.scdn.co/image/ab67616d00001e02e1a461f6e0c4cafc6632a270",
    "year": "2023",
    "duration": "2:08",
    "downloadUrl": "https://cdn-spotify.zm.io.vn/download/4irM0ZydWatEXDDC7SflXS/..."
  }
}
```

**Response Fields:**
- `success` (boolean): Request status
- `platform` (string): Always "Spotify"
- `query` (string): Search query used
- `track` (object): Track information from search
  - `name` (string): Track name
  - `artists` (string): Artist(s) name
  - `link` (string): Spotify track URL
- `download` (object): Download information
  - `title` (string): Track title
  - `artists` (array): Array of artist names
  - `albumImage` (string): Album cover image URL
  - `year` (string): Release year
  - `duration` (string): Track duration (MM:SS)
  - `downloadUrl` (string): Direct download link

**Error Codes:**
- `400` - Missing search parameter or invalid URL
- `500` - Error searching/downloading from Spotify or internal error

---

## SoundCloud Search

Search for tracks on SoundCloud.

### Search SoundCloud Tracks

Search for multiple tracks on SoundCloud.

**Endpoint:** `GET /api/v1/soundcloud/search`

**Query Parameters:**
- `q` (string, required): Track name or artist (can also use: `query`, `name`)
- `limit` (number, optional): Number of results (default: 10, max: 50)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/soundcloud/search?q=te%20vi%20de%20canto&limit=5"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "SoundCloud",
  "query": "te vi de canto",
  "total": 5,
  "results": [
    {
      "id": 1530874528,
      "title": "Rô Rosa - Te vi de canto Prod. Patricio Sid.mp3",
      "artist": 492888114,
      "artwork": "https://i1.sndcdn.com/artworks-Y7UdYfaOQuI7ZG4F-N99dsQ-large.jpg",
      "duration": 134,
      "permalink_url": "https://soundcloud.com/jose-luiiz-ii/ro-rosa-te-vi-de-canto-prod",
      "playback_count": 377571,
      "likes_count": 5268,
      "genre": "Unknown",
      "created_at": "2023-06-05T00:01:08Z"
    }
  ]
}
```

### Search One SoundCloud Track

Search for a specific track (returns only the first result).

**Endpoint:** `GET /api/v1/soundcloud/search-one`

**Query Parameters:**
- `q` (string, required): Track name or artist (can also use: `query`, `name`)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/soundcloud/search-one?q=te%20vi%20de%20canto"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "SoundCloud",
  "query": "te vi de canto",
  "result": {
    "id": 1530874528,
    "title": "Rô Rosa - Te vi de canto Prod. Patricio Sid.mp3",
    "artist": 492888114,
    "artwork": "https://i1.sndcdn.com/artworks-Y7UdYfaOQuI7ZG4F-N99dsQ-large.jpg",
    "duration": 134,
    "permalink_url": "https://soundcloud.com/jose-luiiz-ii/ro-rosa-te-vi-de-canto-prod",
    "playback_count": 377571,
    "likes_count": 5268,
    "genre": "Unknown",
    "created_at": "2023-06-05T00:01:08Z"
  }
}
```

**Response Fields:**
- `success` (boolean): Request status
- `platform` (string): Always "SoundCloud"
- `query` (string): Search query used
- `total` (number): Total results found (only in `/search`)
- `results` (array): Array of tracks (only in `/search`)
- `result` (object): Single track object (only in `/search-one`)
- `id` (number): SoundCloud track ID
- `title` (string): Track title
- `artist` (number): Artist ID
- `artwork` (string): Track artwork URL
- `duration` (number): Duration in seconds
- `permalink_url` (string): SoundCloud track URL
- `playback_count` (number): Number of plays
- `likes_count` (number): Number of likes
- `genre` (string): Track genre
- `created_at` (string): Upload date

**Error Codes:**
- `400` - Missing search parameter
- `500` - Error searching SoundCloud or internal error

### Download SoundCloud Track

Download a track from SoundCloud by URL.

**Endpoint:** `GET /api/v1/soundcloud/download`

**Query Parameters:**
- `url` (string, required): SoundCloud track URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/soundcloud/download?url=https%3A%2F%2Fsoundcloud.com%2Fjose-luiiz-ii%2Fro-rosa-te-vi-de-canto-prod"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "SoundCloud",
  "data": {
    "title": "Rô Rosa - Te vi de canto Prod. Patricio Sid.mp3",
    "artist": "@jose.7uiz",
    "thumbnail": "https://i1.sndcdn.com/artworks-Y7UdYfaOQuI7ZG4F-N99dsQ-t500x500.jpg",
    "downloadUrl": "https://cf-media.sndcdn.com/LUht8AzbUqDu.128.mp3?Policy=..."
  }
}
```

### Search and Download SoundCloud

Search for a track and automatically download it (combines search + download).

**Endpoint:** `GET /api/v1/soundcloud/search-download`

**Query Parameters:**
- `q` (string, required): Track name or artist (can also use: `query`, `name`)

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/soundcloud/search-download?q=te%20vi%20de%20canto"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "SoundCloud",
  "track": {
    "id": 1530874528,
    "title": "Rô Rosa - Te vi de canto Prod. Patricio Sid.mp3",
    "artist": 492888114,
    "artwork": "https://i1.sndcdn.com/artworks-Y7UdYfaOQuI7ZG4F-N99dsQ-large.jpg",
    "duration": 134,
    "permalink_url": "https://soundcloud.com/jose-luiiz-ii/ro-rosa-te-vi-de-canto-prod",
    "playback_count": 377571,
    "likes_count": 5268,
    "genre": "Unknown",
    "created_at": "2023-06-05T00:01:08Z"
  },
  "download": {
    "title": "Rô Rosa - Te vi de canto Prod. Patricio Sid.mp3",
    "artist": "@jose.7uiz",
    "thumbnail": "https://i1.sndcdn.com/artworks-Y7UdYfaOQuI7ZG4F-N99dsQ-t500x500.jpg",
    "downloadUrl": "https://cf-media.sndcdn.com/LUht8AzbUqDu.128.mp3?Policy=..."
  }
}
```

**Response Fields:**
- `success` (boolean): Request status
- `platform` (string): Always "SoundCloud"
- `track` (object): Track information from search
  - `id` (number): SoundCloud track ID
  - `title` (string): Track title
  - `artist` (number): Artist ID
  - `artwork` (string): Track artwork URL
  - `duration` (number): Duration in seconds
  - `permalink_url` (string): SoundCloud track URL
  - `playback_count` (number): Number of plays
  - `likes_count` (number): Number of likes
  - `genre` (string): Track genre
  - `created_at` (string): Upload date
- `download` (object): Download information
  - `title` (string): Track title
  - `artist` (string): Artist username
  - `thumbnail` (string): Track thumbnail URL
  - `downloadUrl` (string): Direct download link

**Error Codes:**
- `400` - Missing search parameter or invalid URL
- `500` - Error searching/downloading from SoundCloud or internal error

---

## Facebook Download

Download videos from Facebook with multiple quality options.

### Download Facebook Video

Download a Facebook video with all available quality options.

**Endpoint:** `GET /api/v1/facebook/download`

**Query Parameters:**
- `url` (string, required): Facebook video URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/facebook/download?url=https%3A%2F%2Fwww.facebook.com%2Fshare%2Fr%2F14RStacRcih%2F"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Facebook",
  "videos": [
    {
      "resolution": "720p (HD)",
      "thumbnail": "https://scontent-vie1-1.xx.fbcdn.net/...",
      "url": "https://d.rapidcdn.app/v2?token=...",
      "shouldRender": false
    },
    {
      "resolution": "1080p",
      "thumbnail": "https://scontent-vie1-1.xx.fbcdn.net/...",
      "url": "/render.php?token=...",
      "shouldRender": true
    }
  ]
}
```

### Download Facebook HD Video

Download a Facebook video in the best available quality (HD preferred).

**Endpoint:** `GET /api/v1/facebook/download-hd`

**Query Parameters:**
- `url` (string, required): Facebook video URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/facebook/download-hd?url=https%3A%2F%2Fwww.facebook.com%2Fshare%2Fr%2F14RStacRcih%2F"
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Facebook",
  "video": {
    "resolution": "1080p",
    "thumbnail": "https://scontent-vie1-1.xx.fbcdn.net/...",
    "url": "/render.php?token=...",
    "shouldRender": true
  },
  "allQualities": [
    {
      "resolution": "720p (HD)",
      "thumbnail": "https://scontent-vie1-1.xx.fbcdn.net/...",
      "url": "https://d.rapidcdn.app/v2?token=...",
      "shouldRender": false
    },
    {
      "resolution": "1080p",
      "thumbnail": "https://scontent-vie1-1.xx.fbcdn.net/...",
      "url": "/render.php?token=...",
      "shouldRender": true
    }
  ]
}
```

**Response Fields:**
- `success` (boolean): Request status
- `platform` (string): Always "Facebook"
- `videos` (array): Array of video quality options (only in `/download`)
- `video` (object): Best quality video (only in `/download-hd`)
- `allQualities` (array): All available qualities (only in `/download-hd`)
- `resolution` (string): Video resolution (e.g., "720p (HD)", "1080p")
- `thumbnail` (string): Video thumbnail URL
- `url` (string): Direct download link
- `shouldRender` (boolean): Whether the URL needs server-side rendering

**Supported URL Formats:**
- `https://www.facebook.com/share/r/...`
- `https://www.facebook.com/watch?v=...`
- `https://fb.watch/...`
- `https://www.facebook.com/username/videos/...`

**Error Codes:**
- `400` - Missing URL parameter or invalid Facebook URL
- `500` - Error downloading from Facebook or internal error

---

## Reddit Download

Download videos and media from Reddit posts using yt-dlp.

### Download Reddit Media

Download video or media from a Reddit post.

**Endpoint:** `GET /api/v1/reddit/download`

**Query Parameters:**
- `url` (string, required): Reddit post URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/reddit/download?url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fvideos%2Fcomments%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Reddit",
  "data": {
    "title": "Amazing video title",
    "author": "username",
    "subreddit": "videos",
    "thumbnail": "https://...",
    "duration": 45,
    "downloadUrl": "https://...",
    "isVideo": true,
    "upvotes": 1250,
    "comments": 85
  }
}
```

### Get Reddit Post Info

Get information about a Reddit post without downloading.

**Endpoint:** `GET /api/v1/reddit/info`

**Query Parameters:**
- `url` (string, required): Reddit post URL

**Example Response:**

```json
{
  "success": true,
  "platform": "Reddit",
  "info": {
    "title": "Amazing video title",
    "author": "username",
    "subreddit": "videos",
    "thumbnail": "https://...",
    "duration": 45,
    "description": "Post description",
    "timestamp": 1640000000,
    "isVideo": true,
    "upvotes": 1250,
    "comments": 85,
    "url": "https://reddit.com/..."
  }
}
```

---

## Twitch Download

Download clips and VODs from Twitch using yt-dlp.

### Download Twitch Clip/VOD

Download a Twitch clip or VOD.

**Endpoint:** `GET /api/v1/twitch/download`

**Query Parameters:**
- `url` (string, required): Twitch clip or VOD URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/twitch/download?url=https%3A%2F%2Fwww.twitch.tv%2Fvideos%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Twitch",
  "data": {
    "title": "Epic Gaming Moment",
    "streamer": "StreamerName",
    "thumbnail": "https://...",
    "duration": 120,
    "downloadUrl": "https://...",
    "type": "clip",
    "views": 5000,
    "timestamp": 1640000000,
    "game": "Game Name"
  }
}
```

### Get Twitch Formats

Get available quality formats for a Twitch video.

**Endpoint:** `GET /api/v1/twitch/formats`

**Query Parameters:**
- `url` (string, required): Twitch clip or VOD URL

**Example Response:**

```json
{
  "success": true,
  "platform": "Twitch",
  "formats": [
    {
      "formatId": "source",
      "quality": "1920x1080",
      "ext": "mp4",
      "filesize": 50000000,
      "url": "https://..."
    },
    {
      "formatId": "720p60",
      "quality": "1280x720",
      "ext": "mp4",
      "filesize": 30000000,
      "url": "https://..."
    }
  ]
}
```

### Get Twitch Video Info

Get information about a Twitch clip or VOD.

**Endpoint:** `GET /api/v1/twitch/info`

**Query Parameters:**
- `url` (string, required): Twitch clip or VOD URL

---

## Vimeo Download

Download videos from Vimeo using yt-dlp.

### Download Vimeo Video

Download a video from Vimeo.

**Endpoint:** `GET /api/v1/vimeo/download`

**Query Parameters:**
- `url` (string, required): Vimeo video URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/vimeo/download?url=https%3A%2F%2Fvimeo.com%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Vimeo",
  "data": {
    "title": "Beautiful Short Film",
    "author": "Creator Name",
    "thumbnail": "https://...",
    "duration": 180,
    "downloadUrl": "https://...",
    "description": "Film description",
    "views": 10000,
    "likes": 500,
    "timestamp": 1640000000,
    "width": 1920,
    "height": 1080,
    "quality": "1080p"
  }
}
```

### Get Vimeo Formats

Get available quality formats for a Vimeo video.

**Endpoint:** `GET /api/v1/vimeo/formats`

**Query Parameters:**
- `url` (string, required): Vimeo video URL

**Example Response:**

```json
{
  "success": true,
  "platform": "Vimeo",
  "formats": [
    {
      "formatId": "http-1080p",
      "quality": "1920x1080",
      "ext": "mp4",
      "filesize": 80000000,
      "url": "https://..."
    },
    {
      "formatId": "http-720p",
      "quality": "1280x720",
      "ext": "mp4",
      "filesize": 45000000,
      "url": "https://..."
    }
  ]
}
```

### Get Vimeo Video Info

Get information about a Vimeo video.

**Endpoint:** `GET /api/v1/vimeo/info`

**Query Parameters:**
- `url` (string, required): Vimeo video URL

**Response Fields:**
- All platforms use yt-dlp for reliable downloads
- Supports multiple quality options
- Includes metadata (views, likes, duration, etc.)
- Error handling with detailed messages

**Supported URL Formats:**
- **Reddit**: `reddit.com/r/subreddit/comments/...`, `redd.it/...`
- **Twitch**: `twitch.tv/videos/...`, `twitch.tv/username/clip/...`, `clips.twitch.tv/...`
- **Vimeo**: `vimeo.com/...`

**Error Codes:**
- `400` - Missing URL parameter or invalid URL format
- `500` - Error downloading or internal error

---

## Dailymotion Download

Download videos from Dailymotion using yt-dlp.

### Download Dailymotion Video

Download a video from Dailymotion.

**Endpoint:** `GET /api/v1/dailymotion/download`

**Query Parameters:**
- `url` (string, required): Dailymotion video URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/dailymotion/download?url=https%3A%2F%2Fwww.dailymotion.com%2Fvideo%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Dailymotion",
  "data": {
    "title": "Amazing Video Title",
    "author": "Channel Name",
    "thumbnail": "https://...",
    "duration": 240,
    "downloadUrl": "https://...",
    "description": "Video description",
    "views": 15000,
    "timestamp": 1640000000,
    "width": 1920,
    "height": 1080,
    "quality": "1080p"
  }
}
```

### Get Dailymotion Formats

Get available quality formats for a Dailymotion video.

**Endpoint:** `GET /api/v1/dailymotion/formats`

**Query Parameters:**
- `url` (string, required): Dailymotion video URL

**Example Response:**

```json
{
  "success": true,
  "platform": "Dailymotion",
  "formats": [
    {
      "formatId": "1080",
      "quality": "1920x1080",
      "ext": "mp4",
      "filesize": 120000000,
      "url": "https://..."
    },
    {
      "formatId": "720",
      "quality": "1280x720",
      "ext": "mp4",
      "filesize": 70000000,
      "url": "https://..."
    }
  ]
}
```

### Get Dailymotion Video Info

Get information about a Dailymotion video.

**Endpoint:** `GET /api/v1/dailymotion/info`

**Query Parameters:**
- `url` (string, required): Dailymotion video URL

---

## Streamable Download

Download videos from Streamable using yt-dlp.

### Download Streamable Video

Download a video from Streamable.

**Endpoint:** `GET /api/v1/streamable/download`

**Query Parameters:**
- `url` (string, required): Streamable video URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/streamable/download?url=https%3A%2F%2Fstreamable.com%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Streamable",
  "data": {
    "title": "Streamable Video",
    "thumbnail": "https://...",
    "duration": 30,
    "downloadUrl": "https://...",
    "description": "Video description",
    "timestamp": 1640000000,
    "width": 1280,
    "height": 720,
    "quality": "720p",
    "filesize": 25000000
  }
}
```

### Get Streamable Formats

Get available quality formats for a Streamable video.

**Endpoint:** `GET /api/v1/streamable/formats`

**Query Parameters:**
- `url` (string, required): Streamable video URL

### Get Streamable Video Info

Get information about a Streamable video.

**Endpoint:** `GET /api/v1/streamable/info`

**Query Parameters:**
- `url` (string, required): Streamable video URL

---

## Bandcamp Download

Download music and albums from Bandcamp using yt-dlp.

### Download Bandcamp Track/Album

Download a track or album from Bandcamp.

**Endpoint:** `GET /api/v1/bandcamp/download`

**Query Parameters:**
- `url` (string, required): Bandcamp track or album URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/bandcamp/download?url=https%3A%2F%2Fartist.bandcamp.com%2Ftrack%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Bandcamp",
  "data": {
    "title": "Song Title",
    "artist": "Artist Name",
    "album": "Album Name",
    "thumbnail": "https://...",
    "duration": 210,
    "downloadUrl": "https://...",
    "description": "Track description",
    "releaseDate": "2024-01-01",
    "genre": "Electronic",
    "track": "Song Title",
    "trackNumber": 1,
    "ext": "mp3"
  }
}
```

### Get Bandcamp Formats

Get available formats for a Bandcamp track.

**Endpoint:** `GET /api/v1/bandcamp/formats`

**Query Parameters:**
- `url` (string, required): Bandcamp track URL

### Get Bandcamp Track Info

Get information about a Bandcamp track or album.

**Endpoint:** `GET /api/v1/bandcamp/info`

**Query Parameters:**
- `url` (string, required): Bandcamp track or album URL

---

## Likee Download

Download videos from Likee using yt-dlp.

### Download Likee Video

Download a video from Likee.

**Endpoint:** `GET /api/v1/likee/download`

**Query Parameters:**
- `url` (string, required): Likee video URL

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/likee/download?url=https%3A%2F%2Flikee.video%2F..."
```

**Example Response:**

```json
{
  "success": true,
  "platform": "Likee",
  "data": {
    "title": "Likee Video",
    "author": "Username",
    "thumbnail": "https://...",
    "duration": 15,
    "downloadUrl": "https://...",
    "description": "Video description",
    "views": 5000,
    "likes": 250,
    "comments": 30,
    "timestamp": 1640000000,
    "width": 1080,
    "height": 1920
  }
}
```

### Get Likee Video Info

Get information about a Likee video.

**Endpoint:** `GET /api/v1/likee/info`

**Query Parameters:**
- `url` (string, required): Likee video URL

**Response Fields:**
- All platforms use yt-dlp for reliable downloads
- Supports multiple quality options where available
- Includes metadata (views, likes, duration, etc.)
- Error handling with detailed messages

**Supported URL Formats:**
- **Dailymotion**: `dailymotion.com/video/...`, `dai.ly/...`
- **Streamable**: `streamable.com/...`
- **Bandcamp**: `artist.bandcamp.com/track/...`, `artist.bandcamp.com/album/...`
- **Likee**: `likee.video/...`, `likee.com/...`

**Error Codes:**
- `400` - Missing URL parameter or invalid URL format
- `500` - Error downloading or internal error

---

## Universal Download (AllDL)

Universal download endpoint that extracts **all available media** from any URL supported by yt-dlp. Returns an array with videos, audio tracks, and images, each with its URL and type.

### Download All Media

Extract all available media (video, audio, images) from any supported URL.

**Endpoint:** `GET /api/v1/alldl`

**Query Parameters:**
- `url` (string, required): Any URL supported by yt-dlp

**Supported Platforms:**
- YouTube, Vimeo, Dailymotion, Twitch, TikTok, Instagram, Facebook
- Twitter/X, Reddit, Streamable, Bandcamp, SoundCloud, Spotify
- Likee, and 1000+ other sites

**Example Request:**

```bash
curl -X GET "https://cog.api.br/api/v1/alldl?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ"
```

**Example Response:**

```json
{
  "success": true,
  "data": {
    "metadata": {
      "title": "Video Title",
      "description": "Video description",
      "duration": 213,
      "uploader": "Channel Name",
      "uploadDate": "20240101",
      "views": 1000000,
      "likes": 50000,
      "webpage": "https://...",
      "platform": "youtube"
    },
    "media": [
      {
        "type": "video",
        "url": "https://...",
        "quality": "best",
        "format": "mp4",
        "filesize": 50000000,
        "resolution": "1920x1080",
        "duration": 213,
        "title": "Video Title",
        "description": "Best quality available",
        "isBest": true
      },
      {
        "type": "video",
        "url": "https://...",
        "quality": "1920x1080",
        "format": "mp4",
        "filesize": 48000000,
        "resolution": "1920x1080",
        "fps": 30,
        "vcodec": "h264",
        "acodec": "aac",
        "formatId": "137+140"
      },
      {
        "type": "video",
        "url": "https://...",
        "quality": "1280x720",
        "format": "mp4",
        "filesize": 25000000,
        "resolution": "1280x720",
        "fps": 30,
        "vcodec": "h264",
        "acodec": "aac",
        "formatId": "136+140"
      },
      {
        "type": "audio",
        "url": "https://...",
        "quality": "128kbps",
        "format": "m4a",
        "filesize": 3000000,
        "acodec": "aac",
        "abr": 128,
        "asr": 44100,
        "formatId": "140"
      },
      {
        "type": "image",
        "url": "https://i.ytimg.com/vi/.../maxresdefault.jpg",
        "quality": "1280x720",
        "width": 1280,
        "height": 720,
        "id": "maxresdefault"
      },
      {
        "type": "image",
        "url": "https://i.ytimg.com/vi/.../hqdefault.jpg",
        "quality": "480x360",
        "width": 480,
        "height": 360,
        "id": "hqdefault"
      }
    ],
    "totalItems": 15,
    "videoCount": 8,
    "audioCount": 5,
    "imageCount": 2
  }
}
```

**Response Fields:**

- `metadata` - Video/content metadata
  - `title` - Content title
  - `description` - Content description
  - `duration` - Duration in seconds
  - `uploader` - Channel/uploader name
  - `uploadDate` - Upload date (YYYYMMDD)
  - `views` - View count
  - `likes` - Like count
  - `webpage` - Original webpage URL
  - `platform` - Platform name (youtube, vimeo, etc.)

- `media[]` - Array of all available media
  - `type` - Media type: `video`, `audio`, or `image`
  - `url` - Direct download URL
  - `quality` - Quality description (resolution, bitrate, etc.)
  - `format` - File extension (mp4, webm, m4a, jpg, etc.)
  - `filesize` - File size in bytes (when available)
  - `isBest` - True for the recommended best quality option

- Video-specific fields:
  - `resolution` - Video resolution (1920x1080, etc.)
  - `fps` - Frames per second
  - `vcodec` - Video codec (h264, vp9, etc.)
  - `acodec` - Audio codec (aac, opus, etc.)
  - `formatId` - Format identifier

- Audio-specific fields:
  - `acodec` - Audio codec
  - `abr` - Audio bitrate in kbps
  - `asr` - Audio sample rate

- Image-specific fields:
  - `width` - Image width in pixels
  - `height` - Image height in pixels
  - `id` - Thumbnail identifier

- `totalItems` - Total number of media items
- `videoCount` - Number of video formats
- `audioCount` - Number of audio formats
- `imageCount` - Number of images/thumbnails

### Download by Type

Get media filtered by type (video, audio, or image only).

**Endpoint:** `GET /api/v1/alldl/type`

**Query Parameters:**
- `url` (string, required): Any URL supported by yt-dlp
- `type` (string, required): Media type to filter - `video`, `audio`, or `image`

**Example Request:**

```bash
# Get only audio tracks
curl -X GET "https://cog.api.br/api/v1/alldl/type?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&type=audio"

# Get only images/thumbnails
curl -X GET "https://cog.api.br/api/v1/alldl/type?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ&type=image"
```

**Example Response (audio only):**

```json
{
  "success": true,
  "data": {
    "metadata": {
      "title": "Video Title",
      "description": "Video description",
      "duration": 213,
      "uploader": "Channel Name",
      "platform": "youtube"
    },
    "media": [
      {
        "type": "audio",
        "url": "https://...",
        "quality": "128kbps",
        "format": "m4a",
        "filesize": 3000000,
        "acodec": "aac",
        "abr": 128,
        "asr": 44100,
        "formatId": "140"
      },
      {
        "type": "audio",
        "url": "https://...",
        "quality": "96kbps",
        "format": "webm",
        "filesize": 2200000,
        "acodec": "opus",
        "abr": 96,
        "asr": 48000,
        "formatId": "251"
      }
    ],
    "totalItems": 2
  }
}
```

**Use Cases:**

1. **Download Manager** - Present all available quality options to users
2. **Thumbnail Extractor** - Get all thumbnail sizes for a video
3. **Audio Ripper** - Extract only audio tracks in various formats
4. **Format Converter** - Choose specific codecs and resolutions
5. **Bandwidth Optimization** - Select appropriate quality based on connection
6. **Multi-Quality Player** - Implement adaptive streaming with multiple sources

**Features:**

- ✅ Universal support for 1000+ websites via yt-dlp
- ✅ Returns ALL available formats (not just best quality)
- ✅ Includes video, audio, and image URLs
- ✅ Detailed metadata for each media item
- ✅ Filter by media type (video/audio/image)
- ✅ File size information when available
- ✅ Codec and quality information
- ✅ Thumbnail URLs in multiple resolutions

**Error Codes:**
- `400` - Missing URL parameter, invalid URL format, or invalid type parameter
- `500` - Error extracting media or unsupported URL

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

Full code examples are available in the `/examples` directory:
- **Node.js**: `/examples/nodejs/`
- **Python**: `/examples/python/`

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

#### Spotify Search

See full example: [`/examples/nodejs/spotify.js`](./examples/nodejs/spotify.js)

```javascript
const axios = require('axios');

async function searchSpotify(query, limit = 10) {
  const response = await axios.get(
    'https://cog.api.br/api/v1/spotify/search',
    {
      params: { q: query, limit }
    }
  );
  
  const { results } = response.data;
  results.forEach(track => {
    console.log(`${track.name} - ${track.artists}`);
    console.log(`Link: ${track.link}`);
  });
}

searchSpotify('te vi dançando', 5);
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

#### Spotify Search

See full example: [`/examples/python/spotify.py`](./examples/python/spotify.py)

```python
import requests

def search_spotify(query, limit=10):
    response = requests.get(
        'https://cog.api.br/api/v1/spotify/search',
        params={'q': query, 'limit': limit}
    )
    
    data = response.json()
    for track in data['results']:
        print(f"{track['name']} - {track['artists']}")
        print(f"Link: {track['link']}")

search_spotify('te vi dançando', 5)
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

### 4. Performance

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
