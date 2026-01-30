# Chinese Language Support / 中文语言支持

## Overview / 概述

This bot now supports Chinese language commands and features!

本机器人现在支持中文命令和功能！

## Chinese Commands / 中文命令

### Basic Commands / 基本命令

| Chinese / 中文 | English | Description / 说明 |
|---------------|---------|-------------------|
| `/开始` | `/start` | Start the bot / 开始使用机器人 |
| `/帮助` | `/help` | Get help / 获取帮助信息 |
| `/检测语言` | `/detect` | Detect language / 检测文本语言 |
| `/翻译` | `/translate` | Translate text / 翻译文本 |

### Weather / 天气

| Chinese / 中文 | English | Example / 示例 |
|---------------|---------|---------------|
| `/天气` | `/weather` | `/天气 北京` (Weather in Beijing) |

### Fun Commands / 娱乐命令

| Chinese / 中文 | English | Description / 说明 |
|---------------|---------|-------------------|
| `/随机` | `/8` (random) | Random number 1-100 / 随机数字 1-100 |
| `/图片` | `/mem` | Get meme image / 获取图片 |
| `/获取图片` | `/getimage` | Get image / 获取图片 |
| `/情感` | `/emotion` | Sentiment analysis / 情感分析 |
| `/分析` | `/emotion` | Text analysis / 文本分析 |

## New Features / 新功能

### 1. Language Detection / 语言检测

Automatically detect the language of any text.

自动检测任何文本的语言。

**Usage / 使用方法:**
```
You: /检测语言
Bot: 发送文字，我会检测语言
You: 你好世界
Bot: 🌐 Detected Language:
     • English: Chinese
     • 中文: 中文
     • Русский: Китайский
     Code: zh-cn
```

**Supported commands:**
- `/detect` (English)
- `/检测语言` (Chinese)

### 2. Translation / 翻译

Translate text between languages.

在不同语言之间翻译文本。

**Usage / 使用方法:**

**Simple translation (auto-detect source):**
```
You: /翻译
Bot: Send text to translate...
You: zh Hello world
Bot: 🌐 Translation (en → zh-cn):
     你好世界
```

**Translate to Chinese:**
```
You: /translate
You: chinese How are you today?
Bot: 🌐 Translation (en → zh-cn):
     你今天好吗？
```

**Translate to English:**
```
You: /translate
You: en 你好
Bot: 🌐 Translation (zh-cn → en):
     Hello
```

**Supported target languages:**
- `en` / `english` / `英语` - English
- `zh` / `chinese` / `中文` - Chinese

**Supported commands:**
- `/translate` (English)
- `/翻译` (Chinese)

## Examples / 示例

### Example 1: Check Weather in Chinese / 用中文查天气
```
You: /天气 上海
Bot: 22.5 clear sky, up to 25.0, at night 18.0
```

### Example 2: Get Random Number / 获取随机数
```
You: /随机
Bot: 42
```

### Example 3: Detect Language / 检测语言
```
You: /检测语言
Bot: 发送文字，我会检测语言
You: 这是一个测试
Bot: 🌐 Detected Language:
     • English: Chinese
     • 中文: 中文
     Code: zh-cn
```

### Example 4: Translate Chinese to English / 中译英
```
You: /翻译
Bot: Send text to translate...
You: en 我喜欢这个机器人
Bot: 🌐 Translation (zh-cn → en):
     I like this bot
```

### Example 5: Translate English to Chinese / 英译中
```
You: /translate
You: zh Welcome to the bot!
Bot: 🌐 Translation (en → zh-cn):
     欢迎使用机器人！
```

## Sentiment Analysis in Chinese / 中文情感分析

The sentiment analysis currently works best with English text, but you can still use it with Chinese:

情感分析目前对英文效果最好，但您仍然可以使用中文：

```
You: /情感
Bot: Send your text
You: 我今天很开心！
Bot: 😊 {'neg': 0.0, 'neu': 0.5, 'pos': 0.5, 'compound': 0.5}
```

## Technical Details / 技术细节

### Dependencies / 依赖
```
langdetect==1.0.9          # Language detection / 语言检测
googletrans==4.0.0rc1      # Translation / 翻译
```

### Installation / 安装
```bash
pip install langdetect googletrans==4.0.0rc1
```

### Supported Languages / 支持的语言

Currently supported languages:

当前支持的语言：

- English (英语)
- Chinese Simplified (简体中文)
- Chinese Traditional (繁体中文)

## Tips / 提示

1. **Weather commands work with Chinese city names:**
   - `/天气 北京` (Beijing)
   - `/天气 上海` (Shanghai)
   - `/天气 深圳` (Shenzhen)

2. **Translation format:**
   - Always specify target language first
   - Use language codes (en, zh, ru) or full names

3. **Language detection:**
   - Works with any text length
   - More text = more accurate detection
   - Minimum ~5 characters recommended

## Future Enhancements / 未来改进

- [ ] Chinese sentiment analysis model / 中文情感分析模型
- [ ] Chinese voice input/output / 中文语音输入输出
- [ ] Chinese calendar/date support / 中文日历日期支持
- [ ] Traditional Chinese support / 繁体中文支持
- [ ] Chinese idiom/slang detection / 中文成语俚语检测

## Feedback / 反馈

Found a bug or have a suggestion? Please open an issue on GitHub!

发现错误或有建议？请在 GitHub 上提交问题！

https://github.com/ruopsdev/tibo-telegram-bot/issues
