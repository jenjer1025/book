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

## 序與首頁簡介
- 序放在 `chapters/00-序.md`。檔名以 `00` 開頭會標示為「序」、網址為 `preface.html`，並排在第一章之前。
- 首頁簡介放在 `intro.md`，每一行是一個段落。修改後執行 `python3 build.py` 再推送。

## 在章節加入影片
在章節檔第一行（`# 章名`）的下一行加上：
```
video: 影片網址或檔名
```
- YouTube：直接貼網址，例如 `video: https://www.youtube.com/watch?v=XXXXXXXXXXX`（會以 youtube-nocookie 嵌入）。
- 自己的 MP4：把檔案放進 `videos/` 資料夾（檔名建議用英文，例如 `chapter-02.mp4`），再寫 `video: chapter-02.mp4`。若有同名的 `.jpg`（如 `chapter-02.jpg`），會自動當作封面圖。
- 影片會顯示在章名下方、內文上方，並標示「影片版」。
- 建議先把影片壓縮成 720p、40MB 以下（GitHub 單檔上限 100MB）：
  ```
  ffmpeg -i 原檔.mp4 -vf scale=-2:720 -c:v libx264 -crf 26 -c:a aac -b:a 96k -movflags +faststart videos/chapter-02.mp4
  ```

## 修改書名／作者
編輯 `config.json` 的 `title`、`author`、`description`，再執行 `python3 build.py` 並照上面第 5 步推送。

## 外觀
修改 `style.css`，重新 build 後推送。讀者可在頁面右上角切換深色模式及調整字體大小。
