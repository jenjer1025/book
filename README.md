# 我的書 — 靜態閱讀網站

線上閱讀：https://jenjer1025.github.io/book/

## 新增章節並重新發佈
1. 在 `chapters/` 資料夾新增一個文字檔，例如 `02-第二幕.md`（檔名開頭的數字決定順序）。
2. 第一行寫章名，前面加 `# `，例如：`# 第二幕〈標題〉`。
3. 接著貼上內文，每一行就是一個段落。場景分隔請單獨一行寫 `＊　＊　＊`。
4. 產生網頁（輸出到 `docs/`）：
   ```
   python3 build.py
   ```
5. 上傳到 GitHub，約 1 分鐘後網站自動更新：
   ```
   git add .
   git commit -m "新增第二章"
   git push
   ```
（網站由 GitHub Pages 從 `main` 分支的 `/docs` 資料夾發佈。）

## 修改書名／作者
編輯 `config.json` 的 `title`、`author`、`description`，再執行 `python3 build.py` 並照上面第 5 步推送。

## 外觀
修改 `style.css`，重新 build 後推送。讀者可在頁面右上角切換深色模式及調整字體大小。
