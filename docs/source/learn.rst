============
一级标题
============

二级标题
============

三级标题
----------

四级标题
^^^^^^^^^^^

五级标题
""""""""""""

六级标题
***********


*斜体文本*

**加粗文本**

``等宽文本``

E = mc\ :sup:`2`

H\ :sub:`2`\ O

\*BSD



:emphasis:`斜体文本`

:strong:`加粗文本`

:literal:`等宽文本`

:title-reference:`书籍标题`

E = mc\ :superscript:`2`

H\ :subscript:`2`\ O


.. toctree::
   :maxdepth: 2

   intro
   strings
   datatypes
   numeric
   (many more documents listed here)


.. danger::
   Beware killer rabbits!

.. Caution:: Don't take any wooden nickels.

.. note:: 这是一条注释警告。
   这是第一段的第二行。

   - 注释包含
     以下所有缩进的正文元素。
   - 其中包括此项目符号列表。


| 这里是段落

  缩进的段落被视为引文。

| 这里也是段落

  缩进的段落被视为引文。

| 这里还是段落

  缩进的段落被视为引文。
  

下面是行块内容：
 | 这是一段行块内容
 | 这同样也是行块内容
   还是行块内容

这是新的一段。


下面是文字块内容：
::

   这是一段文字块
   同样也是文字块
   还是文字块

这是新的一段。


定义1
  这是定义1的内容

定义2
  这是定义2的内容


:标题: reStructuredText语法说明

:作者:
 - Seay
 - Seay1
 - Seay2

:时间: 2017年12月12日

:概述: 这是一篇
 关于reStructuredText的语法说明。

 你在这里可以了解更多语法信息。



-------------

* 符号列表1
* 符号列表2

  * 符号列表2-嵌套1
  * 符号列表2-嵌套2
  * 符号列表2-嵌套3

* 符号列表3




1. 这是个有序列表.
#. 是个有序列表.
#. 也有两项.
  

-------------

术语1
  这是术语1的定义。定义必须缩进。

  定义可以包含多段内容。

术语2
  这是术语2的定义。
  定义也可以包含多行内容。

------------
术语3:
 | 这些行
 | 在源文件里
 | 被分隔的一模一样.

------------


| 这些行
| 在源文件里
| 被分隔的一模一样。

| 这就话就算不用
| 空格来分开行,也会
| 被分为三行来展示

------------

这是一段正常文本. 下一段是代码文字::

  它不需要特别处理，仅是
  缩进就可以了.

  它可以有多行.

再是正常的文本段.

------------

下面是文字块内容::

  这是一段文字块
  同样也是文字块

  还是文字块

这是新的一段。

------------

.. image:: ./_static/图标_6.png

------------

def my_function(参数1, 参数2, 参数3):
  """函数的描述.

  :参数1: 参数1的描述说明
  :参数2: 参数2的描述说明
  :参数3: 参数3的描述说明
  :返回: 返回内容的描述说明

  """


------------

.. function:: foo(x)
              foo(y, z)
   :module: some.module.name

   返回用户输入的一行文本.

--------------------

>>> 1+1

------------
1. 枚举列表1
#. 枚举列表2
#. 枚举列表3

A. 枚举列表1
#. 枚举列表2
#. 枚举列表3

a. 枚举列表1
#. 枚举列表2
#. 枚举列表3



-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too


``echo "Hello World!";``

-----------------------------------------------------------------------------


双冒号方式 ::

  echo "Hello World!";

-----------------------------------------------------------------------------

访问 `我的博客1 <http://ramble.3vshej-1.cn>`_, 可以了解更多信息。



访问 `我的博客2`_, 可以了解更多信息。

.. _我的博客2: http://ramble.3vshej-2.cn


我的博客3地址是： http://ramble.3vshej-3.cn ，以了解更多信息。


这篇文章参考的是：`reStructuredText(rst)快速入门语法说明`__。

.. __: http://www.jianshu.com/p/1885d5570b37


==========
外连接
==========

`外连接`_，点击后链接到本页，且只能链到本页。


点击这里，查看 `我的首页 3vshej.cn <http://3vshej.cn/>`_


.. image:: ./_static/图标_6.png
  :width: 200px

.. image:: ./_static/loading_5.gif
  :width: 200px


=====  =====  ======
输入          输出
------------  ------
A      B      A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+



本文档参考自 [赵子清的技术文章]_

.. [赵子清的技术文章] 《使用Sphinx + reST编写文档》 https://www.cnblogs.com/zzqcn/p/5096876.html



当然，也参考了 seayxu [#简书]_ 的 reStructuredText(rst)快速入门语法说明 [#地址]_

脚注

.. [#简书] seayxu 简书 http://www.jianshu.com/u/3462d3ed1acd
.. [#地址] reStructuredText(rst)快速入门语法说明 http://www.jianshu.com/p/1885d5570b37



今天的日期是 |日期| 

.. |日期| replace:: 2022-01-01


下面是引用的内容：

    真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血

    人生的意志和劳动将创造奇迹般的奇迹

..

    真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血
    
    人生的意志和劳动将创造奇迹般的奇迹



>>> print "Hello World!"
Hello World!


上面部分

------------

下面部分



上面部分

===============

下面部分


..
  我是注释内容
  你们看不到我


.. note::
  注解型提示。

.. warning::
  警告型提示。

.. error::
  错误型提示。

.. caution::
  小心提示。

.. tip::
  普通提示。




.. index:: 创建, 索引, 测试