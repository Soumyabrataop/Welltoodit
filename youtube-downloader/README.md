# 🎬 YT Downloader

A beautiful web application to download YouTube videos in different formats and qualities with original language audio.

## Features

- 🎯 Clean, modern UI with dark gradient theme
- 🎥 Download videos in multiple resolutions (144p to 4K)
- 🎵 Audio-only format (M4A/AAC)
- 🌐 Downloads in original language (avoids dubbed versions)
- 📊 Simple table view with quality, type, and download options
- ⚡ Fast and responsive

## Quick Start

1. **Clone or download this repository**

2. **Install Python dependencies:**

   ```bash
   cd Yt_dowloader
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

4. **Open your browser:**

   Navigate to `http://127.0.0.1:5000`

## Usage

1. Paste a YouTube URL into the input field
2. Click "Probe Formats" to fetch available quality options
3. Browse the table showing:
   - **Quality:** Resolution (360p, 720p, 1080p, etc.) or M4A for audio
   - **Type:** Audio Only or Video + Audio
   - **Download button:** Click to download that format
4. The download will start automatically in your browser

## System Requirements

### Required:
- **Python 3.7+** (tested with Python 3.13)
- **pip** (Python package manager)

### Python Dependencies (auto-installed):
- Flask >= 2.0
- yt-dlp >= 2023.12.1
- Flask-Cors
- pytest (for testing)

### Optional (for better compatibility):
- **ffmpeg** - Recommended for audio extraction and format merging
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - macOS: `brew install ffmpeg`
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Project Structure

```
Yt_dowloader/
├── app.py              # Flask backend server
├── downloader.py       # yt-dlp wrapper (format listing & downloading)
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/
│   └── index.html     # Main UI page
├── static/
│   ├── styles.css     # Modern styling
│   └── app.js         # Frontend logic
└── tests/
    └── test_imports.py # Basic tests
```

## How It Works

1. **Format Probing:** When you enter a URL and click "Probe Formats":
   - The backend uses yt-dlp to fetch all available formats
   - Filters to show only original language audio (no dubs)
   - Returns curated quality options (best for each resolution)

2. **Download:** When you click a download button:
   - Flask creates a temporary directory
   - yt-dlp downloads the video in the selected format
   - The file is streamed back to your browser
   - Temporary files are cleaned up automatically

3. **Language Selection:** 
   - Automatically detects the video's original language
   - Only shows formats with original audio
   - Avoids dubbed or translated versions

## Troubleshooting

### "Requested format is not available" error:
- This can happen with some videos. Try a different quality option.
- Make sure you have the latest yt-dlp: `pip install --upgrade yt-dlp`

### Downloads are slow:
- This depends on your internet connection
- YouTube may throttle download speeds
- Try lower quality options for faster downloads

### "ffmpeg not found" warning:
- This is optional but recommended
- Install ffmpeg (see System Requirements above)
- The app will still work without it for most formats

### No formats showing:
- The video might be private, deleted, or region-locked
- Try a different YouTube URL
- Check your internet connection

## Development

### Running Tests:
```bash
source .venv/bin/activate
pytest -v
```

### Debug Mode:
The app runs in debug mode by default (auto-reloads on code changes)

## Production Deployment

For production use, replace the development server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Important for production:**
- Add rate limiting (Flask-Limiter)
- Add authentication
- Use HTTPS
- Implement proper file cleanup
- Add download queue system
- Set up logging

## Tech Stack

- **Backend:** Flask + yt-dlp
- **Frontend:** Vanilla JavaScript, HTML5, CSS3
- **Design:** Dark gradient theme with glassmorphism effects
- **Icons:** Emoji-based (no external dependencies)

## Known Limitations

- File sizes not shown (YouTube doesn't always provide this info)
- Some videos may be unavailable due to YouTube restrictions
- Downloads are synchronous (may block for large files)
- Temporary files stored in system temp (cleanup on completion)

## License

MIT

## Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader
- [Flask](https://flask.palletsprojects.com/) - Web framework
