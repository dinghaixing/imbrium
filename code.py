# 中文等utf8 url转换为标准url
from urllib import parse
url = parse.quote(chinese_url, safe='!@#$%^&*()_+|~-=`<>?:"}{[];,./\\')



# pdf2docx 屏幕告警信息过多问题：

1. 找到 converter.py 文件。

	.local/lib/python3.7/site-packages/pdf2docx/converter.py 


2. 在 converter.py 文件顶部添加如下代码。

	logging.basicConfig(
	    level=logging.CRITICAL, 
	    format="[%(levelname)s] %(message)s")

	fitz.TOOLS.mupdf_display_errors(False)
	fitz.TOOLS.reset_mupdf_warnings()



# 通过 ssh 链接 jupyterlib 服务
sudo ssh -L 8889:127.0.0.1:8889 dinglish@112.47.15.93


# 批量杀进程
ps -elf | grep qa_extractor | awk '{print $4}' | xargs kill -9


# 查询文件夹内文件个数
ls -l|grep "^-"| wc -l



# pdf工具：
	pdftables camelot
	PyPDF2 
	PDFMiner 
	pdflib  
	PyFPDF 
	PDFTables 
	PyX 
	ReportLab 
	PyMuPDF 
	pdfrw 



