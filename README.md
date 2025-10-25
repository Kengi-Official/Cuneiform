# Cuneiform 🔺

> A natural language-based programming interface for AI prompt engineering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## What is Cuneiform?

Cuneiform is a structured, natural-language programming language designed specifically for AI prompt engineering. It provides a consistent, version-controllable, and team-friendly way to manage AI interactions.

### 🎯 Key Benefits

- **30-65% Higher Quality**: A/B testing shows significant improvement over raw natural language prompts
- **Consistency**: Same input = same output structure every time
- **Version Control**: `.cf` files work seamlessly with Git
- **Team Collaboration**: Shared templates ensure quality across teams
- **Multi-language**: Supports English, Korean, and Japanese

## 🚀 Quick Start

### Installation

```bash
pip install cuneiform-lang
```

### Your First Cuneiform Program

Create `hello.cf`:

```cf
@language: en

Task: Greeting
Output: "Hello, Cuneiform!"
```

Run it:

```bash
cuneiform run hello.cf
```

## 📊 Proven Results

Our A/B testing with 30 iterations shows:

| Metric | Natural Language | Cuneiform | Improvement |
|--------|-----------------|-----------|-------------|
| Completeness | 3.4/5 | 4.8/5 | **+41%** |
| Consistency | 3.6/5 | 4.5/5 | **+25%** |
| Requirements Met | 3.2/5 | 4.9/5 | **+53%** |

*Note: Creative tasks showed mixed results - natural language may be preferable for highly creative work.*

## 📖 Documentation

### File Format

All Cuneiform files use the `.cf` extension. The first line must specify the language:

```cf
@language: en
```

Supported languages:
- `en` - English
- `ko` - 한국어
- `ja` - 日本語

### Syntax Structure

```cf
@language: en

Task: [task_name]
Purpose: [description]
Input:
  key1 = "value1"
  key2 = "value2"
Output: [output_type]
```

### Example: Business Email

```cf
@language: en

Task: Business_Email
Purpose: Meeting request
Input:
  recipient = "Team Leader Kim"
  tone = "formal+friendly"
  slots = ["Tue 2PM", "Wed 11AM", "Thu 4PM"]
  deadline = "3d"
Output: "Email"
```

## 🛠️ Development

### Prerequisites

- Python 3.8+
- Anthropic API key

### Setup

```bash
# Clone repository
git clone https://github.com/Kengi-Official/Cuneiform.git
cd Cuneiform

# Create virtual environment
python -m venv venv
venv\Scriptsctivate

# Install dependencies
pip install -r requirements.txt
```

### Run Experiment

```bash
python tests/experiment.py
```

## 📝 License

MIT License - see LICENSE for details.
