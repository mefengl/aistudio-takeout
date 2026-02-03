# aistudio-takeout

Convert Google AI Studio chats to Markdown.

## Install

```bash
uv tool install aistudio-takeout
```

## Usage

```bash
aistudio-takeout "Google AI Studio"           # Creates aistudio/*.chat.md
aistudio-takeout "Google AI Studio" output    # Creates output/*.chat.md
```

Output:
```
aistudio/
├── 2025-01-15-乔治霍兹的轻量化栈.chat.md
├── 2025-01-20-founder-mode.chat.md
└── ...
```

## Requirements

- Python 3.8+

## License

MIT
