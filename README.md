# 用人间失格生成词云

最近网抑云很火。就想着弄一个生成最有B格的网抑云。

![人间失格](https://zouyishan.oss-cn-beijing.aliyuncs.com/images/20201204122421)



生成的背景图片可以改。直接把项目中的1.jpg换下来就行。(注意图片的颜色对比要鲜明点 不然效果很差)。如果不想要背景图片的话就直接注释掉代码中的 `mask=alice_coloring`就行，这个我也生成了一个

![网抑云](https://zouyishan.oss-cn-beijing.aliyuncs.com/images/20201204122419)



然后不用删`人间失格.png`生成的图片是可以直接覆盖的。

如果有些词你不想要可以在cn_stopwords.txt中删除和添加。比如上面张图片不想要`所谓`这两个词。就可以在里面添加所谓这两个词。生成的图片中就不会有所谓了。

祝你成为12点最抑的崽
