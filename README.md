# LLaMA-AI
這是我的個人 LLaMA 模型專案！這個專案使用 LLaMA 模型來建立個人化 AI 系統。
-------------------------------------------------------------
## 🚀 功能
- 文字對話
- 知識查詢
- 記憶功能 (未來計畫)
-------------------------------------------------------------
📂 專案結構

    main.py：主程式檔案，負責執行 LLaMA 模型。
    
    test_transformers.py：測試 Transformers 是否正常運行。
    
    models/：儲存下載的模型檔案。
    
    scripts/：額外的 Python 腳本。
    
    data/：存放資料集的資料夾。
-------------------------------------------------------------
📦 必要套件安裝
```bash

pip install -r requirements.txt

cd LLaMA-AI

-------------------------------------------------------------
2. 創建虛擬環境並啟動
python -m venv llama-env

.\llama-env\Scripts\activate  # Windows

source llama-env/bin/activate  # Linux/Mac

-------------------------------------------------------------
3. 安裝必要套件
pip install -r requirements.txt

會顯示
  torch>=2.0.0
  transformers>=4.28.0
  accelerate>=0.15.0
  sentencepiece>=0.1.97

-------------------------------------------------------------
4. 執行測試檔案 (確認 Transformers 成功載入)
python test_transformers.py

-------------------------------------------------------------
5. 執行主程式
```bash
python main.py

這個指令會啟動你的 LLaMA 模型，並讓你在終端機中與 AI 對話。輸入 exit 或 quit 可以結束對話。

-------------------------------------------------------------

📌注意事項:
這個專案需要使用者自行下載 LLaMA 模型 (meta-llama/Llama-2-7b-chat-hf) 並放到 models/ 資料夾中。
訪問模型會有48小時限制，過了時效性需重新申請權限，可以到https://huggingface.co/查詢，或是到https://github.com/meta-llama下載檔案、申請訪問權限。
