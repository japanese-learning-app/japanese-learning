#!/usr/bin/env python3
import re
from datetime import datetime

def update_cache_busting():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    version_str = f"v67_permanent_future_word_protection_v71_romaji_loop_{timestamp}"

    # 1. Update index.html & public/index.html
    html_files = [
        'index.html',
        'public/index.html'
    ]
    for hf in html_files:
        try:
            with open(hf, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace ?v=... on script tags
            new_content = re.sub(r'(\.js)\?v=[0-9_]+', rf'\1?v={timestamp}', content)
            
            if new_content != content:
                with open(hf, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ✓ Updated cache busting query strings in {hf} to {timestamp}")
        except Exception as e:
            print(f"  ⚠ Failed to update {hf}: {e}")

    # 2. Update js/app.js & public/js/app.js CURRENT_DATA_VERSION
    app_files = [
        'js/app.js',
        'public/js/app.js'
    ]
    for af in app_files:
        try:
            with open(af, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = re.sub(
                r"const CURRENT_DATA_VERSION = ['\"][^'\"]+['\"];",
                f"const CURRENT_DATA_VERSION = '{version_str}';",
                content
            )

            if new_content != content:
                with open(af, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  ✓ Updated CURRENT_DATA_VERSION in {af} to {version_str}")
        except Exception as e:
            print(f"  ⚠ Failed to update {af}: {e}")

if __name__ == '__main__':
    update_cache_busting()
