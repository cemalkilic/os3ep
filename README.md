# os3ep 

os3p stands for Operating Systems: Three Easy Pieces. It is a free online
operating systems book. The link to book is: http://pages.cs.wisc.edu/~remzi/OSTEP/

I created this simple python script to download the book which is in form of
chapter-by-chapter. Instead of downloading all chapters manually, renaming and
ordering by hand, I created this simple script.

It is simply gets the table where book content is placed. Parses the table and downloads the PDFs in parallel, thanks to multithreading.

## Installing

* Clone the repo.
* Activate your virtual environment ```source path/to/virtualenv/bin/activate```
* Install dependencies ```pip install -r requirements.txt```
* Start by ```python o3ep.py```


## Authors

* Cemal Kılıç

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

