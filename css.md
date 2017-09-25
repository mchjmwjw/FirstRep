*   伪类选择器
    1. 通用 a:hover

*   选择器

    1. ```
       H1.pastoral { color: green }  /* H1 elements with class~=pastoral */
       ```

*   标签的权值为1，类选择符的权值为10，ID选择符的权值最高为100。(权值越高，优先使用)
```css
p{color:red;} /*权值为1*/
p span{color:green;} /*权值为1+1=2*/
.warning{color:white;} /*权值为10*/
p span.warning{color:purple;} /*权值为1+1+10=12*/
#footer .note p{color:yellow;} /*权值为100+10+1=111*/
```
*   继承的权值最低，为0.1
*   层叠(后面的样式会覆盖前面的样式)
    * 由此-> 优先级: 内联>嵌入>外部引用
*   用 !important 来提高权值   
        ​```p{color:red!important;}```
    * 要写在分号前面
*   body{font-family:"Microsoft Yahei";}
*   font-style:italic; 斜体 
*   text-decoration:underline; 下划线
*   text-decoration:line-through; 删除线
*   text-indent:2em; 缩进(2em 文字的两倍大小)
*   line-height:2em; 行间距
*   word-spacing: 20px; 英文单词间距
*   letter-spacing: 20px; 字母或文字间距
*   text-align: center/left/right; 块状元素中的文本、图片设置对齐方式

*   标签元素分为:  
    1. 块状元素  
        ```
        <div> <p> <h1>...<h6> <ol> <ul> <dl> <table> <address> <blockquote> <form>
        ```
    2. 内联元素(行内元素)
        ```
        <a> <span> <br> <i> <em> <strong> <label> <q> <var> <cite> <code>
        ```
    3. 内联块状元素
        ```
        <img> <input>
        ```
*   块级元素  
    * 设置display:block;(将元素显示为块级元素)
    * 特点:  
        1. 每个块级元素都从新的一行开始，并且其后的元素也另起一行（即一个块级元素独占一行）
        2. 元素的高度、宽度、行高以及顶和底边距都可以设置
        3. 元素宽度在不设置的情况下，是它本身父容器的100%(即和父元素的宽度一致)，除非设定一个宽度

*   内联元素（行内元素）
    *   display: inline;(将元素显示为内联元素)
    *   特点: 
        1. 和其他元素都在一行上;
        2. 元素的高度、宽度以及顶部和底部边距不可设置;
        3. 元素的宽度就是它包含的文字或图片的宽度，不可改变  
        * 内联元素被当作字体处理，字体有间距则内联元素之间也有间距

*   内联块状元素
    * display: inline-block;(同时具备内联元素和块状元素的特点)
    * 特点：
        1. 和其他元素都在一行上;
        2. 元素的高度、宽度、行高以及顶和底边距都可以设置

*   border-style: dashed(虚线) | dotted(点线) | solid(实线)
*   border-bottom/top/right/left

*   布局模型
    1. 流动模型 Flow -- 默认  
        * 块状元素，自上而下，宽度默认都为100%
        * 内联元素在所处的包含元素中，从左到右
    2. 浮动模型 Float
        * 若想让块状元素并排显示，使用 float
    3. 层模型 Layer
        * 绝对定位(position: absolute;)  <strong>爹</strong>
            * 使用left、right、top、bottom属性相对于其最接近的一个具有定位属性的父包含块进行绝对定位 (如果不存在这样的包含块，则相对于body元素)
        * 相对定位(position: relative;) <strong>正常</strong>
            * 通过left、right、top、bottom属性确定元素在正常文档流中的偏移位置。 (相对定位完成的过程是首先按static(float)方式生成一个元素(并且元素像层一样浮动了起来)，然后相对于以前的位置移动，移动的方向和幅度由left、right、top、bottom属性确定，偏移前的位置保留不动)
        * 固定定位(position: fixed;)
            * 相对于浏览器视图，拖动滚动条位置固定不变
        * relative 与 absolute 的灵活使用

*   代码简写
    1. margin:10px; 上下左右的外边距都为10px
    2. margin: 10px 20px; //上下为10px 左右为20px
    3. margin: 10px 20px 30px 40px; //上右下左
    4. margin: 10px 20px 30px; // 上 左右 下

*   颜色缩写(16进制)
    1. color: #000000; 等价 color: #000;
    2. color: #336699; 等价 color: #369;

*   字体缩写 font: ... ... ...;(间隔为空格)
    1. 必须指定 font-size 和 font-family(其余未指定将使用默认值)
    2. font-size 与 line-height 之间要加入 '/'

*   颜色
    1. 英文名 red pink
    2. RGB color:rgb(123,34,200); -- 0~255之间 或者 0%~100%之间
    3. 十六进制

*   长度值
    1. 像素 px (90px=1英寸)
    2. em (1em = 1个字体大小(font-size为10px, 则1em=10px))(缩进两字符 text-indent:2em;)
        * 当给 p 的font-size 设置单位为 em 时，此时计算的标准以 p 的父元素的 font-size 为基础。
    3. 百分比
        * 行高的百分比为字体(font-size)的百分比

*   水平居中:
    1.  行内元素 父元素设置 text-align: center;
    2.  定宽块状元素 
          ```
          margin-left: auto;
          margin-right: auto;
          ```
    3.  不定宽块状元素
        1. 使用table
        2. display: inline; 配合 text-align: center;
        3. display
           ```css
            /*父元素*/
            display: float;
            position: relative;
            left: 50%;
            /*子元素*/
            position: relative;
            left: -50%;
           ```
*   垂直居中
    1. line-height 和 height
    2. css 中有一个用于竖直居中的属性 vertical-align，在父元素设置此样式时，会对inline-block类型的子元素都有用。
    3. 在 chrome、firefox 及 IE8 以上的浏览器下可以设置块级元素的 display 为 table-cell（设置为表格单元显示），激活 vertical-align 属性，但注意 IE6、7 并不支持这个样式, 兼容性比较差。 
    ```
    position:absolute; 
    float:left; 或 float:right ;
    ```
    4. 简单来说，只要html代码中出现以上两句之一，元素(除 display:none;)的display显示类型就会自动变为以 display:inline-block（块状元素）的方式显示，当然就可以设置元素的 width 和 height 了，且默认宽度不占满父元素。
