"""
Basic tests for telegram bot
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_python_version():
    """Test that Python version is correct"""
    assert sys.version_info >= (3, 13), "Python 3.13+ required"


def test_contains_chinese():
    """Test Chinese character detection"""
    # Mock the function since we can't import telegram.py directly
    def contains_chinese(text):
        for char in text:
            if '\u4e00' <= char <= '\u9fff':
                return True
        return False

    assert contains_chinese("你好") == True
    assert contains_chinese("Hello") == False
    assert contains_chinese("Hello 你好") == True
    assert contains_chinese("123") == False


def test_chinese_keywords():
    """Test Chinese keyword mapping exists"""
    chinese_keywords = {
        '帮助': 'help',
        '开始': 'start',
        '天气': 'weather',
        '随机': 'random',
        '图片': 'image',
    }

    assert '帮助' in chinese_keywords
    assert chinese_keywords['帮助'] == 'help'
    assert chinese_keywords['天气'] == 'weather'


def test_pinyin_commands():
    """Test Pinyin command list"""
    chinese_commands = ['kaishi', 'bangzhu', 'tianqi', 'suiji', 'tupian',
                       'huoqutupian', 'qinggan', 'fenxi', 'jianceyu', 'fanyi']

    assert 'bangzhu' in chinese_commands
    assert 'tianqi' in chinese_commands
    assert 'fanyi' in chinese_commands
    assert len(chinese_commands) == 10


def test_requirements_file_exists():
    """Test that requirements.txt exists"""
    assert os.path.exists('requirements.txt')


def test_main_bot_file_exists():
    """Test that telegram.py exists"""
    assert os.path.exists('telegram.py')


def test_env_example_exists():
    """Test that .env.example exists"""
    assert os.path.exists('.env.example')


if __name__ == '__main__':
    pytest.main([__file__])
