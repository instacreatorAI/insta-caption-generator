# Instagram Caption Generator ✨

A Python CLI tool that generates engaging Instagram captions with hashtags. Supports multiple topics, moods (motivational / funny / aesthetic), and Hinglish captions for high engagement.

## Features

- **8 Topics**: travel, adventure, selflove, fitness, food, fashion, nature, love
- **3 Moods per topic**: motivational, funny, aesthetic
- **120 curated captions** with emojis and Hinglish flair
- **Auto-generated hashtags** per topic
- **Ready-to-copy output** (caption + hashtags)
- **Zero dependencies** — uses only the Python standard library
- **Importable as a module** for use in other projects

## Quick Start

```bash
python caption_generator.py
```

Follow the interactive prompts to pick a topic, mood, and number of captions.

## Use as a Module

```python
from caption_generator import generate_caption, generate_hashtags, format_post

caption = generate_caption("travel", mood="funny")
tags = generate_hashtags("travel", count=5)
print(format_post(caption, tags))
```

## Available Topics & Moods

| Topic | Moods |
|-------|-------|
| travel | motivational, funny, aesthetic |
| adventure | motivational, funny, aesthetic |
| selflove | motivational, funny, aesthetic |
| fitness | motivational, funny, aesthetic |
| food | motivational, funny, aesthetic |
| fashion | motivational, funny, aesthetic |
| nature | motivational, funny, aesthetic |
| love | motivational, funny, aesthetic |

## License

MIT
