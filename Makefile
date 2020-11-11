
.PHONY: buildall
buildall:
	id=0 ; while [[ $$id -le 2 ]] ; do \
	jupyter nbconvert --execute --allow-errors --to pdf --template tex.tplx ./leccion_$$id/*.ipynb ; \
	((id = id + 1)) ; \
	done


ID?=0
.PHONY: build
build:
	jupyter nbconvert --execute --allow-errors --to pdf --template tex.tplx ./$$ID/*.ipynb
	jupyter nbconvert --execute --allow-errors --output='README.md' --to markdown ./$$ID/*.ipynb

