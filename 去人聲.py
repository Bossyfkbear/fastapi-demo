"""
去人聲腳本 (使用 Demucs)
使用前先安裝：pip install demucs
"""

import subprocess
import sys
import os

def remove_vocals(input_file, output_dir="output"):
    """
    輸入音樂檔，輸出去人聲版本 (no_vocals.wav) 和純人聲版本 (vocals.wav)
    """
    if not os.path.exists(input_file):
        print(f"找不到檔案: {input_file}")
        return

    print(f"開始處理: {input_file}")
    print("這可能需要幾分鐘，請稍候...")

    cmd = [
        sys.executable, "-m", "demucs",
        "--two-stems=vocals",
        "-o", output_dir,
        input_file
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("處理完成！")
        print(f"結果存放在: {output_dir} 資料夾內")
        print("  - no_vocals.wav：去人聲伴奏")
        print("  - vocals.wav：純人聲")
    else:
        print("執行失敗，錯誤訊息：")
        print(result.stderr)


if __name__ == "__main__":
    # 修改成你的音樂檔案路徑
    input_path = "your_music.mp3"

    remove_vocals(input_path)
