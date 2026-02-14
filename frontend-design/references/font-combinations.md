# 字体组合参考

## 概述

本文档提供精心策划的字体组合方案，避免使用通用字体（Inter、Roboto、Arial等），帮助创建独特的前端设计。

---

## 极简/优雅风格

### 组合1：经典衬线
- **展示字体**：Playfair Display (700)
- **正文字体**：Source Serif Pro (400, 600)
- **适用场景**：高端品牌、奢侈品、艺术作品集
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Serif+Pro:wght@400;600&display=swap" rel="stylesheet">
  ```

### 组合2：精致现代
- **展示字体**：Cormorant Garamond (700)
- **正文字体**：Lora (400, 500)
- **适用场景**：时尚、设计工作室、文化机构
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&family=Lora:wght@400;500&display=swap" rel="stylesheet">
  ```

### 组合3：简约优雅
- **展示字体**：Crimson Text (700)
- **正文字体**：Merriweather (300, 400)
- **适用场景**：出版、博客、内容平台
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Crimson+Text:wght@700&family=Merriweather:wght@300;400&display=swap" rel="stylesheet">
  ```

---

## 现代/科技风格

### 组合4：未来科技
- **展示字体**：Orbitron (700, 900)
- **正文字体**：Rajdhani (400, 600)
- **适用场景**：科技产品、游戏、未来主义设计
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@400;600&display=swap" rel="stylesheet">
  ```

### 组合5：现代几何
- **展示字体**：Exo 2 (700, 800)
- **正文字体**：Work Sans (400, 500)
- **适用场景**：SaaS产品、科技公司、创业公司
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700;800&family=Work+Sans:wght@400;500&display=swap" rel="stylesheet">
  ```

### 组合6：技术专业
- **展示字体**：Space Mono (700)
- **正文字体**：IBM Plex Sans (400, 600)
- **适用场景**：开发工具、技术文档、代码编辑器
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@700&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
  ```

---

## 玩趣/创意风格

### 组合7：活力玩趣
- **展示字体**：Righteous (400)
- **正文字体**：Quicksand (400, 600)
- **适用场景**：儿童产品、娱乐应用、创意工作室
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Righteous&family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
  ```

### 组合8：圆润可爱
- **展示字体**：Fredoka (700)
- **正文字体**：Nunito (400, 600)
- **适用场景**：教育、社交、生活方式应用
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@700&family=Nunito:wght@400;600&display=swap" rel="stylesheet">
  ```

### 组合9：手写风格
- **展示字体**：Pacifico (400)
- **正文字体**：Comfortaa (400, 600)
- **适用场景**：个人博客、创意作品、手工艺品
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Comfortaa:wght@400;600&display=swap" rel="stylesheet">
  ```

---

## 编辑/杂志风格

### 组合10：大胆编辑
- **展示字体**：Bebas Neue (400)
- **正文字体**：Libre Franklin (400, 600)
- **适用场景**：新闻、杂志、媒体平台
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Libre+Franklin:wght@400;600&display=swap" rel="stylesheet">
  ```

### 组合11：现代杂志
- **展示字体**：Oswald (700)
- **正文字体**：Archivo (400, 500)
- **适用场景**：时尚杂志、生活方式、品牌故事
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Archivo:wght@400;500&display=swap" rel="stylesheet">
  ```

### 组合12：粗犷标题
- **展示字体**：Anton (400)
- **正文字体**：Public Sans (400, 600)
- **适用场景**：体育、活动、宣传页面
- **Google Fonts**：
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Public+Sans:wght@400;600&display=swap" rel="stylesheet">
  ```

---

## 使用建议

### 字体大小比例

```css
:root {
  /* 展示字体 */
  --font-display-xl: 4rem;    /* 64px */
  --font-display-lg: 3rem;    /* 48px */
  --font-display-md: 2rem;    /* 32px */

  /* 正文字体 */
  --font-body-lg: 1.25rem;    /* 20px */
  --font-body-md: 1rem;       /* 16px */
  --font-body-sm: 0.875rem;   /* 14px */
}
```

### 字重使用

- **展示字体**：使用700-900的粗字重，创造视觉冲击
- **正文字体**：使用400（常规）和600（半粗）两个字重
- **避免**：不要使用过多字重，保持简洁

### 行高设置

```css
/* 展示字体：紧凑行高 */
h1, h2, h3 {
  line-height: 1.2;
}

/* 正文字体：舒适行高 */
p, li {
  line-height: 1.6;
}
```

### 字间距调整

```css
/* 展示字体：适当收紧 */
h1 {
  letter-spacing: -0.02em;
}

/* 正文字体：保持默认或略微放宽 */
p {
  letter-spacing: 0.01em;
}
```

---

## 避免使用的字体

以下字体过于通用，应避免使用：

❌ **系统字体**：
- Arial
- Helvetica
- Times New Roman
- Georgia

❌ **过度使用的现代字体**：
- Inter
- Roboto
- Open Sans
- Lato
- Montserrat
- Poppins

❌ **缺乏个性的字体**：
- system-ui
- -apple-system
- BlinkMacSystemFont

---

## 字体加载优化

### 使用font-display

```css
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-display: swap; /* 避免FOIT */
}
```

### 预加载关键字体

```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

### 字体子集化

只加载需要的字符集，减小文件大小：
```
?family=Playfair+Display:wght@700&text=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
```

---

## 总结

选择字体时记住：
1. **避免通用**：不使用Inter、Roboto等常见字体
2. **配对协调**：展示字体大胆，正文字体易读
3. **保持一致**：整个项目使用2-3种字体
4. **考虑性能**：优化字体加载，提升用户体验
5. **测试可读性**：确保在不同设备和尺寸下都清晰可读
