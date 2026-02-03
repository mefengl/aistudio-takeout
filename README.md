# aistudio-takeout

Convert Google AI Studio chats to Markdown.

## Install

```bash
pip install aistudio-takeout
```

## Usage

```bash
aistudio-takeout "Google AI Studio"           # Creates aistudio/*.chat.md
aistudio-takeout "Google AI Studio" output    # Creates output/*.chat.md
```

Output:
```
aistudio/
├── 2025-01-15-chat-title.chat.md
├── 2025-01-20-another-chat.chat.md
└── ...
```

## Requirements

- Python 3.8+

## License

MIT
