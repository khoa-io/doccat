

PRESENTATION = presentation
PRESENTATION_SOURCE_FILE = presentation.tex
PRESENTATION_OUTPUT_FILE = presentation.pdf

HANDOUT = handout
HANDOUT_SOURCE_FILE = handout.tex
HANDOUT_OUTPUT_FILE = handout.pdf

HANDOUT_TEACHERS = handout_teachers
HANDOUT_TEACHERS_SOURCE_FILE = handout_teachers.tex
HANDOUT_TEACHERS_OUTPUT_FILE = handout_teachers.pdf

all: presentation handout handout_teachers

default: presentation

# Xây dựng presentation.pdf là tệp chính để chính chiếu
presentation:
	pdflatex $(PRESENTATION_SOURCE_FILE)
	pdflatex $(PRESENTATION_SOURCE_FILE)
	thumbpdf $(PRESENTATION_OUTPUT_FILE)
#	pdflatex $(PRESENTATION_SOURCE_FILE)
	rm -vf *.{aux,lo?,out,idx,toc,exa,ilg,ind,tpt,nav,vrb,snm,lof,log,lot}

# Xây dựng handout.pdf là tệp phụ cho ghi chú
handout:
	pdflatex $(HANDOUT_SOURCE_FILE)
	pdflatex $(HANDOUT_SOURCE_FILE)
	thumbpdf $(HANDOUT_OUTPUT_FILE)
#	pdflatex $(HANDOUT_SOURCE_FILE)
	rm -vf *.{aux,lo?,out,idx,toc,exa,ilg,ind,tpt,nav,vrb,snm,lof,log,lot}

handout_teachers:
	pdflatex $(HANDOUT_TEACHERS_SOURCE_FILE)
	pdflatex $(HANDOUT_TEACHERS_SOURCE_FILE)
	thumbpdf $(HANDOUT_TEACHERS_OUTPUT_FILE)
#	pdflatex $(HANDOUT_TEACHERS_SOURCE_FILE)
	rm -vf *.{aux,lo?,out,idx,toc,exa,ilg,ind,tpt,nav,vrb,snm,lof,log,lot}

# Dọn dẹp các tệp tạm trong quá trình xây dựng
clean:
	rm -vf *.{aux,lo?,out,idx,toc,exa,ilg,ind,tpt,nav,vrb,snm,lof,log,lot}

# Loại bỏ toàn bộ các tệp tạo ra do quá trình xây dựng
distclean: clean
	rm *.pdf
